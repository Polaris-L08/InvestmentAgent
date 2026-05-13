from agents.base_agent import BaseAgent
from workflows.shared_state import SharedState


class ResearchAgent(BaseAgent):
    """
    Research Agent
    """
    async def run(
        self,
        state: SharedState
    ):
        state.research_result = (
            f"Research about {state.query}"
        )

        return state
