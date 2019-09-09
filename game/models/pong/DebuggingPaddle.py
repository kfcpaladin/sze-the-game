from .Paddle import Paddle
from util.colours import PrimaryColours

class DebuggingPaddle(Paddle):

    def __init__(self, width, height, speed, colour):
        Paddle.__init__(self, width, height, speed, colour)
    
    def on_collision(self, entity):
        if not self.check_collision(entity):
            return

        Paddle.on_collision(self, entity)

        if entity.velocity.x < 0:
            self.colour = PrimaryColours.RED
        elif entity.velocity.x > 0:
            self.colour = PrimaryColours.GREEN

      
       
