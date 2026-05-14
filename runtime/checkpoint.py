from pydantic import BaseModel
from typing import Any
import time


class Checkpoint(BaseModel):

    workflow_id: str

    step: str

    state: dict

    timestamp: float = (
        time.time()
    )