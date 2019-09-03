from .Entity import Entity
from .PongRenderer import Renderable

class Ball(Entity, Renderable):
    def __init__(self, width, height, speed, colour):
        Entity.__init__(self, width, height)
        self.max_speed = speed
        self.colour = colour

    def render(self, renderer):
        return renderer.render_ball(self)


