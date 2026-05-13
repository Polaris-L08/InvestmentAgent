import asyncio


async def with_timeout(
    coro,
    timeout=30
):

    return await asyncio.wait_for(
        coro,
        timeout=timeout
    )