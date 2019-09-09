from .AttributeNotification import AttributeNotification

class AttributeValueMessage(AttributeNotification):
    def __init__(self, messages):
        self._messages = messages
    
    def on_change(self, old, new):
        message = self._messages.get_entry(new)
        self.say(message)
    