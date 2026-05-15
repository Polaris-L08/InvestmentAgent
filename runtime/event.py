from pydantic import BaseModel
from typing import Any
import time
import uuid


class Event(BaseModel):

    event_id: str = (
        str(uuid.uuid4())
    )

    event_type: str

    payload: dict[str, Any]

    timestamp: float = (
        time.time()
    )