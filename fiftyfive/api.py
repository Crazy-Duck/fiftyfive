"""The 50five API client."""

from __future__ import annotations

import json
import logging
import re
from collections.abc import Mapping
from enum import StrEnum
from http.cookies import SimpleCookie
from typing import TYPE_CHECKING, Any

from yarl import URL

if TYPE_CHECKING:
    from aiohttp import ClientResponse, ClientSession

    from .requests import Request

_HTTP_OK = 200
_HTTP_FOUND = 302
_HTTP_REDIRECT_MIN = 300
_HTTP_REDIRECT_MAX = 400
_UNAUTHORIZED_STATUSES = {401, 403}
_TOKEN_PATTERNS = (
    re.compile(
        r"""name=["']_token["'][^>]*?value=["']([^"']+)["']""",
        re.IGNORECASE,
    ),
    re.compile(
        r"""value=["']([^"']+)["'][^>]*?name=["']_token["']""",
        re.IGNORECASE,
    ),
)


class AuthenticationError(Exception):
    """Raised when the provider rejects authentication."""


class MfaRequiredError(AuthenticationError):
    """Raised when interactive email verification is required."""


class AuthenticationResult(StrEnum):
    """Result of a non-interactive authentication attempt."""

    AUTHENTICATED = "authenticated"
    MFA_REQUIRED = "mfa_required"
    INVALID_CREDENTIALS = "invalid_credentials"


class Market(StrEnum):
    """50five market."""

    AT = "at"
    BELUX = "belux"
    DE = "de"
    FR = "fr"
    NL = "nl"
    UK = "uk"
    NONE = ""


class CustomerType(StrEnum):
    """50five customer type."""

    FIFTYFIVE = "fiftyfive"
    FORMER_SHELL = "shell"


class Api:
    """Client for the 50five portal API."""

    def __init__(
        self,
        session: ClientSession,
        email: str,
        password: str,
        market: Market,
        customer_type: CustomerType = CustomerType.FORMER_SHELL,
    ) -> None:
        """Initialize the client."""
        self.session = session
        self.email = email
        self.password = password
        self.url = (
            f"https://50five"
            f"{'-s' if customer_type == CustomerType.FORMER_SHELL else ''}"
            f"{market}.evc-net.com"
        )
        self.api = f"{self.url}/api/ajax"
        self.logger = logging.getLogger("fiftyfive")

    async def logout(self) -> None:
        """Log out of the portal."""
        async with self.session.get(f"{self.url}/Logout") as response:
            response.raise_for_status()

    async def login(self) -> bool:
        """Log in for backwards compatibility with the pre-MFA API."""
        return await self.authenticate() is AuthenticationResult.AUTHENTICATED

    async def authenticate(self) -> AuthenticationResult:
        """Attempt password authentication without requesting an MFA email."""
        data = {
            "emailField": self.email,
            "passwordField": self.password,
            "Login": "Log in",
        }
        async with self.session.post(
            url=f"{self.url}/Login/Login",
            data=data,
            allow_redirects=False,
        ) as response:
            if response.status != _HTTP_FOUND:
                return AuthenticationResult.INVALID_CREDENTIALS
            location = response.headers.get("Location", "")

        result = self._authentication_result_from_location(location)
        if result is not None:
            return result

        async with self.session.get(
            f"{self.url}/",
            allow_redirects=False,
        ) as response:
            location = response.headers.get("Location", "")
            if response.status == _HTTP_OK and not location:
                return AuthenticationResult.AUTHENTICATED

        return (
            self._authentication_result_from_location(location)
            or AuthenticationResult.INVALID_CREDENTIALS
        )

    async def request_mfa_code(self) -> str:
        """Request one email MFA code and return the form challenge token."""
        async with self.session.get(f"{self.url}/2fa") as response:
            response.raise_for_status()
            html = await response.text()

        for pattern in _TOKEN_PATTERNS:
            if match := pattern.search(html):
                return match.group(1)

        msg = "The 50five MFA form did not contain a challenge token"
        raise AuthenticationError(msg)

    async def complete_mfa(self, code: str, challenge: str) -> bool:
        """Submit an email MFA code."""
        data = {
            "_auth_code": code.strip(),
            "_token": challenge,
            "VerifyOtp": "Verify",
        }
        async with self.session.post(
            f"{self.url}/2fa_check",
            data=data,
            allow_redirects=False,
        ) as response:
            if response.status != _HTTP_FOUND:
                return False
            location = response.headers.get("Location", "")

        normalized = location.lower()
        return "2fa" not in normalized and "login" not in normalized

    def export_session(self) -> dict[str, Any]:
        """Export serializable cookies for this portal."""
        cookies = self.session.cookie_jar.filter_cookies(URL(self.url))
        return {"cookies": {name: morsel.value for name, morsel in cookies.items()}}

    def restore_session(self, state: Mapping[str, Any]) -> None:
        """Restore cookies exported by :meth:`export_session`."""
        raw_cookies = state.get("cookies", state)
        if not isinstance(raw_cookies, Mapping):
            return

        cookies = SimpleCookie()
        for name, value in raw_cookies.items():
            if isinstance(name, str) and isinstance(value, str):
                cookies[name] = value

        if cookies:
            self.session.cookie_jar.update_cookies(
                cookies,
                response_url=URL(self.url),
            )

    async def make_requests(self, requests: list[Request]) -> Any:
        """Make API requests, renewing a password-only session once if needed."""
        if not self._has_session_cookie():
            self._raise_for_authentication_result(await self.authenticate())

        payload, authentication_required = await self._make_requests_once(requests)
        if not authentication_required:
            return payload

        self._clear_session_cookie()
        self._raise_for_authentication_result(await self.authenticate())

        payload, authentication_required = await self._make_requests_once(requests)
        if authentication_required:
            msg = "The restored 50five session could not be renewed"
            raise AuthenticationError(msg)
        return payload

    async def _make_requests_once(
        self,
        requests: list[Request],
    ) -> tuple[Any, bool]:
        """Make one provider request and report whether authentication is needed."""
        params = {
            "requests": json.dumps(
                dict(enumerate([request.request for request in requests]))
            )
        }
        async with self.session.get(
            self.api,
            params=params,
            allow_redirects=False,
        ) as response:
            if self._response_requires_authentication(response):
                return None, True
            text = await response.text()

        try:
            payload = json.loads(text)
        except json.JSONDecodeError:
            normalized = text.lower()
            if "login" in normalized or "2fa" in normalized:
                return None, True
            raise

        return payload, payload == []

    @staticmethod
    def _response_requires_authentication(response: ClientResponse) -> bool:
        """Return whether an API response points to an authentication page."""
        if response.status in _UNAUTHORIZED_STATUSES:
            return True
        if _HTTP_REDIRECT_MIN <= response.status < _HTTP_REDIRECT_MAX:
            location = response.headers.get("Location", "").lower()
            return "login" in location or "2fa" in location
        return False

    @staticmethod
    def _authentication_result_from_location(
        location: str,
    ) -> AuthenticationResult | None:
        """Map a redirect location to an authentication result."""
        normalized = location.lower()
        if "2fa" in normalized:
            return AuthenticationResult.MFA_REQUIRED
        if "login" in normalized:
            return AuthenticationResult.INVALID_CREDENTIALS
        if location:
            return AuthenticationResult.AUTHENTICATED
        return None

    @staticmethod
    def _raise_for_authentication_result(result: AuthenticationResult) -> None:
        """Raise the appropriate exception for a failed authentication result."""
        if result is AuthenticationResult.AUTHENTICATED:
            return
        if result is AuthenticationResult.MFA_REQUIRED:
            msg = "50five email verification is required"
            raise MfaRequiredError(msg)
        msg = "50five rejected the supplied credentials"
        raise AuthenticationError(msg)

    def _has_session_cookie(self) -> bool:
        """Return whether the portal session cookie is present."""
        cookies = self.session.cookie_jar.filter_cookies(URL(self.url))
        return "PHPSESSID" in cookies

    def _clear_session_cookie(self) -> None:
        """Remove a rejected session cookie before a renewal attempt."""
        self.session.cookie_jar.clear(
            lambda morsel: (
                morsel.key == "PHPSESSID"
                and morsel["domain"].lstrip(".") == URL(self.url).host
            )
        )
