class SemanticMemory:
    """
    抽象知识（概念知识）
    """

    def __init__(self):

        self.knowledge = {}

    def store(
        self,
        key,
        value
    ):

        self.knowledge[key] = value

    def retrieve(
        self,
        key
    ):

        return self.knowledge.get(key)