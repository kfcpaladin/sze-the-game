from util import ObservableProperty

class Achievement(object):
    def __init__(self, _id, title, brief, description, icon=None, hidden=False):
        self.id = _id
        self.title = title 
        self.brief = brief 
        self.description = description 
        self.icon = icon

        self._is_complete = ObservableProperty(False)
        self._is_hidden = ObservableProperty(hidden)

        self._unlock_condition = None
        self._reveal_condition = None

    def set_unlock_condition(self, condition):
        if self._unlock_condition is None:
            condition.observe_prop(self._on_unlock_condition)
            self._unlock_condition = condition

    def _on_unlock_condition(self, condition):
        if condition.is_satisfied:
            self.is_complete = True 
    
    def set_reveal_condition(self, condition):
        if self._reveal_condition is None:
            condition.observe_prop(self._on_reveal_condition)
            self._reveal_condition = condition

    def _on_reveal_condition(self, condition):
        if condition.is_satisfied:
            self.is_hidden = False

    @property
    def is_complete(self):
        return self._is_complete.value
        
    @property
    def is_hidden(self):
        return self._is_hidden.value

    @is_complete.setter
    def is_complete(self, is_complete):
        self._is_complete.value = is_complete
    
    @is_hidden.setter
    def is_hidden(self, is_hidden):
        self._is_hidden.value = is_hidden
    
    @property
    def is_complete_prop(self):
        return self._is_complete
    
    @property
    def is_hidden_prop(self):
        return self._is_hidden
