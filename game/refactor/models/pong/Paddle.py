from .PongRenderer import Renderable
from .Wall import Wall
from .Ball import Ball

import math

class Paddle(Wall, Renderable):

    def __init__(self, width, height, speed, colour):
        Wall.__init__(self, width, height)
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

    def on_collision(self, entity):
        if not isinstance(entity, Ball):
            return

        if not self.check_collision(entity):
            return       
        
        # bounce right
        if entity.velocity.x < 0:
            entity.velocity.x = abs(entity.velocity.x)
            entity.position.x = self.rect.right
        # bounce left
        elif entity.velocity.x > 0:
            entity.velocity.x = -abs(entity.velocity.x)
            entity.position.x = self.rect.left - entity.width  

        # calculate bounce angle
        offset = entity.rect.centre.y - self.rect.centre.y
        angle = 0.25 * math.pi * (2*offset - 1)
        entity.velocity.y = entity.speed * math.sin(angle)
