python early:
    class Quests:
        def __init__(self):
            self.quests = []
            self.questDetail = {
                "title": None,
                "shortDescription": None,
                "longDescription": None,
            }

        def addQuest(self, quest):
            if type(quest) not dict:
                raise TypeError("Expected dict for quest, not {0}".format(type(quest)))
            self.quests.append(quest)

        def removeQuest(self, quest):
            if quest not in self.quests:
                raise ValueError("{0} is not in list of quests".format(quest))
            self.quests.remove(quest)
