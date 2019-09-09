from util import Observer
from util import RenpyCallbacks
from abc import abstractmethod

class AttributeNotification(Observer):
    def say(self, message):
        if message is not None:
            RenpyCallbacks.get_instance().say(message)
     