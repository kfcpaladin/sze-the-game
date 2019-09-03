from refactor.util.gametools import Entity, Persistent
from .PongRenderer import Renderable

import random

class Ball(Entity, Persistent, Renderable):
    def __init__(self, width, height, speed, colour):
        Entity.__init__(self, width, height)
        self.speed = speed
        self.colour = colour
        self.store()

    def store(self):
        self._initial_pos = self.position.copy()
        self._initial_vel = self.velocity.copy()

    # when loaded, randomise y velocity
    def load(self):
        self.position = self._initial_pos.copy()
        self.velocity.x = self._initial_vel.x
        self.velocity.y = random.uniform(-self.speed, self.speed)

    def render(self, renderer):
        return renderer.render_ball(self)


