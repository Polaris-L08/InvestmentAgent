from memory.shared_memory import (
    SharedMemory
)


class AgentContext:
    """
    Agent 执行时的运行环境.
        shared_memory
        workflow_state
        runtime_metadata
    """

    def __init__(
            self,
            state,
            shared_memory: SharedMemory
    ):
        self.state = state

        self.shared_memory = (
            shared_memory
        )
