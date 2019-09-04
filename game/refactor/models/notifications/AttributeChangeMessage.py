from .AttributeNotification import AttributeNotification

class AttributeChangeMessage(AttributeNotification):
    def __init__(self, msg_gain, msg_loss):
        self.msg_gain = msg_gain
        self.msg_loss = msg_loss
    
    def on_change(self, old, new):
        if new > old:
            self.say(self.msg_gain)
        else:
            self.say(self.msg_loss)
    
    

