python early:
    class Quests:
        def __init__(self):
            self.ongoing = []
            self.completed = []
            self._emptyQuest = {
                "title": None,
                "shortMsg": None,
                "longMsg": None,
            }

        def addQuests(self, quests):
            """
                Accepts either a single dictionary similar to self._emptyQuest, or a list
                of dictionaries. 
                The method will then append all quests to ongoing quests.
            """
            if type(quests) not in [dict, list]:
                raise TypeError("Expected dict/list for quest, not {0}".format(type(quests)))
            if type(quests) is dict:
                quests = [quests]
            for quest in quests:
                self.ongoing.append(quest)

        def completeQuest(self, index):
            """
                Will set an ongoing quest as completed, depending on which
                index is provided. This can be done through the frontend
                gui, written in renpy.
            """
            if type(index) is not int:
                raise TypeError("Expected index to be an integer, not {0}".format(type(index)))
            if index >= len(self.ongoing):
                raise IndexError("Quest {0} is not an ongoing quest".format(index))
            quest = self.ongoing[index]
            self.completed.append(quest)
            self.ongoing.pop(index)

        def debugQuests(self):
            """
                Will print to console, the ongoing and completed quests.
                Useful for debugging the state of the game.
            """
            print("[ Ongoing quests ]")
            self._debugQuest(self.ongoing)
            print("[ Completed quests ]")
            self._debugQuest(self.completed)
            
        """
            Private methods
        """
        def _debugQuest(self, list):
            for index, quest in enumerate(list):
                print("Quest: {0}".format(index))
                print("Title: {0}".format(quest["title"]))
                print("Short: {0}".format(quest["shortMsg"]))
                print("Long: {0}".format(quest["longMsg"]))
