import bisect

class PriorityList:
    def __init__(self):
        self._entries = []
        self.use_default = True

    def add_entry(self, entry):
        bisect.insort(self._entries, entry)

    def get_entry(self, key):
        for entry in reversed(self._entries):
            if key >= entry.key:
                return entry.value 

        if self.use_default and len(self._entries) > 0:
            return self._entries[0].value

class PriorityEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value 
