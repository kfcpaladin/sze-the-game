from abc import abstractmethod

class Persistent(object):
    @abstractmethod
    def store(self):
        pass
    
    @abstractmethod
    def load(self):
        pass


    