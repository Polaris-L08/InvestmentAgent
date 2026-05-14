from agents.base_agent import BaseAgent
from workflows.shared_state import SharedState


class QuantAgent(BaseAgent):
    """
    Quant Agent
    """
    async def _execute(
        self,
        state: SharedState
    ):
        state.quant_result = (
            f"Backtest result: 18% CAGR"
        )