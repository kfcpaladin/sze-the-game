from .AttributeNotificationSystem import AttributeNotification

class TutorialMessage(Notification):
    def __init__(self, attribute, brief, msg_gain, msg_loss):
        super().__init__(self, attribute)
        self.brief = brief
        self.msg_gain = msg_gain
        self.msg_loss = msg_loss
        self.is_completed = False        
    
    def on_change(self, old, new):
        if self.is_completed:
            return
        
        self.is_completed = True
        self.say(self.brief)
        if new > old:
            self.say(self.msg_gain)
        elif old < new:
            self.say(self.msg_loss)

    def say(self, message):
        if msg is not None:
            renpy.say(adv, message)

