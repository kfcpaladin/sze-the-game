import bisect
from .AttributeNotificationSystem import AttributeNotification

class PriorityAttributeMessage(AttributeNotification):
    def __init__(self, attribute):
        AttributeNotification.__init__(self, attribute)
        self._entries = []
        self.use_default = True

    def on_change(self, old, new):
        message = self.get_message(new)
        self.say(message)

    def add_entry(self, entry):
        bisect.insort(self._entries, entry)


    def add_message(self, message, _min):
        entry = PriorityMessage(message, _min)
        self.add_entry(entry)
    
    def get_message(self, value):
        for entry in reversed(self._entries):
            if value >= entry.value:
                return entry.message 

        if self.use_default and len(self._entries) > 0:
            return self._entries[0].message

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
