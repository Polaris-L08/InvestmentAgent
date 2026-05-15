import asyncio

from runtime.event import Event
from runtime.event_bus import (
    EventBus
)


class ResearchAgent:

    def __init__(
        self,
        event_bus: EventBus
    ):

        self.event_bus = (
            event_bus
        )

    async def run(self):

        print(
            "researching..."
        )

        await asyncio.sleep(2)

        result = {
            "symbol": "AAPL",
            "trend": "bullish"
        }

        await self.event_bus.publish(

            Event(
                event_type=(
                    "research_completed"
                ),

                payload=result
            )
        )


class AnalysisAgent:

    async def on_research_completed(
        self,
        event: Event
    ):

        print(
            "analysis:",
            event.payload
        )


async def main():

    event_bus = EventBus()

    analysis_agent = AnalysisAgent()

    event_bus.subscribe(

        "research_completed",

        analysis_agent.on_research_completed
    )

    research_agent = ResearchAgent(event_bus)

    await research_agent.run()


asyncio.run(main())