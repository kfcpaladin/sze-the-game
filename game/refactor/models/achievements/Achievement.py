from refactor.util import ObservableProperty

class Achievement(object):
    def __init__(self, _id, title, brief, description, icon=None, hidden=False):
        self.id = _id
        self.title = title 
        self.brief = brief 
        self.description = description 
        self.icon = icon

        self._is_complete = ObservableProperty(False)
        self._is_hidden = ObservableProperty(hidden)

    @property
    def is_complete(self):
        return self._is_complete.value
    
    @is_complete.setter
    def is_complete(self, is_complete):
        self._is_complete.value = is_complete

    @property
    def is_hidden(self):
        return self._is_hidden.value
    
    @is_hidden.setter
    def is_hidden(self, is_hidden):
        self._is_hidden.value = is_hidden
