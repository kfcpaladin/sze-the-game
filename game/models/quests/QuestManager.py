from .QuestListener import QuestListener
from util import RenpyCallbacks
from models.popups import Popup

class QuestManager(object):
    def __init__(self, popups):
        self._quests = {}
        self._listeners = []
        self._popups = popups
    
    def __iter__(self):
        for quest in self._quests.values():
            yield quest
        
    @property
    def quests(self):
        return self._quests.values()
    
    def add_quest(self, quest):
        _id = quest.id
        self._quests.setdefault(_id, quest)
        listener = QuestListener(quest)
        self._listeners.append(listener)
        listener.listen_complete(self._on_complete)
        listener.listen_unlock(self._on_unlock)
    
    def unlock_quest(self, id):
        quest = self.get_quest(id)
        quest.is_unlocked = True

    def complete_quest(self, id):
        quest = self.get_quest(id)
        quest.is_unlocked = True
        quest.is_complete = True
    
    def get_quest(self, id):
        quest = self._quests.get(id)
        if quest is None:
            raise KeyError("Unknown quest {0}".format(id))
        return quest
    
    def _on_unlock(self, quest):
        self._popups.add(Popup(
            message="Unlocked quest\n{0}".format(quest.id),
            icon=quest.icon
        ))
        RenpyCallbacks.get_instance().play_sfx("xbox.ogg")
    
    def _on_complete(self, quest):
        self._popups.add(Popup(
            message="Completed quest\n{0}".format(quest.id),
            icon=quest.icon
        ))
        RenpyCallbacks.get_instance().play_sfx("xbox.ogg")

    def is_quest_unlocked(self, id):
        quest = self.get_quest(id)
        return quest.is_unlocked

    def is_quest_complete(self, id):
        quest = self.get_quest(id)
        return quest.is_complete