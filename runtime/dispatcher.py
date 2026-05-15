from runtime.task_queue import TaskQueue


class Dispatcher:

    def __init__(
        self,
        queue: TaskQueue
    ):

        self.queue = queue

    async def dispatch(
        self,
        task
    ):

        await self.queue.put(
            task
        )