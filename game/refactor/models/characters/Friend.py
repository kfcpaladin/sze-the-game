from .Character import Character
from .Attribute import Attribute

class Friend(Character):
    _instances = []

    def __init__(self, name, description=None, friendship=0, **kwargs):
        Character.__init__(self, name, **kwargs)
        self._friendship = Attribute("friendship", friendship)
        self.description = description
        self.add_attribute(self._friendship)
        Friend._instances.append(self)

    @staticmethod
    def get_all():
        return Friend._instances

    @property
    def friendship(self):
        return self._friendship.value
    
    @friendship.setter
    def friendship(self, value):
        self._friendship.value = value
    
    @property
    def friendship_prop(self):
        return self._friendship
