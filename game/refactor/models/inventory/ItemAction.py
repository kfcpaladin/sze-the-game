from abc import abstractmethod

class ItemAction(object):
    @abstractmethod
    def apply(self, person):
        pass
    
    @abstractmethod
    def undo(self, person):
        pass

    @property
    def description(self):
        pass
