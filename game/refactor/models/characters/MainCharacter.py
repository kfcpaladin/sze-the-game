from .Character import Character
from refactor.util import ObservableProperty

class MainCharacter(Character):
    def __init__(self, name, icon=None, **kwargs):
        Character.__init__(self, name, icon, **kwargs)
        self._thirst    = ObservableProperty(0)
        self._fort      = ObservableProperty(0)
        self._charm     = ObservableProperty(0)
        self._strength  = ObservableProperty(0)
        self._intellect = ObservableProperty(0)
    
    @property
    def thirst(self):
        return self._thirst.value

    @property
    def fort(self):
        return self._fort.value

    @property
    def charm(self):
        return self._charm.value

    @property
    def strength(self):
        return self._strength.value

    @property
    def intellect(self):
        return self._intellect.value

    @thirst.setter
    def thirst(self, value):
        self._thirst.value = value

    @fort.setter
    def fort(self, value):
        self._fort.value = value

    @charm.setter
    def charm(self, value):
        self._charm.value = value
    
    @strength.setter
    def strength(self, value):
        self._strength.value = value
    
    @intellect.setter
    def intellect(self, value):
        self._strength.value = value

    @property
    def thirst_prop(self):
        return self._thirst
        
    @property
    def fort_prop(self):
        return self._fort

    @property
    def charm_prop(self):
        return self._charm

    @property
    def strength_prop(self):
        return self._strength

    @property
    def intellect_prop(self):
        return self._intellect