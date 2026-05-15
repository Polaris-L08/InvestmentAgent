from memory.shared_memory import SharedMemory
from workflows.workflow_base_state import WorkflowBaseState


class AgentContext:
    """
    Agent 执行时的运行环境.
        shared_memory
        workflow_state
        runtime_metadata
    """

    def __init__(
            self,
            state: WorkflowBaseState,
            shared_memory: SharedMemory
    ):
        self.state = state

        self.shared_memory = (
            shared_memory
        )
