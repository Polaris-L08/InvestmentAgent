from runtime.checkpoint import Checkpoint
from runtime.checkpoint_store import CheckpointStore

"""
当前其实是把恢复机制与workflow混合在一起了
事实上，Graph Workflow负责定义结构
Durable Runtime负责执行与恢复
"""
class DurableWorkflow:

    def __init__(
        self,
        workflow_id: str,
        checkpoint_store: CheckpointStore
    ):

        self.workflow_id = (
            workflow_id
        )

        self.checkpoint_store = (
            checkpoint_store
        )

        self.steps = []

    def add_step(
        self,
        step_name,
        handler
    ):

        self.steps.append(
            (step_name, handler)
        )

    async def run(
        self,
        state
    ):

        for step_name, handler in (
            self.steps
        ):

            checkpoint = Checkpoint(
                workflow_id=self.workflow_id,

                step=step_name,

                state=state
            )

            self.checkpoint_store.save(
                checkpoint
            )

            state = await handler(state)

        return state

    async def recover(self):

        checkpoint = (
            self.checkpoint_store.load(
                self.workflow_id
            )
        )

        return checkpoint

    async def resume(self):

        checkpoint = (
            self.checkpoint_store.load(
                self.workflow_id
            )
        )

        if not checkpoint:

            raise Exception(
                "No checkpoint found"
            )

        state = checkpoint.state

        start_index = 0

        for i, (
            step_name,
            _
        ) in enumerate(self.steps):

            if (
                step_name
                == checkpoint.step
            ):

                start_index = i + 1

        for step_name, handler in (
            self.steps[start_index:]
        ):

            state = await handler(
                state
            )

        return state