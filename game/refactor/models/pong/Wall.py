from .Entity import Entity
from .Surface import Surface

class Wall(Entity, Surface):
    def __init__(self, width, height):
        Entity.__init__(self, width, height)

    def on_collision(self, entity):
        if not self.check_collision(entity):
            return

        # bounce down 
        if entity.velocity.y < 0:
            entity.velocity.y = abs(entity.velocity.y)
            entity.position.y = self.rect.bottom
        # bounce up
        elif entity.velocity.y > 0:
            entity.velocity.y = -abs(entity.velocity.y)
            entity.position.y = self.rect.top - entity.height
        
        # # bounce right
        # if entity.velocity.x < 0:
        #     entity.velocity.x = abs(entity.velocity.x)
        #     entity.position.x = self.rect.right
        # # bounce left
        # elif entity.velocity.x > 0:
        #     entity.velocity.x = -abs(entity.velocity.x)
        #     entity.position.x = self.rect.left - entity.width  
        
