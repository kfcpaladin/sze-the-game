import bisect

class PopupsManager:
    def __init__(self):
        self.popups = []
        self._listeners = []

    # adds a message to a list
    def add(self, popup):
        if popup in self.popups:
            return
        bisect.insort(self.popups, popup)
        self._on_populate()

    def update(self, speed):
        for popup in self.popups:
            popup.update(speed)
        self.popups = filter(lambda p: p.is_alive, self.popups)

    def listen_populate(self, listener):
        self._listeners.append(listener)
    
    def _on_populate(self):
        for listener in self._listeners:
            listener(self)

    @property
    def total(self):
        return len(self.popups)

    # clear popup list
    def clear(self):
        self.popups.clear()
        self.popups = []