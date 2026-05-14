from agents.base_agent import BaseAgent
from workflows.shared_state import SharedState


class RiskAgent(BaseAgent):
    async def _execute(
            self,
            state: SharedState
    ):
        state.risk_result = (
            "Risk level: Medium"
        )