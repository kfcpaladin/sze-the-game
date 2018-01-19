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

        """
            // Accepts a dictionary of achievements and puts it into unavailable or available achievements
            // Saves to self.hidden or self.available
            addAchievement({
                "achieveID": {
                    "title": "A title",
                    "brief": "A short message",
                    "description": "A longer message with more description",
                    "dependencies": ["quest1", "quest2", etc],
                }, etc
            })
        """
        def addAchievements(self, achievements):
            
            if type(achievements) is not dict:
                raise TypeError("Expected dict for achievements, not {0}".format(type(achievements)))
            for achieveID, achievement in achievements.iteritems():
                self._checkAchieve(achievement)   # Need to validate if correct
                if not achievement["hidden"]:
                    self.available[achieveID] = achievement
                else:
                    self.hidden[achieveID] = achievement

        """
            Will iterate through the dictionary of unavailable achievements, and check
            if they dependencies have been satisified. This occurs when the 
            dependent achievements are in the available section.Then it will add them
            to available achievements
            This method will be called whenever a achievement is completed, and may
            cause some performance drops
        """
        def updateAchievements(self):
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
            unlockAchievement = unlock achievement using id code
            checkAchievements = check all achievements and complete if conditions are satisfied
            describe = print formatted list of all achievements
        """
        def unlockAchievement(self, achieveID):
            for achieveType in ("hidden", "available"):
                achievements = getattr(self, achieveType)
                if achieveID in achievements:
                    achievement = achievements[achieveID]
                    self.completed[achieveID] = achievement
                    achievements.pop(achieveID)
                    playsfx("xbox.ogg")
                    popup({
                        "text": "Unlocked achievement\n {0}".format(achieveID),
                        "icon": achievement["icon"],
                    })

        def checkAchievements(self, achievements):
            achieveMadeAvailable = []
            for achieveID, achievement in achievements.iteritems():
                if(self._checkAchieveDependencies(achievement["dependencies"]) and
                   self._checkAchieveCondition(achievement["conditions"])):
                    self.completed[achieveID] = achievement
                    achieveMadeAvailable.append(achieveID)
            # remove unlocked achievements from hidden/available
            for achieveID in achieveMadeAvailable: 
                achievements.pop(achieveID)
            return achieveMadeAvailable

        def describe(self):
            for achieveType in self.achieveTypes:
                print("[{0}]".format(achieveType))
                self._debugAchieveType(achieveType)
                print("")
            
        """
            _checkAchieveID = checks if id is a string
            _checkAchieve = fills in missing base and custom parameters
            _getAchieveByID = get reference to achievement dict using id
            _checkAchieveCondition = returns true if all conditions are true, otherwise false
            _checkAchieveDependencies = returns true if all dependencies are satisfied, otherwise false
            _debugAchieveType = prints to console all achievements of a specific type
        """
        def _checkAchieveID(self, achieveID):
            if type(achieveID) not in self._stringType:
                raise TypeError("Expected achieveID to be string, not {0}".format(type(achieveID)))

        def _checkAchieve(self, achievement):
            if type(achievement) is not dict:
                raise TypeError("A achievement should be a dict, not a {0}".format(type(achievement)))
            for param in self.achieveParams:
                if param not in achievement:
                    achievement[param] = self._baseParams[param]

        def _getAchieveByID(self, achieveID):
            self._checkAchieveID(achieveID)
            for achieveType in self.achieveTypes:
                achievements = getattr(self, achieveType)
                if achieveID in achievements:
                    return achievements[achieveID]
            else:
                raise NameError("{0} is not a valid achievement ID".format(achieveID))

        def _checkAchieveCondition(self, conditions):
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
