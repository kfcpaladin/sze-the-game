from .Entity import Entity
from .PongRenderer import Renderable
from .PersistentEntity import add_persistence

@add_persistence
class Ball(Entity, Renderable):
    def __init__(self, width, height, colour):
        Entity.__init__(self, width, height)
        self.colour = colour

    def render(self, renderer):
        return renderer.render_ball(self)


