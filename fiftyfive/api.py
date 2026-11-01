"""The 50five API code"""

import logging
from asyncio import Lock
from time import monotonic
from uuid import uuid4

from httpx import AsyncClient
from sgqlc.endpoint.httpx import HTTPXEndpoint
from sgqlc.operation import Operation

from .decorators import authenticated
from .schema import schema

GRAPHQL_API = "https://lms.servicelayer.platform-01.plugz.dev/graphql"


class Api:
    """Class to make API requests"""

    def __init__(
        self,
        client: AsyncClient,
        email: str,
        password: str,
        plugz_application_id: str | None = None,
    ):
        """Initialize the session."""
        self.logger = logging.getLogger("50five")

        self.email = email
        self.password = password
        self.token = ""
        self.token_expires_at = 0.0
        self._auth_lock = Lock()
        self.plugz_application_id = plugz_application_id or str(uuid4())

        headers = {"plugz-application-id": self.plugz_application_id}
        self.endpoint = HTTPXEndpoint(GRAPHQL_API, headers, client=client)

    def _is_authentication_error(self, data: dict) -> bool:
        """Check whether the GraphQL response contains an authentication error."""

        errors = data.get("errors", [])

        return any(
            "You are not authorized to perform this action" in error.get("message", "")
            for error in errors
        )

    async def _ensure_authenticated(self) -> None:
        """Ensure we have a valid authentication token."""

        if self.token and monotonic() < self.token_expires_at:
            return

        async with self._auth_lock:
            # Double-check after acquiring the lock.
            if self.token and monotonic() < self.token_expires_at:
                return

            self.logger.debug("Token expired. Logging in.")
            await self.login()

    async def login(self) -> bool:
        """Authenticate to the 50five API to obtain a JWT token."""

        op = Operation(schema.Mutation)
        login = op.login_fifty_five(password=self.password, email=self.email)
        login.access_token()
        login.token_type()
        login.expires_in()
        data = await self.endpoint(op)

        if data.get("errors"):
            raise RuntimeError("Login failed")

        result = (op + data).login_fifty_five
        if not result or not result.access_token:
            raise RuntimeError("Login did not return access token")

        self.token = result.access_token
        self.token_expires_at = monotonic() + max(0, int(result.expires_in - 30))
        self.endpoint.base_headers["Authorization"] = f"Bearer {self.token}"
        
        return True

    @authenticated
    async def make_request(self, op: Operation) -> dict:
        """Make a graphql request"""
        return await self.endpoint(op)
