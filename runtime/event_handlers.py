from runtime.event import (
    Event
)


async def reflection_handler(
    event: Event
) -> None:

    print(
        "reflection triggered:",
        event.payload
    )


async def memory_handler(
    event: Event
) -> None:

    print(
        "memory update:",
        event.payload
    )