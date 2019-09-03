from abc import abstractmethod
from refactor.util.colours import PrimaryColours

class Surface(object):
    @abstractmethod
    def on_collision(self, entity):
        pass
