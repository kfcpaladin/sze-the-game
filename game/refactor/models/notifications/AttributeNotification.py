from refactor.util import Observer
from abc import abstractmethod

class AttributeNotification(Observer):
    callback = None

    def __init__(self, attribute):
        self._attribute = attribute
    
    @property
    def attribute(self):
        return self._attribute

    def say(self, message):
        if AttributeNotification is not None:
            AttributeNotification.callback(message)
        else:
            raise RuntimeError("Callback for notifications not set")

    