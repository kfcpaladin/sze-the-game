import renpy
from .AttributeManager import AttributeManager
from .AttributeNotifications import AttributeNotificationSystem

class Character(renpy.character.ADVCharacter):
    def __init__(self, name, icon=None, kind=None, **properties):
        super().__init__(self, name, kind=kind, **properties)
        self.icon = icon
        # dependency inject this later, when other things need access to attributes
        self._attributes = AttributeManager() 
        self._notifications = AttributeNotificationSystem(self._attributes)

    def add_attribute(self, attribute):
        self._attributes.add(attribute)

    def add_notification(self, notification):
        self._notifications.add(notification)

    # Legacy functions
    # Get attributes like a member field
    def __getattr__(self, key):
        attribute = self.attributes.get(key)
        if attribute:
            return attribute.value
        else:
            return super().__getattr__(self, key)

    def __setattr__(self, key, value):
        attribute = self.attributes.get(key)
        if attribute:
            attribute.value = value
        else:
            super().__setattr__(self, key, value)

    # modify attributes based on name
    def loss(self, name, total=1):
        attribute = self.attributes.get(name)
        attribute.value -= total 
        
    def gain(self, name, total=1):
        attribute = self.attributes.get(name)
        attribute.value += total 
    
    def say(self, message):
        renpy.say(self, message)
    