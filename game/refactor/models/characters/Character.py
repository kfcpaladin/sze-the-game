import renpy

class Character(renpy.ADVCharacter):
    def __init__(self, name, icon=None, attributes=[], kind=None, **properties):
        super().__init__(self, name, kind=kind, **properties)
        self.icon = icon
        self.attributes = attributes

    def add_attribute(self, attribute):
        self.attributes.append(attribute)

    