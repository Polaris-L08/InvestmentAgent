class EventStore:

    def __init__(self):

        self.events = []

    def append(
        self,
        event
    ):

        self.events.append(
            event
        )

    def get_all(self):

        return self.events