# Fiftyfive

Python 3 package to retrieve EV charger data from 50five

## Installation

```bash
pip3 install fiftyfive
```

## Usage

```Python
import asyncio

from aiohttp import ClientSession
from fiftyfive import Api, CustomerType, Market, NetworkOverview


async def main():
    """Main module"""

    async with ClientSession() as session:
        api = Api(session, "email", "password", Market.BELUX, CustomerType.FORMER_SHELL)

        result = await api.make_requests([NetworkOverview()])
        print(result)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
```

## Email MFA and session persistence

`Api.authenticate()` performs the username/password step without requesting an
email code. It returns `AuthenticationResult.MFA_REQUIRED` when the provider
needs email verification. Only `Api.request_mfa_code()` loads the provider's
MFA form and triggers the email; pass its returned challenge token together
with the user's code to `Api.complete_mfa()`.

Consumers can persist `Api.export_session()` and restore it with
`Api.restore_session()`. API calls detect rejected or expired sessions and make
one safe password-only renewal attempt. If the provider still requires MFA,
`make_requests()` raises `MfaRequiredError` without requesting another code.

## WARNING

50five uses separate endpoints depending on the market (belux, nl, de, ...) as
well as whether or not you were migrated over from Shell Recharge. As I myself
only have access to an account in the belux market as an ex-Shell customer, I
cannot do any testing/reverse engineering on the other markets, so I can't give
any guarantee anything will work for accounts in them.
