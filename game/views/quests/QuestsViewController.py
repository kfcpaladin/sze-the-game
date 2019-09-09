from util import RenpyCallbacks

class QuestsViewController:
    def __init__(self, manager):
        self._manager = manager
        self._quest = None

        self.select_unlocked()

    @property
    def quests(self):
        return filter(self._filter, self._manager.quests)
    
    @property
    def quest(self):
        return self._quest

    @property
    def current_filter_name(self):
        return self._current_filter_name

    def start_quest(self, quest):
        # RenpyCallbacks.get_instance().hide_screen("achieve_screen")
        quest.start()
    
    def select_quest(self, quest):
        self._quest = quest
    
    def select_unlocked(self):
        self._current_filter_name = "unlocked"
        self._filter = self._filter_unlocked
    
    def select_completed(self):
        self._current_filter_name = "completed"
        self._filter = self._filter_completed

    def select_hidden(self):
        self._current_filter_name = "hidden"
        self._filter = self._filter_hidden
    
    def _filter_unlocked(self, quest):
        return quest.is_unlocked and not quest.is_complete
    
    def _filter_completed(self, quest):
        return quest.is_complete
    
    def _filter_hidden(self, quest):
        return not quest.is_unlocked

    def _filter_search(self, key):
        return filter(key, self._manager.quests)

    def get_quest_colour(self, quest, theme):
        if quest.is_complete:
            return theme.positive
        elif quest.is_unlocked:
            return theme.neutral
        return theme.negative
