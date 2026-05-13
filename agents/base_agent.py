from observability.tracer import Tracer


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

    async def run(self,
                  state
                  ):
        # raise NotImplementedError
        span = self.tracer.start_span(
            self.name
        )

        result = await self._run(state)

        span.finish()

        return result

    async def _run(self, state):
        raise NotImplementedError
