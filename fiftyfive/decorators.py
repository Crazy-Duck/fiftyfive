from functools import wraps
from typing import Callable


def authenticated(func: Callable):
    """Authenticate when a call returns an empty list"""

    @wraps(func)
    async def wrapper(self, *args, **kwargs):
        if not [c for c in self.session.cookie_jar if c.key == "PHPSESSID"]:
            await self.login()

        return await func(self, *args, **kwargs)

    return wrapper