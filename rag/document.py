from pydantic import BaseModel
from typing import Any


class Document(BaseModel):

    id: str

    content: str

    metadata: dict[str, Any] = {}