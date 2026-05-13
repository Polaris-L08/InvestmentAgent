
class BaseAgent:
    def __init__(
            self,
            name: str,
    description: str,
    llm_client):
        self.name = name
        self.description = description
        self.llm = llm_client

    async def run(self,
                  state
                  ):
        raise NotImplementedError
