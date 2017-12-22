python early:
    class Quests:
        def __init__(self, questParams):
            self.questParams = questParams
            self.questTypes = ["unavailable", "available", "ongoing", "completed"]
            self.currentQuestType = self.questTypes[2]  # this is used by the screen
            self._stringType = [unicode, str, basestring]
            for questType in self.questTypes:
                setattr(self, questType, {})

        def addQuests(self, quests):
            """
                Accepts a dictionary of quests and puts it into unavailable or available quests
                quests = {
                    "questID": {
                        "title": "A title",
                        "brief": "A short message",
                        "description": "A longer message with more description",
                        "dependencies": ["quest1", "quest2", etc],
                    }, etc
                }
            """
            if type(quests) is not dict:
                raise TypeError("Expected dict for quests, not {0}".format(type(quests)))
            for questID in quests:
                self._checkQuest(quests[questID])   # Need to validate if correct
                if quests[questID]["dependencies"] is None:
                    self.available[questID] = quests[questID]
                else:
                    self.unavailable[questID] = quests[questID]

        def updateQuests(self):
            """
                Will iterate through the dictionary of unavailable quests, and check
                if they dependencies have been satisified. This occurs when the 
                dependent quests are in the available section.
                This method will be called whenever a quest is completed, and may
                cause some performance drops
            """
            questsMadeAvailable = []
            for questID in self.unavailable:
                dependencies = self.unavailable[questID]["dependencies"]
                if type(dependencies) in self._stringType:
                    dependencies = [dependencies]
                for quest in dependencies:
                    if quest not in self.completed:
                        break
                else:
                    self.available[questID] = self.unavailable[questID]
                    questsMadeAvailable.append(questID)
            # Remove the quests that were made available after looping through dict,
            # since removing a quest during iteration results in an error
            for questID in questsMadeAvailable: 
                self.unavailable.pop(questID)


        def acceptQuest(self, questID):
            """
                If a quest is available, it will accept it and push into ongoing quests
            """
            self._checkQuestID(questID)
            if questID in self.available:
                self.ongoing[questID] = self.available[questID]
                self.available.pop(questID)

        def cancelQuest(self, questID):
            """
                If a quest is ongoing, but a user wants to cancel it, they can
                push it back into the available category
            """
            self._checkQuestID(questID)
            if questID in self.ongoing:
                self.available[questID] = self.ongoing[questID]
                self.ongoing.pop(questID)

        def completeQuest(self, questID):
            """
                Will set an ongoing quest as completed, depending on which
                questID is provided. This can be done through the frontend
                gui, written in renpy.
            """
            self._checkQuestID(questID)
            if questID in self.ongoing:
                self.completed[questID] = self.ongoing[questID]
                self.ongoing.pop(questID)
                self.updateQuests()

        def debugQuests(self):
            """
                Will print to console, the ongoing and completed quests.
                Useful for debugging the state of the game.
            """
            for questType in self.questTypes:
                print("[{0}]".format(questType))
                self._debugQuestType(questType)
                print("")
            


        """
            Private methods
        """
        def _checkQuestID(self, questID):
            if type(questID) not in self._stringType:
                raise TypeError("Expected questID to be string, not {0}".format(type(questID)))

        def _checkQuest(self, quest):
            """
                Need to validate if a quest has been written properly.
                If there are missing parameters, fill them with blank statements
            """
            if type(quest) is not dict:
                raise TypeError("A quest should be a dict, not a {0}".format(type(quest)))
            for param in self.questParams:
                if param not in quest:
                    quest[param] = None
                    
        def _getDependencyString(self, questID):
            """
                Used by screens to get the list of dependencies.
                Since the "text" statement cannot process a normal string,
                it needs a specially created string
            """
            self._checkQuestID(questID)
            quest = self._getQuestByID(questID)
            dependencies = quest["dependencies"]
            if type(dependencies) in self._stringType:
                dependencies = [dependencies]
            infoString = ""
            if dependencies:
                for quest in dependencies:
                    infoString += quest
                    if quest is not dependencies[-1]:
                        infoString += ", "
            else:
                infoString = "There exists no dependencies"
            return infoString


        
        def _getQuestByID(self, questID):
            """
                Get the quest object given a questID
                Other if there is not quest that has that ID, throw an
                exception to warn the user
            """
            self._checkQuestID(questID)
            for questType in self.questTypes:
                quests = getattr(self, questType)
                if questID in quests:
                    return quests[questID]
            else:
                raise NameError("{0} is not a valid quest ID".format(questID))


        def _debugQuestType(self, questType):
            quests = getattr(self, questType)
            for questID in quests:
                print("[Quest: {0}]".format(questID))
                for param in self.questParams:
                    print("{0}: {1}".format(param, quests[questID][param]))
                print("")
