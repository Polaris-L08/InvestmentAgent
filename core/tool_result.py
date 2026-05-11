from pydantic import BaseModel
from typing import Any


class ToolResult(BaseModel):

    success: bool

    content: Any = None

    error: str | None = None

    metadata: dict = {}