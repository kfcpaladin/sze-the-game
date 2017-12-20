python early:
    class Friend(ADVCharacter):
        def __init__(self, name, kind=None, **properties):
            ADVCharacter.__init__(self, name, kind=kind, **properties)
            if not hasattr(self, "friendship"):
                setattr(self, "friendship", 0)
            self.msgLoss = None
            self.msgGain = None

        # Functions that return a default message or a customised message
        def lossMessage(self):
            if self.msgLoss is not None:
                return self.msgLoss
            else:
                return "Decreased friendship of {0} to {1}".format(self.name, self.friendship)
        def gainMessage(self): 
            if self.msgGain is not None:
                return self.msgGain
            else:
                return "Increased friendship of {0} to {1}".format(self.name, self.friendship) 

        # Set the strings
        def setOptions(self, options):
            for option in ["msgLoss", "msgGain"]:
                if option in options:
                    setattr(self, option, options[option])

        # Lose or gain friendship
        def loss(self, total=1):
            self.friendship -= total;
            self.sayMessage(self.lossMessage())

        def gain(self, total=1):
            self.friendship += total;
            self.sayMessage(self.gainMessage())

        def sayMessage(self, message):
            message = str(message)
            renpy.say(self, message)
            

            