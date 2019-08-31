from renpy.character import ADVCharacter

class Character(ADVCharacter):
    def __init__(self, name, icon=None, **properties):
        ADVCharacter.__init__(self, name, **properties)
        self._icon = icon
    
    @property
    def icon(self):
        return self._icon
    
    