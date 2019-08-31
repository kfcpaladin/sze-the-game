from renpy.character import ADVCharacter
from .AttributeManager import AttributeManager
from .notifications.AttributeNotificationSystem import AttributeNotificationSystem

class Character(ADVCharacter):
    def __init__(self, name, icon=None, kind=None, **properties):
        ADVCharacter.__init__(self, name, kind=kind, **properties)
        self.icon = icon
        # dependency inject this later, when other things need access to attributes
        self._attributes = AttributeManager() 
        self._notifications = AttributeNotificationSystem(self._attributes)

    @property
    def attributes(self):
        return list(self._attributes)

    def get_attribute(self, name):
        return self._attributes.get(name)

    def add_attribute(self, attribute):
        self._attributes.add(attribute)

    def add_notification(self, notification):
        self._notifications.add(notification)


    def __getattr__(self, key):
        try:
            attribute = self._attributes.get(key)
            return attribute.value
        except KeyError:
            raise AttributeError

    # modify attributes based on name
    def loss(self, name, total=1):
        attribute = self._attributes.get(name)
        attribute.value -= total 
        
    def gain(self, name, total=1):
        attribute = self._attributes.get(name)
        attribute.value += total 

    def change(self, name, value):
        attribute = self._attributes.get(name)
        attribute.value = value 
    
    def say(self, message):
        renpy.say(self, message)
    