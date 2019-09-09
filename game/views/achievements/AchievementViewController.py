class AchievementViewController(object):
    def __init__(self, manager):
        self._manager = manager
        self._achievement = None
        
        self.select_pending()

    @property
    def achievements(self):
        return filter(self._filter, self._manager.achievements)

    @property
    def achievement(self):
        return self._achievement
    
    @property
    def current_filter_name(self):
        return self._current_filter_name

    def select_achievement(self, achievement):
        self._achievement = achievement

    def select_hidden(self):
        self._current_filter_name = "hidden"
        self._filter = self._filter_hidden

    def select_pending(self):
        self._current_filter_name = "pending"
        self._filter = self._filter_pending

    def select_completed(self):
        self._current_filter_name = "completed"
        self._filter = self._filter_completed

    def _filter_hidden(self, achievement):
        return achievement.is_hidden and not achievement.is_complete

    def _filter_pending(self, achievement):
        return not achievement.is_hidden and not achievement.is_complete
    
    def _filter_completed(self, achievement):
        return achievement.is_complete

    def get_achievement_colour(self, achievement, theme):
        if achievement.is_complete:
            return theme.positive
        elif not achievement.is_hidden:
            return theme.neutral
        return theme.negative