"""Models for typing."""

from typing import Literal

Mode = Literal["customer", "rechargeSpot"]
TimeGrouping = Literal["day", "week", "month", "year"]

Notification_nl = Literal[
    "Gereed",
    "Transactie voorbereiden",
    "Remote transactie starten geaccepteerd",
    "Laden",
    "Laden (vol)",
    "Transactie afronden",
    "Commit transactie",
]
