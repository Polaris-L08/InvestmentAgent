from pydantic import BaseModel, Field
from typing import List

from core.messages import Message


class AgentState(BaseModel):
    """
    Agent状态
    """
    messages: List[Message] = Field(
        default_factory=list
    )

    iteration_count: int = 0

    max_iterations: int = 10

    finished: bool = False

    error: str | None = None