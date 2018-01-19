python early:
    class MainCharacter(ADVCharacter):
        """
            self.attributes = all attributes
            self.tutorials = all tutorial messages
            self.introMessages = all intro messages for attributes
            self.attributeMessages = all jokes for attributes
            self.statMessages = all messages for statscreen
        """
        def __init__(self, name, kind=None, **properties):
            ADVCharacter.__init__(self, name, kind=kind, **properties)
            self._default = {
                "attributes": {
                    "intellect": 0,
                    "strength": 0,
                },
                "tutorialMessage": {
                    "show": False,
                    "brief": None,
                    "msgGain": None,
                    "msgLoss": None,
                },
                "attributeIntroMessage": {
                    "msgGain": None,
                    "msgLoss": None,
                },
                "attributeMessage": [
                    {"min": 0, "msg": None},
                ],
                "statMessage": [
                    {"min": 0, "msg": None},
                ]
            }
            self.setAttributes(self._default["attributes"])

        
        """
            setAttributes will initiliase character with a set of attributes, which
            can have messages programmed accordingly for them
            setAttributes({
                "strength": 0,
                "penisLength": -2, etc
            })

        """
        def setAttributes(self, attributes):
            
            self.attributes = []
            for attribute, value in attributes.iteritems():
                setattr(self, attribute, value)
                self.attributes.append(attribute)
            self.setTutorials()
            self.setAttributeIntroMessages()
            self.setAttributeMessages()
            self.setStatMessages()

        """
            // plays when attribute is initially changed, and then disabled
            // saves to self.tutorials
            setTutorials({
                "strength": {
                    "show": True,
                    "brief": ...,
                    "msgGain": ...,
                    "msgLoss": ...,
                }, etc
            })

            // message given when lose() or gain() an attribute
            // saves to self.introMessages
            setAttributeIntroMessages({
                "strength": {
                    "msgGain": "A message for gaining strength",
                    "msgLoss": "A message for losing strength",
                }, etc 
            })

            // status message for current attribute value
            // saves to self.attributeMessages
            setAttributeMessages({
                "strength": [
                    {"min": 10,  "msg": "You are stronger"},
                    {"min": 0,   "msg": "You are average"},
                    {"min": -10, "msg": "You are weaker"}
                ], etc
            })

            // messages for stat screen
            // saves to self.statMessages
            setStatMessage({
                "strength": [
                    {"min": 10,  "msg": "You are stronger"},
                    {"min": 0,   "msg": "You are average"},
                    {"min": -10, "msg": "You are weaker"}
                ], etc
            })
        """
        # Set the tutorial messages and status for character
        def setTutorials(self, tutorials={}):
            self.tutorials = {}
            for attribute in self.attributes:
                # if valid attribute in tutorials, add to list of tutorial messages
                if attribute in tutorials:
                    self.tutorials[attribute] = tutorials[attribute]
                    # fill in any missing components using the default tutorial message
                    for key, defaultMessage in self._default["tutorialMessage"].iteritems():
                        if key not in tutorials[attribute]:
                            self.tutorials[attribute][key] = defaultMessage
                # otherwise, add the default message
                else:
                    self.tutorials[attribute] = self._default["tutorialMessage"]

        # Set initial message for the loss or gain of an attribute
        def setAttributeIntroMessages(self, msgDict={}):
            self._checkDict(msgDict)
            self.introMessages = {}
            for attribute in self.attributes:
                if attribute in msgDict:
                    self.introMessages[attribute] = msgDict[attribute]
                else:
                    self.introMessages[attribute] = self._default["attributeIntroMessage"]


        # Set attribute status messages
        def setAttributeMessages(self, msgDict={}):
            self._checkDict(msgDict)
            self.attributeMessages = {}
            for attribute in self.attributes:
                if attribute in msgDict:
                    sortedList = sorted(msgDict[attribute], key=lambda k: k["min"], reverse=True)
                    self.attributeMessages[attribute] = sortedList
                else:
                    self.attributeMessages[attribute] = self._default["attributeMessage"]

        # Set attribute messages for statscreen
        def setStatMessages(self, msgDict={}):
            self._checkDict(msgDict)
            self.statMessages = {}
            for attribute in self.attributes:
                if attribute in msgDict:
                    sortedList = sorted(msgDict[attribute], key=lambda k: k["min"], reverse=True)
                    self.statMessages[attribute] = sortedList
                else:
                    self.statMessages[attribute] = self._default["statMessage"]

        """
            Methods used during the parsing of the renpy scripts
            loss = decrease attribute and give the appropriate message
            gain = increase attribute and give the appropriate message
            _changeAttribute = directly sets the attribute (Should not be used by writers)
        """
        # Lose n points for a specified attribute
        def loss(self, attribute, amount=1):
            self._changeAttribute(attribute, -amount)
            self.sayIntro(attribute, "msgLoss")
            self.showTutorial(attribute, "msgLoss")
            self.sayStatus(attribute)

        # Gain n points for a specified attribute
        def gain(self, attribute, amount=1):
            self._changeAttribute(attribute, amount)
            self.sayIntro(attribute, "msgGain")
            self.showTutorial(attribute, "msgGain")
            self.sayStatus(attribute)

        def _changeAttribute(self, attribute, amount):
            self._checkAttribute(attribute)
            attributeValue = getattr(self, attribute)
            setattr(self, attribute, attributeValue + amount)

        """
            Methods used by loss/gain functions
            showTutorial = will deactivate tutorial message when called, and call sayTutorialMessage
            sayTutorialMessage = will say the message
            sayIntro = Gives intro to losing or gaining an attribute
            sayStatus = Gives the joke for an attribute
            getStatMessage = Gets the appropriate joke for statscreen
        """
        # Show a tutorial if true, then toggle off
        def showTutorial(self, attribute, msgType="msgLoss"):
            self._checkAttribute(attribute)
            if self.tutorials[attribute]["show"] is True:
                self.sayTutorialMessage(attribute, msgType=msgType)
                self.tutorials[attribute]["show"] = False
        
        # Always says the tutorial message when called
        def sayTutorialMessage(self, attribute, msgType="msgLoss"):
            self._checkAttribute(attribute)
            message = ""
            if self.tutorials[attribute]["brief"]:
                message += self.tutorials[attribute]["brief"]
            message += self.tutorials[attribute][msgType]
            self._say(message)

        # For an attribute, display the intro message
        def sayIntro(self, attribute, msgType="msgLoss"):
            self._checkAttribute(attribute)
            message = self.introMessages[attribute][msgType]
            self._say(message)

        # For an attribute, display the status message    
        def sayStatus(self, attribute):
            self._checkAttribute(attribute)
            msgList = self.attributeMessages[attribute]
            attributeValue = getattr(self, attribute)
            message = None
            for msgEntry in msgList:
                if attributeValue >= msgEntry["min"]:
                    message = msgEntry["msg"]
                    break
            else:
                message = msgList[-1]["msg"]
            self._say(message)

        # For an attribute, display the status message    
        def getStatMessage(self, attribute):
            self._checkAttribute(attribute)
            msgList = self.statMessages[attribute]
            attributeValue = getattr(self, attribute)
            message = None
            for msgEntry in msgList:
                if attributeValue >= msgEntry["min"]:
                    message = msgEntry["msg"]
                    break
            else:
                message = msgList[-1]["msg"]
            if message is None:
                message = "You have a {0} of {1}".format(attribute, attributeValue)
            return message

        # Get tutorial message
        def getTutorialMessage(self, attribute, msgType="brief"):
            self._checkAttribute(attribute)
            message = self.tutorials[attribute][msgType]
            if message is None:
                message = "No tutorial"
            return message

        
        """
            Validation functions used to check if parameters are correct
            _checkAttribute = checks if attribute is part of base attributes
            _checkDict = checks if a msgDict is a dictionary of something else
            _say = wraps message into a list before calling each one sequentially
        """

        # validate attribute is valid
        def _checkAttribute(self, attribute):  
            if attribute not in self.attributes:
                raise AttributeError("{0} is not a valid attribute".format(attribute))

        # used to sanitise dictionary parameters
        def _checkDict(self, potentialDict):
            actualType = type(potentialDict)
            if actualType is not dict:
                raise TypeError("Expected a dict, instead got {0}".format(actualType))

        # says dialog for the character
        def _say(self, message):
            if message is None:
                return
            if type(message) not in [str, basestring, unicode,list]:
                raise TypeError("Expected string or list, instead got {0}".format(type(message)))
            if type(message) in [str, basestring, unicode]:
                message = [message]
            for line in message:
                renpy.say(adv, line)
            
