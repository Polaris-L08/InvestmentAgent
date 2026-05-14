from observability.tracer import Tracer
from runtime.middleware.pipeline import MiddlewarePipeline
from runtime.retry_policy import RetryPolicy
from runtime.timeout import with_timeout


class BaseAgent:
    def __init__(
            self,
            name: str,
            description: str,
            llm_client,
            pipeline: MiddlewarePipeline,
    ):
        self.name = name
        self.description = description
        self.llm = llm_client
        self.pipeline = pipeline

    async def run(self,
                  state
                  ):
        # span = self.tracer.start_span(
        #     self.name
        # )
        #
        # result = await with_timeout(
        #     self.retry_policy.execute(
        #         lambda: self._execute(
        #             state
        #         )
        #     ),
        #     timeout=30
        # )
        #
        # span.finish()

        result = await self.pipeline.execute(
            state,
            self._execute
        )

        return result

    async def _execute(self, state):
        raise NotImplementedError
