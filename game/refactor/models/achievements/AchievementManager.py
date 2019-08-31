class AchievementManager(object):
    def __init__(self):
        self._achievements = {} 

    def __iter__(self):
        for achievement in self._achievements.values():
            yield achievement

    @property
    def achievements(self):
        return self._achievements.values()

    def add_achievement(self, achievement):
        _id = achievement.id
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

    # LEGACY
    def unlockAchievement(self, _id):
        self.unlock_achievement(_id)