import renpy
from abc import abstractmethod

class AttributeNotificationSystem:
    def __init__(self, attributes):
        self._attributes = attributes 

    def add(self, notification):
        self._notifications.append(notification)
        @self._attributes.listen_attribute_change(
            notification.attribute, 
            notification.condition)
        def listener(old, new):
            notification.on_change(old, new)
        
class AttributeNotification:
    def __init__(self, attribute):
        self._attribute = attribute
    
    @property
    def attribute(self):
        return self._attribute

    @abstractmethod
    def on_change(self, old, new):
        pass
    
    def condition(self, old, new):
        return True

    def say(self, message):
        if msg is not None:
            renpy.say(adv, message)



