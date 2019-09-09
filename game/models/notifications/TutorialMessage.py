from .AttributeNotification import AttributeNotification

class TutorialMessage(AttributeNotification):
    def __init__(self, brief, msg_gain, msg_loss, show=True):
        self.brief = brief
        self.msg_gain = msg_gain
        self.msg_loss = msg_loss
        self.is_completed = not show 
    
    def on_change(self, old, new):
        if self.is_completed:
            return
        
        self.is_completed = True
        self.say(self.brief)
        if new > old:
            self.say(self.msg_gain)
        elif old < new:
            self.say(self.msg_loss)

