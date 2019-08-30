class AchievementViewController:
    def __init__(self, manager):
        self._manager = manager
        self._achievements = []
        self._achievement = None

    @property
    def achievements(self):
        return self._achievements

    @property
    def achievement(self):
        return self._achievement

    def select_achievement(self, achievement):
        self._achievement = achievement

    def select_hidden(self):
        self._achievements = self._manager.achievements

    def select_pending(self):
        self._achievements = self._manager.pending_achievements 

    def select_available(self):
        self._achievements = self._manager.unlocked_achievements

    def select_completed(self):
        self._achievements = self._manager.completed_achievements


    