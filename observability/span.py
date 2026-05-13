import time
from pydantic import BaseModel
from typing import Optional


class Span(BaseModel):

    name: str

    start_time: float

    end_time: Optional[float] = None

    metadata: dict = {}

    def finish(self):

        self.end_time = time.time()

    @property
    def duration(self):

        if not self.end_time:

            return None

        return (
            self.end_time
            - self.start_time
        )