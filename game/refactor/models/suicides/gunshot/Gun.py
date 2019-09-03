from refactor.util.gametools import Entity, Renderable, Vector2D
from abc import abstractmethod

class Gun(Entity, Renderable):
    def __init__(self, width, height):
        Entity.__init__(self, width, height)

    @abstractmethod
    def pull_trigger(self):
        return
        yield

    @abstractmethod 
    def release_trigger(self):
        return
        yield

    @abstractmethod 
    def render(self, renderer):
        pass
