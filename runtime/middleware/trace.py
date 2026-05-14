from runtime.middleware.base import Middleware


class TraceMiddleware(Middleware):

    def __init__(
        self,
        tracer
    ):

        self.tracer = tracer

    async def process(
        self,
        context,
        next_handler
    ):

        span = (
            self.tracer.start_span(
                "agent_run"
            )
        )

        try:

            return await next_handler(
                context
            )

        finally:

            span.finish()