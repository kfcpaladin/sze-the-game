from util import ObservableProperty

class Quest(object):
    def __init__(self, id, title, brief, description, icon=None, is_unlocked=False):
        self.id = id
        self.title = title
        self.brief = brief
        self.description = description
        self.icon = icon

        self._is_unlocked = ObservableProperty(is_unlocked)
        self._is_complete = ObservableProperty(False)

        self._unlock_condition = None
        self._complete_condition = None
        self._start_callback = UnimplementedQuestJump()

    def set_unlock_condition(self, condition):
        if self._unlock_condition is None:
            condition.observe_prop(self._on_unlock_condition)
            self._unlock_condition = condition

    def _on_unlock_condition(self, condition):
        if condition.is_satisfied:
            self.is_unlocked = True 
    
    def set_complete_condition(self, condition):
        if self._complete_condition is None:
            condition.observe_prop(self._on_complete_condition)
            self._complete_condition = condition

    def _on_complete_condition(self, condition):
        if condition.is_satisfied:
            self.is_complete = True

    def set_start_callback(self, callback):
        self._start_callback = callback

    def start(self):
        self._start_callback(self)

    @property
    def is_complete(self):
        return self._is_complete.value
    
    @property
    def is_unlocked(self):
        return self._is_unlocked.value
    
    @is_complete.setter
    def is_complete(self, is_complete):
        self._is_complete.value = is_complete

    @is_unlocked.setter
    def is_unlocked(self, is_unlocked):
        self._is_unlocked.value = is_unlocked
    
    @property
    def is_complete_prop(self):
        return self._is_complete

    @property
    def is_unlocked_prop(self):
        return self._is_unlocked


class UnimplementedQuestJump:
    def __call__(self, quest):
        raise Warning("Unimplemented quest jump for quest {0}".format(quest.id))

    