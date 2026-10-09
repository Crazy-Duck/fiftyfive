"""Tests for the 50five authentication lifecycle."""

# ruff: noqa: PT009, PT027, S106

from __future__ import annotations

import unittest
from collections import deque
from http.cookies import SimpleCookie
from typing import Any, Self

from aiohttp import CookieJar
from fiftyfive import (
    Api,
    AuthenticationResult,
    CustomerType,
    Market,
    MfaRequiredError,
    NetworkOverview,
)
from yarl import URL

_HTTP_BAD_REQUEST = 400


class FakeResponse:
    """Minimal aiohttp response context manager."""

    def __init__(
        self,
        status: int,
        *,
        location: str = "",
        text: str = "",
    ) -> None:
        """Initialize a fake response."""
        self.status = status
        self.headers = {"Location": location} if location else {}
        self._text = text

    async def __aenter__(self) -> Self:
        """Enter the response context."""
        return self

    async def __aexit__(self, *args: object) -> None:
        """Exit the response context."""

    async def text(self) -> str:
        """Return response text."""
        return self._text

    def raise_for_status(self) -> None:
        """Raise for unexpected test response statuses."""
        if self.status >= _HTTP_BAD_REQUEST:
            raise RuntimeError(self.status)


class FakeSession:
    """Queue-backed aiohttp session replacement."""

    def __init__(
        self,
        *,
        gets: list[FakeResponse] | None = None,
        posts: list[FakeResponse] | None = None,
    ) -> None:
        """Initialize response queues."""
        self.cookie_jar = CookieJar(unsafe=True)
        self.gets = deque(gets or [])
        self.posts = deque(posts or [])
        self.get_calls: list[tuple[str, dict[str, Any]]] = []
        self.post_calls: list[tuple[str, dict[str, Any]]] = []

    def get(self, url: str, **kwargs: Any) -> FakeResponse:
        """Return the next GET response."""
        self.get_calls.append((url, kwargs))
        return self.gets.popleft()

    def post(self, url: str, **kwargs: Any) -> FakeResponse:
        """Return the next POST response."""
        self.post_calls.append((url, kwargs))
        return self.posts.popleft()


def create_api(session: FakeSession) -> Api:
    """Create an API client for tests."""
    return Api(
        session=session,  # type: ignore[arg-type]
        email="joris@example.com",
        password="secret",
        market=Market.NL,
        customer_type=CustomerType.FORMER_SHELL,
    )


def seed_session_cookie(api: Api) -> None:
    """Seed an expired session cookie."""
    cookie: SimpleCookie[str] = SimpleCookie()
    cookie["PHPSESSID"] = "expired"
    api.session.cookie_jar.update_cookies(cookie, response_url=URL(api.url))


class AuthenticationTests(unittest.IsolatedAsyncioTestCase):
    """Test authentication without contacting the provider."""

    async def test_authenticate_detects_mfa_without_requesting_email(self) -> None:
        """Password login should detect MFA without loading the MFA form."""
        session = FakeSession(
            posts=[FakeResponse(302, location="/2fa")],
        )
        api = create_api(session)

        result = await api.authenticate()

        self.assertIs(result, AuthenticationResult.MFA_REQUIRED)
        self.assertEqual(session.get_calls, [])

    async def test_request_mfa_code_extracts_challenge(self) -> None:
        """The explicit MFA method should load the form once."""
        session = FakeSession(
            gets=[
                FakeResponse(
                    200,
                    text='<input name="_token" value="csrf-token">',
                )
            ]
        )
        api = create_api(session)

        challenge = await api.request_mfa_code()

        self.assertEqual(challenge, "csrf-token")
        self.assertEqual(len(session.get_calls), 1)
        self.assertTrue(session.get_calls[0][0].endswith("/2fa"))

    async def test_password_only_session_renewal_retries_request_once(self) -> None:
        """An expired session should renew and retry for non-MFA accounts."""
        session = FakeSession(
            gets=[
                FakeResponse(302, location="/Login"),
                FakeResponse(200, text='[[{"IDX": "charger"}]]'),
            ],
            posts=[FakeResponse(302, location="/Overview")],
        )
        api = create_api(session)
        seed_session_cookie(api)

        result = await api.make_requests([NetworkOverview()])

        self.assertEqual(result, [[{"IDX": "charger"}]])
        self.assertEqual(len(session.post_calls), 1)
        self.assertEqual(len(session.get_calls), 2)

    async def test_expired_session_raises_mfa_without_requesting_code(self) -> None:
        """Background renewal must not load the MFA page or trigger email."""
        session = FakeSession(
            gets=[FakeResponse(302, location="/Login")],
            posts=[FakeResponse(302, location="/2fa")],
        )
        api = create_api(session)
        seed_session_cookie(api)

        with self.assertRaises(MfaRequiredError):
            await api.make_requests([NetworkOverview()])

        self.assertEqual(len(session.get_calls), 1)
        self.assertFalse(any(url.endswith("/2fa") for url, _ in session.get_calls))

    async def test_session_state_round_trip(self) -> None:
        """Exported cookies should restore into another client."""
        first = create_api(FakeSession())
        seed_session_cookie(first)

        state = first.export_session()
        second = create_api(FakeSession())
        second.restore_session(state)

        cookies = second.session.cookie_jar.filter_cookies(URL(second.url))
        self.assertEqual(cookies["PHPSESSID"].value, "expired")
