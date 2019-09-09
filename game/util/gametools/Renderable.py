from abc import abstractmethod

class Renderable(object):
    @abstractmethod
    def render(self, renderer):
        pass   