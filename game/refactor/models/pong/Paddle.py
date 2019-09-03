from .Entity import Entity
from .PongRenderer import Renderable
from .BounceSurface import BounceSurface, left_right_bounce

class Paddle(Entity, BounceSurface):

    def __init__(self, width, height, speed, colour):
        Entity.__init__(self, width, height)
        self.max_speed = speed
        self.colour = colour
    
    # up and down is inverted (origin is top-left)
    def move_up(self):
        self.velocity.y = -self.max_speed.y
        self.velocity.x = 0
    
    def move_down(self):
        self.velocity.y = +self.max_speed.y
        self.velocity.x = 0

    def render(self, renderer):
        return renderer.render_paddle(self)

    def bounce(self, ball):
        return left_right_bounce(self, ball)

            
            

