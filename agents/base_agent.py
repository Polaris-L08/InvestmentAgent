from runtime.agent_context import AgentContext
from runtime.middleware.pipeline import MiddlewarePipeline
from workflows.shared_state import SharedState


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
                  context: AgentContext
                  ):

        result = await self.pipeline.execute(
            context,
            self._execute
        )

        return result

    async def _execute(self, context: AgentContext):
        raise NotImplementedError
