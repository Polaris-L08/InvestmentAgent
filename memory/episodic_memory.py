class EpisodicMemory:
    """
    长期记忆（经历过的事件）
    """

    def __init__(self):

        self.events = []

    def add_event(
        self,
        memory_item
    ):

        self.events.append(memory_item)

    def recent(
        self,
        n=5
    ):

        return self.events[-n:]