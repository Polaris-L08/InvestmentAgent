from agents.base_agent import BaseAgent
from runtime.agent_context import AgentContext
from workflows.shared_state import SharedState


class RiskAgent(BaseAgent):
    async def _execute(
            self,
            context: AgentContext
    ):
        context.state.risk_result = (
            "Risk level: Medium"
        )