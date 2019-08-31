from .AttributeNotification import AttributeNotification
from .PriorityList import PriorityList

class AttributeValueMessage(AttributeNotification):
    def __init__(self, attribute, messages: PriorityList):
        AttributeNotification.__init__(self, attribute)
        self._messages = messages
    
    def on_change(self, old, new):
        message = self._messages.get_entry(new)
        self.say(message)
    