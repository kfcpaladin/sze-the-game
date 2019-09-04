from .Vector2D import Vector2D
from .Rect2D import Rect2D

class Entity(object):
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self.position = Vector2D(0, 0)
        self.velocity = Vector2D(0, 0)

    def update(self, dt):
        self.position += self.velocity * dt

    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height

    @property
    def rect(self):
        return Rect2D(right=self.width, bottom=self.height).add_offset(self.position)

    def check_collision(self, other):
        return self.rect.check_overlap(other.rect) 

        