import bisect

class PriorityAttributeMessage:
    def __init__(self):
        self._entries = []
        self.use_default = True

    def add_message(self, message, _min):
        entry = PriorityMessage(message, _min)
        self._entries.insort(entry)
    
    def get_message(self, value):
        for entry in in self._entries:
            if entry.value <= value:
                return entry.message 
        elif self.use_default and len(self._entries) > 0:
            return self._entries[-1].message

class PriorityMessage:
    def __init__(self, message, value):
        self.message = message
        self.value = value
    
    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value 
