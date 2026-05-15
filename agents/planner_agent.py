from agents.base_agent import BaseAgent
from runtime.agent_context import AgentContext


class PlannerAgent(BaseAgent):

    async def _execute(
        self,
        context: AgentContext
    ):

        context.state.plan = [
            "research",
            "quant",
            "risk",
            "report"
        ]

        return context