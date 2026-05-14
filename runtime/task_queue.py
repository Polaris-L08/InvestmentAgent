import asyncio


class TaskQueue:

    def __init__(self):

        self.queue = asyncio.Queue()

    async def put(
        self,
        task
    ):

        await self.queue.put(
            task
        )

    async def get(self):

        return await self.queue.get()