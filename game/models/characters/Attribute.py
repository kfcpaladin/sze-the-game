from util import ObservableProperty

class Attribute(ObservableProperty):
    def __init__(self, name, value=0):
        ObservableProperty.__init__(self, value)
        self._name = name

    @property
    def name(self):
        return self._name
