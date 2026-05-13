from observability.tracer import Tracer
from runtime.retry_policy import RetryPolicy
from runtime.timeout import with_timeout


class BaseAgent:
    def __init__(
            self,
            name: str,
    description: str,
    llm_client):
        self.name = name
        self.description = description
        self.llm = llm_client
        self.tracer = Tracer()
        self.retry_policy = RetryPolicy()

    async def run(self,
                  state
                  ):
        span = self.tracer.start_span(
            self.name
        )

        result = await with_timeout (
            self.retry_policy.execute(
                lambda: self._run(
                    state
                )
            ),
            timeout=30
        )

        span.finish()

        return result

    async def _run(self, state):
        raise NotImplementedError
