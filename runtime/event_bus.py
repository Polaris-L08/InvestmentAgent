from collections import defaultdict
from typing import Awaitable
from typing import Callable

from runtime.event import (
    Event
)


EventHandler = Callable[
    [Event],
    Awaitable[None]
]


class EventBus:

    def __init__(self):

        self.subscribers = (
            defaultdict(list)
        )

    def subscribe(
        self,
        event_type: str,
        handler: EventHandler
    ) -> None:

        self.subscribers[
            event_type
        ].append(handler)

    async def publish(
        self,
        event: Event
    ) -> None:

        handlers = self.subscribers.get(
            event.event_type,
            []
        )

        for handler in handlers:

            await handler(event)