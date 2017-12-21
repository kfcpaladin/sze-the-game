python early:
    class Quests:
        def __init__(self):
            self.quests = []
            self._emptyQuest = {
                "title": None,
                "shortMsg": None,
                "longMsg": None,
            }

        def addQuests(self, quests):
            if type(quests) not in [dict, list]:
                raise TypeError("Expected dict/list for quest, not {0}".format(type(quests)))
            if type(quests) is dict:
                quests = [quests]
            for quest in quests:
                self.quests.append(quest)

        def removeQuest(self, index):
            if type(index) is not int:
                raise TypeError("Expected index to be an integer, not {0}".format(type(index)))
            if index >= len(self.quests):
                raise IndexError("Quest {0} is not in list of quests".format(quest))
            del self.quests[index]

        def debugQuests(self):
            for index, quest in enumerate(self.quests):
                print("[ Quest {0} ]".format(index))
                print("Title: {0}".format(quest["title"]))
                print("Short: {0}".format(quest["shortMsg"]))
                print("Long: {0}".format(quest["longMsg"]))