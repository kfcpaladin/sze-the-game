from .Entity import Entity
from .PongRenderer import Renderable
from .BounceSurface import BounceSurface, left_right_bounce
from .PersistentEntity import add_persistence

@add_persistence
class Paddle(Entity, BounceSurface, Renderable):

    def __init__(self, width, height, speed, colour):
        Entity.__init__(self, width, height)
        self.max_speed = speed
        self.colour = colour
    
    # up and down is inverted (origin is top-left)
    def move_up(self):
        self.velocity.y = -self.max_speed
    
    def move_down(self):
        self.velocity.y = +self.max_speed
    
    def stop(self):
        self.velocity.y = 0

    def render(self, renderer):
        return renderer.render_paddle(self)

    def bounce(self, ball):
        return left_right_bounce(self, ball)

            
            

