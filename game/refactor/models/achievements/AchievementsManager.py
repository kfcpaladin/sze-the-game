# TODO: Use observer interface to automatically move achievement to diff list
# instead of creating a generator each time
class AchievementsManager:
    def __init__(self):
        self._achievements = []

    def add_achievement(self, achievement):
        self._achievements.append(achievement)

    @property 
    def achievements(self):
        return self._achievements

    @property
    def unlocked_achievements(self):
        return (achieve for achieve in self.achievements if achieve.is_unlocked)

    @property
    def completed_achievements(self):
        return (achieve for achieve in self.achievements if achieve.is_completed)