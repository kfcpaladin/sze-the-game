from abc import abstractmethod, abstractproperty
from . import serialisation

class Dependency(serialisation.Visitable):
    @abstractmethod
    def listen(self, listener):
        pass
    
    @abstractmethod
    def unlisten(self, listener):
        pass

    @abstractmethod
    def notify_all(self):
        pass

    @abstractproperty
    def is_satisfied(self):
        pass

    @abstractproperty
    def accept(self, visitor):
        pass