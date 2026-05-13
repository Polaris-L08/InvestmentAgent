from pydantic import BaseModel
from typing import Any
import time


class MemoryItem(BaseModel):

    id: str

    content: str

    memory_type: str

    metadata: dict[str, Any] = {}

    importance: float = 0.0

    created_at: float = time.time()