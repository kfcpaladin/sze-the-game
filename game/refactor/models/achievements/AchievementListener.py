from refactor.util import Observer

class AchievementListener(Observer):
    def __init__(self, achievement):
        self._achievement = achievement
        self._achievement.is_complete_prop.observe(self.on_unlock)
        self._achievement.is_hidden_prop.observe(self.on_reveal)

        self._unlock_listeners = []
        self._reveal_listeners = []

    def on_unlock(self, _, is_completed):
        if is_completed:
            for listener in self._unlock_listeners:
                listener(self._achievement)
    
    def on_reveal(self, _, is_hidden):
        if not is_hidden:
            for listener in self._reveal_listeners:
                listener(self._achievement)


