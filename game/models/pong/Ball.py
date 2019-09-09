from util.gametools import Entity, Persistent, Renderable

import random

class Ball(Entity, Persistent, Renderable):
    def __init__(self, width, height, speed, colour):
        Entity.__init__(self, width, height)
        self.speed = speed
        self.colour = colour
        self.store()

    def store(self):
        self._initial_pos = self.position.copy()
        self._initial_vel_x = self.velocity.x
        self.velocity.y = random.uniform(-self.speed, self.speed)

    # when loaded, randomise y velocity
    def load(self):
        self.position = self._initial_pos.copy()
        self.velocity.x = self._initial_vel_x
        self.velocity.y = random.uniform(-self.speed, self.speed)

    def render(self, renderer):
        return renderer.render_ball(self)


