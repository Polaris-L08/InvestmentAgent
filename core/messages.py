from typing import Optional, Literal
from pydantic import BaseModel


Role = Literal[
    "system",
    "user",
    "assistant",
    "tool"
]


class Message(BaseModel):
    role: Role
    content: str
    tool_call_id: Optional[str] = None
    name: Optional[str] = None