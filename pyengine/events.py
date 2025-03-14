class Event:
    """
    A representation of an event.
    :param event_type: The event type of this event : default 0
    :param data: The data of this event : default None

    When sent by the ``APP.sendEvent()`` function where ``APP`` is the instance of the App class, a default value for the event data is set to a tuple containing the event timestamp and any additional data which defaults to None
    """
    type: int
    data: tuple | None
    def __init__(self, event_type: int = 0, data: tuple | None = None):
        self.type = event_type
        self.data = data


QUIT = 1
TEST = 2