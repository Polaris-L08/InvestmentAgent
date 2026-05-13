from agents.base_agent import BaseAgent


class PlannerAgent(BaseAgent):

    async def _run(
        self,
        state
    ):

        state.plan = [
            "research",
            "quant",
            "risk",
            "report"
        ]

        return state