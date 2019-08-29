from abc import abstractmethod, abstractproperty
from . import Dependency

class BasicDependency(Dependency):
    def __init__(self):
        self._listeners = []

    def listen(self, listener):
        self._listeners.append(listener)
    
    def unlisten(self, listener):
        self._listeners.remove(listener)

    def notify_all(self):
        for listener in self._listeners:
            listener(self)

    @abstractproperty
    def is_satisfied(self):
        pass

        
