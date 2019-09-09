from util import ObservableProperty
from util import Observer

class ObservableCondition(ObservableProperty, Observer):
    def __init__(self):
        ObservableProperty.__init__(self, False)
    
    @property
    def is_satisfied(self):
        return self._value

