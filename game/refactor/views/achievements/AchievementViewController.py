class AchievementViewController(object):
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
        self._achievements = self._filter_search(lambda a: a.is_hidden and not a.is_complete) 

    def select_pending(self):
        self._achievements = self._filter_search(lambda a: not a.is_hidden and not a.is_complete) 

    def select_completed(self):
        self._achievements = self._filter_search(lambda a: a.is_complete) 

    def _filter_search(self, key):
        return filter(key, self._manager.achievements)
    