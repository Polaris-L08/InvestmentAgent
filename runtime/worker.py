class Worker:

    def __init__(
        self,
        queue,
        agent_registry
    ):

        self.queue = queue

        self.agent_registry = (
            agent_registry
        )

    async def run(self):

        while True:

            task = await self.queue.get()

            print(
                f"WORKER EXEC:"
                f"{task.agent_name}"
            )

            agent = (
                self.agent_registry[
                    task.agent_name
                ]
            )

            await agent.run(
                task.payload
            )
