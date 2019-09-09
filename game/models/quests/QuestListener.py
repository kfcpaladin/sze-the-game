from util import Observer

class QuestListener(Observer):
    def __init__(self, quest):
        self._quest = quest
        self._quest.is_complete_prop.observe(self.on_complete)
        self._quest.is_unlocked_prop.observe(self.on_unlock)

        self._unlock_listeners = []
        self._complete_listeners = []

    def listen_unlock(self, listener):
        self._unlock_listeners.append(listener)
    
    def listen_complete(self, listener):
        self._complete_listeners.append(listener)

    def on_unlock(self, _, is_unlocked):
        if is_unlocked:
            for listener in self._unlock_listeners:
                listener(self._quest)
    
    def on_complete(self, _, is_completed):
        if not is_completed:
            for listener in self._complete_listeners:
                listener(self._quest)