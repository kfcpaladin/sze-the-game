from abc import abstractmethod

class Controls(object):
    @abstractmethod
    def update(self):
        pass