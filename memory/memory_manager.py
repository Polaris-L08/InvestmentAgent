from memory.episodic_memory import EpisodicMemory
from memory.memory_item import MemoryItem
from memory.semantic_memory import SemanticMemory
from memory.working_memory import WorkingMemory


class MemoryManager:

    def __init__(self):

        self.working = WorkingMemory()

        self.episodic = EpisodicMemory()

        self.semantic = SemanticMemory()

    def remember(
        self,
        memory_item: MemoryItem
    ):

        self.working.add(memory_item)

        if (
            memory_item.importance
            > 0.7
        ):

            self.episodic.add_event(
                memory_item
            )

    def retrieve_context(
            self
    ):
        context = []

        context.extend(
            self.working.get_all()
        )

        context.extend(
            self.episodic.recent()
        )

        return context

    def consolidate(self):
        """
        整合
        :return:
        """

        for event in (
            self.episodic.events
        ):

            if (
                "momentum"
                in event.content.lower()
            ):

                self.semantic.store(
                    "momentum_strategy",
                    "Momentum investing "
                    "focuses on trend following."
                )