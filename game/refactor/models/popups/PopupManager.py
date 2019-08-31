import bisect

class PopUpManager:
    screen_callback = None

    def __init__(self):
        self.popups = []

    # adds a message to a list
    def add(self, popup):
        if popup in self.popups:
            return
        bisect.insort(self.popups, popup)

    def update(self, speed):
        for popup in self.popups:
            popup.update(speed)
        self.popups = filter(lambda p: p.is_alive, self.popups)


    # clear popup list
    def clear(self):
        self.popups.clear()
        self.popups = []