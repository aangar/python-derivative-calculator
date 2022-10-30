class ValueWithEnum:
    enum = None
    value = None
    def __init__(self, value, enum):
        self.enum = enum
        self.value = value