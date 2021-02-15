class Time:

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    @classmethod
    def from_string(cls, text):
        hour, minute = text.split(":")
        return cls(hour, minute)