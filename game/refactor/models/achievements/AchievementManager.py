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
        achievement = self._get_achievement_by_id(_id)
        achievement.is_complete = True

    def reveal_achievement(self, _id):
        achievement = self._get_achievement_by_id(_id)
        achievement.is_hidden = False

    def _get_achievement_by_id(self, _id):
        achievement = self._achievements.get(_id)
        if achievement is None:
            raise KeyError("Unknown achievement {0}".format(_id))
        return achievement

    # LEGACY
    def unlockAchievement(self, _id):
        self.unlock_achievement(_id)