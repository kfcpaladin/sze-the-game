from abc import abstractmethod

class Surface(object):
    @abstractmethod
    def on_collision(self, entity):
        pass
