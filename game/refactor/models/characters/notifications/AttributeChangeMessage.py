from .AttributeNotificationSystem import AttributeNotification

class AttributeChangeMessage(Notification):
    def __init__(self, attribute, msg_gain, msg_loss):
        super().__init__(self, attribute)
        self.msg_gain = msg_gain
        self.msg_loss = msg_loss
    
    def add_value_notification(self, notification):
        self._value_notifications.append(notifications)

    def on_change(self, old, new):
        if new > old:
            self.say(self.msg_gain)
        else:
            self.say(self.msg_loss)
    
    

