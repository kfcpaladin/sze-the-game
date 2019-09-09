from util.gametools import Entity, Renderable, Vector2D
from abc import abstractmethod

class Gun(Entity, Renderable):
    def __init__(self, width, height):
        Entity.__init__(self, width, height)
        self.fired_bullets = []
    
    def __iter__(self):
        while len(self.fired_bullets) > 0:
            bullet = self.fired_bullets.pop(0)
            yield bullet

    def fire_bullet(self, bullet):
        self.fired_bullets.append(bullet)

    @abstractmethod
    def pull_trigger(self):
        pass

    @abstractmethod 
    def release_trigger(self):
        pass

    @abstractmethod 
    def render(self, renderer):
        pass
