from agents.base_agent import BaseAgent
from workflows.shared_state import SharedState


class RiskAgent(BaseAgent):
    async def run(
            self,
            state: SharedState
    ):
        state.risk_result = (
            "Risk level: Medium"
        )