from agents.base_agent import BaseAgent
from runtime.agent_context import AgentContext


class ResearchAgent(BaseAgent):
    """
    Research Agent
    """
    async def _execute(
        self,
        context: AgentContext
    ):
        context.state.research_result = (
            f"Research about {context.state.query}"
        )

        return context
