from .Entity import Entity
from .PongRenderer import Renderable
from .BounceSurface import BounceSurface

from refactor.util.colours import PrimaryColours

class DebuggingPaddle(Entity, BounceSurface, Renderable):

    def __init__(self, width, height, speed):
        Entity.__init__(self, width, height)
        self.max_speed = speed
        self.colour = PrimaryColours.WHITE
    
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
        if not self.check_collision(ball):
            self.colour = PrimaryColours.WHITE
            return False

        # bounce right
        if ball.rect.left > self.rect.left:
            ball.position.x = self.rect.right
            ball.velocity.x = abs(ball.velocity.x)
            self.colour = PrimaryColours.RED
            return True
        elif ball.rect.left < self.rect.left:
            ball.position.x = self.position.x - ball.rect.width
            ball.velocity.x = -abs(ball.velocity.x)
            self.colour = PrimaryColours.GREEN
            return True

        self.colour = PrimaryColours.YELLOW 
        return False 
