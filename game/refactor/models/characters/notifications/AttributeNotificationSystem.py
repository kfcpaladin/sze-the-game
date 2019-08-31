from abc import abstractmethod

class AttributeNotificationSystem:
    def __init__(self, attributes):
        self._attributes = attributes 
        self._notifications = []

    def add(self, notification):
        self._notifications.append(notification)
        @self._attributes.listen_change(
            notification.attribute, 
            notification.condition)
        def listener(old, new):
            notification.on_change(old, new)
        
class AttributeNotification:
    message_callback = None

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
        AttributeNotification._static_say(message)

    @staticmethod
    def _static_say(message):
        if AttributeNotification.message_callback is None:
            raise RuntimeError("AttributeNotification needs static callback to narrator method")
        AttributeNotification.message_callback[0](message)



