from refactor.util import Vector2D, Rect2D
from .Persistent import Persistent

class Entity(Persistent):
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

    def store(self):
        self._initial_pos = self.position.copy()
        self._initial_vel = self.velocity.copy()
    
    def load(self):
        self.position = self._initial_pos.copy()
        self.velocity = self._initial_vel.copy()

    def check_collision(self, other):
        return self.rect.check_overlap(other.rect) 

        