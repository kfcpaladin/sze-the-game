from .Character import Character
from .Attribute import Attribute

class Friend(Character):
    def __init__(self, name, friendship=0, **kwargs):
        Character.__init__(self, name, **kwargs)
        self._friendship = Attribute("friendship", friendship)
        self.add_attribute(self._friendship)

    @property
    def friendship(self):
        return self._friendship.value
    
    @friendship.setter
    def friendship(self, value):
        self._friendship.value = value
    
    @property
    def friendship_prop(self):
        return self._friendship
