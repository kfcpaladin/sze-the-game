python early:
    class Quests:
        def __init__(self, questParams):
            self.questParams = questParams
            self._baseParams = ["title", "brief", "description", "dependencies", "label"]
            for baseParam in self._baseParams:
                if baseParam not in self.questParams:
                    self.questParams.append(baseParam)
            self.questTypes = ["unavailable", "available", "completed"]
            self.displayableQuestTypes = ["available", "completed"]
            self.currentQuestType = self.questTypes[1]  # this is used by the screen by default
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
            questUnlockMessages = []
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
                    questUnlockMessages.append("Unlocked quest: {0}".format(questID))
            # Remove the quests that were made available after looping through dict,
            # since removing a quest during iteration results in an error
            for questID in questsMadeAvailable: 
                self.unavailable.pop(questID)
            popup(questUnlockMessages)

        def unlockQuest(self, questID):
            """
                If a quest is unavailable due to a lock, allow
                for a direct unlock given a questID
            """
            self._checkQuestID(questID)
            if questID in self.unavailable:
                self.available[questID] = self.unavailable[questID]
                self.unavailable.pop(questID)
                popup("Unlocked quest: {0}".format(questID))

        def startQuest(self, questID):
            """
                If a quest is ongoing, and a user wants to start it, make a call to
                the appropriate label
            """
            self._checkQuestID(questID)
            if questID in self.available:
                label = self.available[questID]["label"]
                if type(label) in self._stringType:
                    renpy.hide_screen("questscreen")
                    renpy.call(label)
                else:
                    playsfx("vpunch.ogg")

        def completeQuest(self, questID):
            """
                Will set an available quest as completed, depending on which
                questID is provided. This can be done through the frontend
                gui, written in renpy.
            """
            self._checkQuestID(questID)
            if questID in self.available:
                self.completed[questID] = self.available[questID]
                self.available.pop(questID)
                self.updateQuests()

        def debugQuests(self):
            """
                Will print to console, the quests.
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
