from refactor.util import Observer
from abc import abstractmethod

class AttributeNotification(Observer):
    narrator = None

    def say(self, message):
        if AttributeNotification.narrator is not None:
            AttributeNotification.narrator.say(message)
        else:
            raise RuntimeError("Callback for notifications not set")

    