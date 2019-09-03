from .Entity import Entity
from .BounceSurface import BounceSurface, left_right_bounce

class Wall(Entity, BounceSurface):
    def bounce(self, ball):
        return left_right_bounce(self, ball)