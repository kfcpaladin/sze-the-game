python early:
    class MainCharacter(ADVCharacter):
        def __init__(self, name, kind=None, **properties):
            ADVCharacter.__init__(self, name, kind=kind, **properties)
            self._default = {
                "attributes": {
                    "intellect": 0,
                    "strength": 0,
                },
                "tutorialMessage": {
                    "show": False,
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
            }
            self.setAttributes(self._default["attributes"])

        ## Update character attributes and generate default tutorial
        def setAttributes(self, attributes):
            """
                attributes = {
                    "strength": 0, etc
                }

                Attributes stored in the dictionary will be put into an array, then the
                values will be stored into the object's attributes 
                self.attributes = [strength, etc]
                self.strength = 0, self.intellect = 0, etc etc

            """
            self.attributes = []
            for attribute in attributes:
                setattr(self, attribute, attributes[attribute])
                self.attributes.append(attribute)
            self.setTutorials()
            self.setAttributeIntroMessages()
            self.setAttributeMessages()

        # Set the tutorial messages and status for character
        def setTutorials(self, tutorials={}):
            """
                tutorials = {
                    "strength": {
                        "show": True, 
                        "msgGain": "Tutorial message for gaining",
                        "msgLoss": "Tutorial message for losing",
                    }, etc
                }
                An attribute is fetched from self.attributes, and used to read from
                the tutorials dictionary. 
                If there is an attribute in the tutorial which matches, set that as
                the new tutorial message, otherwise default to an empty tutorial 
                
                Custom tutorial messages are stored in self.tutorials in the same format
                displayed above
            """
            self.tutorials = {}
            for attribute in self.attributes:
                if attribute in tutorials:
                    self.tutorials[attribute] = tutorials[attribute]
                else:
                    self.tutorials[attribute] = self._default["tutorialMessage"]

        ## Set initial message for the loss or gain of an attribute
        def setAttributeIntroMessages(self, msgDict={}):
            """
                msgDict = {
                    "strength": {
                        "msgGain": "A message for gaining strength",
                        "msgLoss": "A message for losing strength",
                    }, etc etc
                }
                This is stored inside self.introMessages with the same syntax as
                msgDict listed above
            """
            self._checkDict(msgDict)
            self.introMessages = {}
            for attribute in self.attributes:
                if attribute in msgDict:
                    self.introMessages[attribute] = msgDict[attribute]
                else:
                    self.introMessages[attribute] = self._default["attributeIntroMessage"]


        ## Set attribute status messages
        def setAttributeMessages(self, msgDict={}):
            """ 
                msgDict = {
                    "strength": [
                        {"min": 10,  "msg": "You are stronger"},
                        {"min": 0,   "msg": "You are average"},
                        {"min": -10, "msg": "You are weaker"}
                    ], etc etc
                }
                When dictionary is passed into function, it autosorts it into
                descending order based on the "min" attribute
                If the attribute value does not exceed any of the values

                self.attributeMessages matches the syntax of msgDict shown above
            """
            self._checkDict(msgDict)
            self.attributeMessages = {}
            for attribute in self.attributes:
                if attribute in msgDict:
                    sortedList = sorted(msgDict[attribute], key=lambda k: k["min"], reverse=True)
                    self.attributeMessages[attribute] = sortedList
                else:
                    self.attributeMessages[attribute] = self._default["attributeMessage"]

        """
            Methods used during the parsing of the renpy scripts
        """

        # Lose n points for a specified attribute
        def loss(self, attribute, amount=1):
            self._checkAttribute(attribute)
            self._changeAttribute(attribute, -amount)
            self.sayIntro(attribute, "msgLoss")
            self.showTutorial(attribute, "msgLoss")
            self.sayStatus(attribute)

        # Gain n points for a specified attribute
        def gain(self, attribute, amount=1):
            self._checkAttribute(attribute)
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
            message = self.tutorials[attribute][msgType]
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
                renpy.say(self, line)
            
