from .Character import Character
from refactor.util import ObservableProperty

class Friend(Character):
    def __init__(self, name, friendship=0, **kwargs):
        Character.__init__(self, name, **kwargs)
        self._friendship = ObservableProperty(friendship)

    @property
    def friendship(self):
        return self._friendship.value
    
    @friendship.setter
    def friendship(self, value):
        self._friendship.value = value
    
    @property
    def friendship_prop(self):
        return self._friendship
