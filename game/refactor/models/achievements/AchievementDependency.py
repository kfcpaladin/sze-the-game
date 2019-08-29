from . import Dependency
from abc import abstractproperty

class AchievementDependency(Dependency):
    def __init__(self, achievement):
        self._achievement = achievement

    @property
    def id(self):
        return self._achievement.id

    def listen(self, listener):
        self._achievement.listen_update(listener)
    
    def unlisten(self, listener):
        pass

    def notify_all(self):
        self._achievement.notify_all()

    @abstractproperty
    def is_satisfied(self):
        return self._achievement.is_completed

    def accept(self, visitor):
        return visitor.visit("achievement_dependency", self)