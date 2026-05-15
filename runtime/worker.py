from runtime.event import Event
from runtime.event_bus import EventBus


class Worker:

    def __init__(
            self,
            queue,
            agent_registry,
            event_bus: EventBus
    ):
        self.queue = queue

        self.agent_registry = (
            agent_registry
        )

        self.event_bus = event_bus

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

            # await agent.run(
            #     task.payload
            # )
            await self.event_bus.publish(
                Event(
                    event_type="memory",
                    payload={
                        "agent_name": task.agent_name,
                        "memory": agent.memory
                    }
                )
            )

