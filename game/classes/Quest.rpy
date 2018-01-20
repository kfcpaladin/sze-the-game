python early:
    class Quests:
        def __init__(self, questParams):
            self.questParams = questParams
            self._baseParams = {
                "title": None, 
                "brief": None,
                "description": None, 
                "dependencies": None, 
                "label": None,
                "icon": None,
                "conditions": [
                    {
                        "function": None,
                        "msg": None,
                    },
                ],
            }
            # Add in basic parameters
            for baseParam in self._baseParams:
                if baseParam not in self.questParams:
                    self.questParams.append(baseParam)
            # Quest types
            self.questTypes = ["unavailable", "available", "completed"]
            self.displayableQuestTypes = ["available", "completed"]
            self.currentQuestType = self.questTypes[1]  # this is used by the screen by default
            self._stringType = [unicode, str, basestring]
            for questType in self.questTypes:
                setattr(self, questType, {})

        """
            // add a dictionary of quests to either unavailable or available
            // saves to self.unavailable or self.available
            addQuests({
                "questID": {
                    "title": ...,
                    "brief": ...,
                    "description": ...,
                    "dependencies": [],
                }, etc
            })

            // update all unavailable quests to see if they are now available
            updateQuests()


        """
        def addQuests(self, quests):
            if type(quests) is not dict:
                raise TypeError("Expected dict for quests, not {0}".format(type(quests)))
            for questID in quests:
                self._checkQuest(quests[questID])   # Need to validate if correct
                if quests[questID]["dependencies"] is None:
                    self.available[questID] = quests[questID]
                else:
                    self.unavailable[questID] = quests[questID]

        """
            updateQuests will go through all unavailable quests and make them available
            for the user to complete
            It will give a popup to alert the user that a quest is available
        """
        def updateQuests(self):
            questsMadeAvailable = []
            # unlock quest if dependencies and conditions are satisfied
            for questID, quest in self.unavailable.iteritems():
                if self._checkQuestDependencies(quest["dependencies"]):
                    quest = self.unavailable[questID]
                    self.available[questID] = quest
                    questsMadeAvailable.append(questID)
                    popup({
                        "text": "Unlocked quest: {0}".format(questID),
                        "icon": quest["icon"],
                    })
            # Remove the quests that were made available from self.unavailable
            for questID in questsMadeAvailable: 
                self.unavailable.pop(questID)
            if len(questsMadeAvailable) > 0:
                playsfx("xbox.ogg")

        """
            unlockQuest = unlock a quest by id, and give popup
            startQuest = given a quest id, tries to go to a story label
            completeQuest = moves quest, given an id,  from self.available to self.complete, and gives popup
            describe = will print to console, a formatted description of all quests
        """
        def unlockQuest(self, questID):
            self._checkQuestID(questID)
            if questID in self.unavailable:
                quest = self.unavailable[questID]
                self.available[questID] = quest
                self.unavailable.pop(questID)
                playsfx("xbox.ogg")
                popup({
                    "text": "Unlocked quest: {0}".format(questID),
                    "icon": quest["icon"],
                })

        def startQuest(self, questID):
            self._checkQuestID(questID)
            if questID in self.available:
                quest = self.available[questID]
                if self._checkQuestCondition(quest["conditions"]):
                    self._gotoLabel(quest["label"])

        def completeQuest(self, questID):
            self._checkQuestID(questID)
            if questID in self.available:
                quest = self.available[questID]
                self.completed[questID] = quest
                self.available.pop(questID)
                playsfx("xbox.ogg")
                popup({
                    "text": "Completed quest: {0}".format(questID),
                    "icon": quest["icon"],
                })

        def describe(self):
            for questType in self.questTypes:
                print("[{0}]".format(questType))
                self._debugQuestType(questType)
                print("")
            
        """
            _checkQuestID = check if questid is a string
            _checkQuest = fill in missing parameters from base and custom parameter list
            _checkQuestCondition = return true if all conditons are satisfied, otherwise false and gives popup
            _checkQuestDependencies = return true if all dependencies are completed
            _gotoLabel = tries to jump to label, otherwise if it fails, give error popup
            _debugQuestType = gives formatted console output of all quests of a specific type
        """
        def _checkQuestID(self, questID):
            if type(questID) not in self._stringType:
                raise TypeError("Expected questID to be string, not {0}".format(type(questID)))

        def _checkQuest(self, quest):
            if type(quest) is not dict:
                raise TypeError("A quest should be a dict, not a {0}".format(type(quest)))
            for param in self.questParams:
                if param not in quest:
                    quest[param] = self._baseParams[param]
        
        def _getQuestByID(self, questID):
            self._checkQuestID(questID)
            for questType in self.questTypes:
                quests = getattr(self, questType)
                if questID in quests:
                    return quests[questID]
            else:
                raise NameError("{0} is not a valid quest ID".format(questID))

        def _checkQuestCondition(self, conditions):
            if type(conditions) is dict:
                conditions = [conditions]
            elif type(conditions) is not list:
                raise TypeError("Quest conditions must be either a list or dict")
            failMessages = []
            for condition in conditions:
                if condition["function"]:
                    if not callable(condition["function"]):
                        raise TypeError("Expected a function for a condition")
                    if not condition["function"]():
                        failMessages.append(condition["msg"])
            if len(failMessages) > 0:
                playsfx("vpunch.ogg")
                popup(failMessages)
                return False
            else:
                return True

        def _checkQuestDependencies(self, dependencies):
            if not dependencies:
                return True
            if type(dependencies) in self._stringType:
                dependencies = [dependencies]
            for dependency in dependencies:
                if dependency not in self.completed:
                    return False
            return True


        def _gotoLabel(self, label):
            if type(label) in self._stringType:
                closeDiary()
                renpy.jump(label)
                playsfx("vpunch.ogg")
            else:
                playsfx("error.ogg")
                popup("This quest does not go anywhere!")

        def _debugQuestType(self, questType):
            quests = getattr(self, questType)
            for questID in quests:
                print(">>> Quest: {0}".format(questID))
                for param in self.questParams:
                    print("{0}: {1}".format(param, quests[questID][param]))
                print("")
