from refactor.util import RenpyCallbacks

class QuestsViewController:
    def __init__(self, manager):
        self._manager = manager
        self._quests = []
        self._quest = None
    
    @property
    def quests(self):
        return self._quests
    
    @property
    def quest(self):
        return self._quest

    def get_quest_colour(self, quest, theme):
        if quest.is_complete:
            return theme.positive
        elif quest.is_unlocked:
            return theme.neutral
        return theme.negative

    def start_quest(self, quest):
        # RenpyCallbacks.get_instance().hide_screen("achieve_screen")
        quest.start()
    
    def select_quest(self, quest):
        self._quest = quest
    
    def select_unlocked(self):
        self._quests = self._filter_search(lambda x: x.is_unlocked and not x.is_complete)
    
    def select_completed(self):
        self._quests = self._filter_search(lambda x: x.is_complete)

    def select_hidden(self):
        self._quests = self._filter_search(lambda x: not x.is_unlocked)

    def _filter_search(self, key):
        return filter(key, self._manager.quests)

        
