from .PongRenderer import Renderable
from .Paddle import Paddle
from refactor.util.colours import PrimaryColours

class DebuggingPaddle(Paddle):

    def __init__(self, width, height, speed, colour):
        Paddle.__init__(self, width, height, speed, colour)
    
    def bounce(self, entity):
        if not self.check_collision(entity):
            return

        # bounce right
        if entity.velocity.x < 0:
            entity.velocity.x = abs(entity.velocity.x)
            entity.position.x = self.rect.right
            self.colour = PrimaryColours.RED

        # bounce left
        elif entity.velocity.x > 0:
            entity.velocity.x = -abs(entity.velocity.x)
            entity.position.x = self.rect.left - entity.width  
            self.colour = PrimaryColours.GREEN
