from refactor.util import Observer
from refactor.util import RenpyCallbacks
from abc import abstractmethod

class AttributeNotification(Observer):
    def say(self, message):
        RenpyCallbacks.get_instance().say(message)
     