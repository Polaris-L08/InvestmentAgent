class SharedMemory:

    def __init__(self):

        self.memory = {}

    def set(
        self,
        key: str,
        value
    ) -> None:

        self.memory[key] = value

    def get(
        self,
        key: str
    ):

        return self.memory.get(key)

    def dump(self):

        return self.memory