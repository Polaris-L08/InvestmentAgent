from agents.base_agent import BaseAgent
from runtime.agent_context import AgentContext
from workflows.shared_state import SharedState


class QuantAgent(BaseAgent):
    """
    Quant Agent
    """
    async def _execute(
        self,
        context: AgentContext
    ):
        context.state.quant_result = (
            f"Backtest result: 18% CAGR"
        )