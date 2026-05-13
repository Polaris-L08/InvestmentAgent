from workflows.shared_state import SharedState


class Supervisor:
    def __init__(self, agents: dict):
        self.agents = agents

    async def run(
            self,
            state: SharedState
    ):
        planner = self.agents["planner"]

        state = await planner.run(state)

        for step in state.plan:
            if step == "research":
                state = await self.agents["research"].run(state)
            elif step == "quant":
                state = await self.agents["quant"].run(state)
            elif step == "risk":
                state = await self.agents["risk"].run(state)

        return state
