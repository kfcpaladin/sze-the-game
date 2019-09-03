from .Entity import Entity
from .BounceSurface import BounceSurface, left_right_bounce
from .PersistentEntity import add_persistence

@add_persistence
class Wall(Entity, BounceSurface):
    def __init__(self, width, height):
        Entity.__init__(self, width, height)

    def bounce(self, ball):
        return left_right_bounce(self, ball)