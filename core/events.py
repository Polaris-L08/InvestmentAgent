from pydantic import BaseModel
from typing import Any


class RuntimeEvent(BaseModel):

    type: str

    data: Any

    timestamp: float | None = None