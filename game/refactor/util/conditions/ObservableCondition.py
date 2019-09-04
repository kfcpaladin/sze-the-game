from refactor.util import ObservableProperty
from refactor.util import Observer

class ObservableCondition(ObservableProperty, Observer):
    def __init__(self):
        ObservableProperty.__init__(self, False)
    
    @property
    def is_satisfied(self):
        return self._value

