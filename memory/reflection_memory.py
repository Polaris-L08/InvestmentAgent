class ReflectionMemory:

    def __init__(self):

        self.reflections = []

    def add(
        self,
        reflection
    ):

        self.reflections.append(
            reflection
        )

    def recent(
        self,
        n=5
    ):

        return self.reflections[-n:]