from abc import abstractmethod

class Visitable:
    @abstractmethod
    def accept(self, visitor):
        pass
