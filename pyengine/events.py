class Event:
    type: int
    data: tuple | None
    def __init__(self, event_type: int = 0, data: tuple | None = None):
        self.type = event_type
        self.data = data


QUIT = 1
TEST = 2