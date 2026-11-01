from __future__ import annotations

from collections.abc import Awaitable, Callable
from functools import wraps
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from .api import Api


def authenticated[**P, T](
    func: Callable[P, Awaitable[T]],
) -> Callable[P, Awaitable[T]]:
    """Ensure authentication before executing an API request."""

    @wraps(func)
    async def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        self = cast("Api", args[0])

        await self._ensure_authenticated()

        previous_token = self.token

        data = await func(*args, **kwargs)

        if not self._is_authentication_error(data):
            return data

        self.logger.debug("Authentication rejected. Refreshing token.")

        async with self._auth_lock:
            # Another coroutine may already have refreshed the token.
            if self.token == previous_token:
                await self.login()

        # Retry the original request once.
        data = await func(*args, **kwargs)

        if self._is_authentication_error(data):
            raise RuntimeError("Authentication failed after refreshing token")

        return data

    return wrapper
