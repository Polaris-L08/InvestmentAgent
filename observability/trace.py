from pydantic import BaseModel
from typing import List
from observability.span import Span


class Trace(BaseModel):

    trace_id: str

    spans: List[Span] = []

    def add_span(
        self,
        span: Span
    ):

        self.spans.append(span)