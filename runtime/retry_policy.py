import asyncio


class RetryPolicy:

    def __init__(
        self,
        max_retry=3,
        delay=1
    ):

        self.max_retry = max_retry

        self.delay = delay

    async def execute(
        self,
        coro
    ):

        last_error = None

        for attempt in range(
            self.max_retry
        ):

            try:

                return await coro()

            except Exception as e:

                last_error = e

                await asyncio.sleep(
                    self.delay
                )

        raise last_error