python early:
    class Achievements:
        def __init__(self, achieveParams):
            self.achieveParams = achieveParams
            self._baseParams = {
                "title": None, 
                "brief": None,
                "description": None, 
                "dependencies": None, 
                "hidden": False,
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
                if baseParam not in self.achieveParams:
                    self.achieveParams.append(baseParam)
            # Quest types
            self.achieveTypes = ["hidden", "available", "completed"]
            self.displayableAchieveTypes = ["available", "completed"]
            self.currentAchieveType = self.achieveTypes[1]  # this is used by the screen by default
            self._stringType = [unicode, str, basestring]
            for achieveType in self.achieveTypes:
                setattr(self, achieveType, {})

        def addAchievements(self, achievements):
            """
                Accepts a dictionary of achievements and puts it into unavailable or available achievements
                achievements = {
                    "achieveID": {
                        "title": "A title",
                        "brief": "A short message",
                        "description": "A longer message with more description",
                        "dependencies": ["quest1", "quest2", etc],
                    }, etc
                }
            """
            if type(achievements) is not dict:
                raise TypeError("Expected dict for achievements, not {0}".format(type(achievements)))
            for achieveID, achievement in achievements.iteritems():
                self._checkAchieve(achievement)   # Need to validate if correct
                if not achievement["hidden"]:
                    self.available[achieveID] = achievement
                else:
                    self.hidden[achieveID] = achievement

        def updateAchievements(self):
            """
                Will iterate through the dictionary of unavailable achievements, and check
                if they dependencies have been satisified. This occurs when the 
                dependent achievements are in the available section.Then it will add them
                to available achievements
                This method will be called whenever a achievement is completed, and may
                cause some performance drops
            """
            achieveMadeAvailable = []
            achieveUnlockMessages = []
            unlockableTypes = ["hidden", "available"]
            for achieveType in unlockableTypes:
                achievements = getattr(self, achieveType)
                unlockedAchievements = self.checkAchievements(achievements)
                achieveMadeAvailable.extend(unlockedAchievements)
            for achieveID in achieveMadeAvailable:
                achieveUnlockMessages.append("Unlocked achievement: {0}".format(achieveID))
            if len(achieveUnlockMessages) > 0:
                playsfx("xbox.ogg")
                popup(achieveUnlockMessages)

        """
            Unlock an achievement by achievement identification code
        """
        def unlockAchievement(self, achieveID):
            for achieveType in ("hidden", "available"):
                achievements = getattr(self, achieveType)
                if achieveID in achievements:
                    self.completed[achieveID] = achievements[achieveID]
                    achievements.pop(achieveID)
                    playsfx("xbox.ogg")
                    popup("Unlocked achievement: {0}".format(achieveID))

        def checkAchievements(self, achievements):
            achieveMadeAvailable = []
            for achieveID, achievement in achievements.iteritems():
                if(self._checkAchieveDependencies(achievement["dependencies"]) and
                   self._checkAchieveCondition(achievement["conditions"])):
                    self.completed[achieveID] = achievement
                    achieveMadeAvailable.append(achieveID)
                    
            # Remove the achievements that were made available after looping through dict,
            # since removing a achievement during iteration results in an error
            for achieveID in achieveMadeAvailable: 
                achievements.pop(achieveID)
            return achieveMadeAvailable

        def debugAchievements(self):
            """
                Will print to console, the achievements.
                Useful for debugging the state of the game.
            """
            for achieveType in self.achieveTypes:
                print("[{0}]".format(achieveType))
                self._debugAchieveType(achieveType)
                print("")
            


        """
            Private methods
        """
        def _checkAchieveID(self, achieveID):
            if type(achieveID) not in self._stringType:
                raise TypeError("Expected achieveID to be string, not {0}".format(type(achieveID)))

        def _checkAchieve(self, achievement):
            """
                Need to validate if a achievement has been written properly.
                If there are missing parameters, fill them with blank statements
            """
            if type(achievement) is not dict:
                raise TypeError("A achievement should be a dict, not a {0}".format(type(achievement)))
            for param in self.achieveParams:
                if param not in achievement:
                    achievement[param] = self._baseParams[param]
                    
        def _getDependencyString(self, achieveID):
            """
                Used by screens to get the list of dependencies.
                Since the "text" statement cannot process a normal string,
                it needs a specially created string
            """
            self._checkAchieveID(achieveID)
            achievement = self._getAchieveByID(achieveID)
            dependencies = achievement["dependencies"]
            if type(dependencies) in self._stringType:
                dependencies = [dependencies]
            infoString = ""
            if dependencies:
                for achievement in dependencies:
                    infoString += achievement
                    if achievement is not dependencies[-1]:
                        infoString += ", "
            else:
                infoString = "There exists no dependencies"
            return infoString


        
        def _getAchieveByID(self, achieveID):
            """
                Get the achievement object given a achieveID
                Other if there is not achievement that has that ID, throw an
                exception to warn the user
            """
            self._checkAchieveID(achieveID)
            for achieveType in self.achieveTypes:
                achievements = getattr(self, achieveType)
                if achieveID in achievements:
                    return achievements[achieveID]
            else:
                raise NameError("{0} is not a valid achievement ID".format(achieveID))

        def _checkAchieveCondition(self, conditions):
            """
                Check all lists of conditions and sees if they are all verified
                If not return False, otherwise True
            """
            if type(conditions) is dict:
                conditions = [conditions]
            elif type(conditions) is not list:
                raise TypeError("Quest conditions must be either a list or dict")
            for condition in conditions:
                if condition["function"]:
                    if not callable(condition["function"]):
                        raise TypeError("Expected a function for a condition")
                    if not condition["function"]():
                        return False
                # if no unlock function, assume it requires a direct unlock
                else:
                    return False
            return True

        def _checkAchieveDependencies(self, dependencies):
            if not dependencies:
                return True
            if type(dependencies) in self._stringType:
                dependencies = [dependencies]
            for dependency in dependencies:
                if dependency not in self.completed:
                    return False
            return True


        def _debugAchieveType(self, achieveType):
            achievements = getattr(self, achieveType)
            for achieveID, achievement in achievements.iteritems():
                print("[Quest: {0}]".format(achieveID))
                for param in self.achieveParams:
                    print("{0}: {1}".format(param, achievement[param]))
                print("")
