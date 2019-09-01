from renpy.character import ADVCharacter

class Character(ADVCharacter):
    def __init__(self, name, icon=None, **properties):
        ADVCharacter.__init__(self, name, **properties)
        self.icon = icon
        self._attributes = {}
    
    @property
    def attributes(self):
        return self._attributes.values()

    def add_attribute(self, attribute):
        name = attribute.name
        if name in self._attributes:
            raise KeyError("Attribute {0}={1} already exists".format(name, self._attributes[name].value))
        self._attributes.setdefault(name, attribute)

    def get_attribute(self, name):
        attribute = self._attributes.get(name)
        if attribute is None:
            raise KeyError("Attribute {0} doesn't exist".format(name))
        return attribute

    # LEGACY: compatability with existing code 
    def gain(self, name, value=1):
        attribute = self.get_attribute(name)
        attribute.value += value
    
    def loss(self, name, value=1):
        attribute = self.get_attribute(name)
        attribute.value -= value
    
    