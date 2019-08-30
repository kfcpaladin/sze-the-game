from .AttributeNotificationSystem import Notification
from refactor.characters.PriorityAttributeMessage import PriorityAttributeMessage

class PriorityAttributeMessageNotification(Notification):
    def __init__(self, attribute, priority_message: PriorityAttributeMessage):
        super().__init__(self, attribute)
        self._message = priority_message

    def on_change(self, old, new):
        message = self._message.get_message(new)
        if message is not None:
            self.say(message)