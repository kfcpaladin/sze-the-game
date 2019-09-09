from .AchievementListener import AchievementListener
from models.popups import Popup

class AchievementManager(object):
    def __init__(self, popups):
        self._achievements = {} 
        self._listeners = []
        self._popups = popups

    def __iter__(self):
        for achievement in self._achievements.values():
            yield achievement

    @property
    def achievements(self):
        return self._achievements.values()

    def add_achievement(self, achievement):
        _id = achievement.id
        listener = AchievementListener(achievement)
        self._listeners.append(listener)
        listener.listen_unlock(self._on_unlock)
        listener.listen_reveal(self._on_reveal)
        self._achievements.setdefault(_id, achievement)
    
    def unlock_achievement(self, _id):
        achievement = self.get_achievement(_id)
        achievement.is_complete = True
        achievement.is_hidden = False

    def reveal_achievement(self, _id):
        achievement = self.get_achievement(_id)
        achievement.is_hidden = False
    
    def is_achievement_unlocked(self, _id):
        achievement = self.get_achievement(_id)
        return achievement.is_complete

    def get_achievement(self, _id):
        achievement = self._achievements.get(_id)
        if achievement is None:
            raise KeyError("Unknown achievement {0}".format(_id))
        return achievement

    def _on_reveal(self, achievement):
        pass

    def _on_unlock(self, achievement):
        self._popups.add(Popup(
            message="Unlocked achievement\n{0}".format(achievement.id),
            icon=achievement.icon))