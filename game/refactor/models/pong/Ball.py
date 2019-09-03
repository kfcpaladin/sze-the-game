from .Entity import Entity
from .PongRenderer import Renderable

import random

class Ball(Entity, Renderable):
    def __init__(self, width, height, speed, colour):
        Entity.__init__(self, width, height)
        self.speed = speed
        self.colour = colour

    # when loaded, randomise y velocity
    def load(self):
        Entity.load(self)
        self.velocity.y = random.uniform(-self.speed, self.speed)

    def render(self, renderer):
        return renderer.render_ball(self)


