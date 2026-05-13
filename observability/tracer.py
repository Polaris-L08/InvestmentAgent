import uuid
import time

from observability.trace import Trace
from observability.span import Span


class Tracer:

    def __init__(self):

        self.current_trace = None

    def start_trace(self):

        self.current_trace = Trace(
            trace_id=str(uuid.uuid4())
        )

        return self.current_trace

    def start_span(
        self,
        name: str,
        metadata=None
    ):

        span = Span(
            name=name,
            start_time=time.time(),
            metadata=metadata or {}
        )

        self.current_trace.add_span(
            span
        )

        return span