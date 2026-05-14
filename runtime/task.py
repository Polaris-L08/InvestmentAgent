from pydantic import BaseModel
from typing import Any


class Task(BaseModel):

    task_id: str

    agent_name: str

    payload: dict[str, Any]