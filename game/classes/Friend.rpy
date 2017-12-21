python early:
    class Friend(ADVCharacter):
        def __init__(self, name, kind=None, **properties):
            ADVCharacter.__init__(self, name, kind=kind, **properties)
            self._baseAttributes = {    # these are attributes which must exist
                "friendship": 0,
                "intellect": 0,
                "strength": 0,
                "thirst": 0,
            }
            self.attributes = []
            self.attributeMessages = {}
            self._getIterableAttributes(properties)

            for baseAttribute in self._baseAttributes:
                if not hasattr(self, baseAttribute):
                    setattr(self, baseAttribute, 0)
                    self.attributes.append(baseAttribute)

        """
            Used to add attributes to a character, and set messages
        """
        # Add a dictionary or list of attributes
        def addAttributes(self, attributes):
            if type(attributes) is list:
                attributes = self._getDictFromList(attribute)
            if type(attributes) is not dict:
                raise TypeError("Expected list or dict for attributes, instead got {0}".format(type(attributes)))
            for attribute in attributes:
                if attribute not in self.attributes:
                    self.attributes.append(attribute)
                setattr(self, attribute, attributes[attribute])

        # Set the messages for each attribute
        def setMessages(self, msgDict):
            for attribute in msgDict:
                self._checkAttribute(attribute)
                self.attributeMessages[attribute] = msgDict[attribute]

        """
            Methods used to provide messages based on which attribute was modified
        """
        # Lose or gain friendship
        def loss(self, attribute="friendship", total=1):
            self._checkAttribute(attribute)
            self._changeAttribute(attribute, -total)
            self.sayMessage(attribute, "msgLoss")

        def gain(self, attribute="friendship", total=1):
            self._checkAttribute(attribute)
            self._changeAttribute(attribute, total)
            self.sayMessage(attribute, "msgGain")

        # Functions that return a default message or a customised message
        def sayMessage(self, attribute, msgType):
            self._checkAttribute(attribute)
            if attribute not in self.attributeMessages:
                message = self._defaultAttributeMessage(attribute, msgType)
            else:
                message = self.attributeMessages[attribute][msgType]
            self._say(message)


        """
            Private methods 
        """
        # Default message for an attribute
        def _defaultAttributeMessage(self, attribute, msgType):
            self._checkAttribute(attribute)
            if msgType is "msgLoss":
                phrase = "decreased"
            else:
                phrase = "increased"
            return "{0}'s {1} {2} to {3}".format(self.name, attribute, phrase, getattr(self, attribute))

        # Change an attribute
        def _changeAttribute(self, attribute, delta):
            self._checkAttribute(attribute)
            attributeValue = getattr(self, attribute)
            setattr(self, attribute, attributeValue + delta)

        # Validate if attribute is in the Friend object
        def _checkAttribute(self, attribute):
            if attribute not in self.attributes:
                raise AttributeError("{0} is not a valid attribute".format(attribute))

        # Used for character speech
        def _say(self, message):
            if message is None:
                return
            if type(message) not in [str, basestring, unicode,list]:
                raise TypeError("Expected string or list, instead got {0}".format(type(message)))
            if type(message) in [str, basestring, unicode]:
                message = [message]
            for line in message:
                renpy.say(self, line)

        # Used to get iterable attributes from properties
        def _getIterableAttributes(self, properties):
            for attribute in properties:
                if type(properties[attribute]) in [int, float]:
                    self.attributes.append(attribute)

        # Get a dictionary of default values from a list
        def _getDictFromList(self, array, defaultValue=0):
            dictionary = {}
            for item in array:
                dictionary[item] = defaultValue
            return dictionary


            

            