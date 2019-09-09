from util.gametools import Entity, Surface, Persistent

class Wall(Entity, Persistent, Surface):
    def __init__(self, width, height):
        Entity.__init__(self, width, height)
        self.store()
    
    def store(self):
        self._initial_pos = self.position.copy()
        self._initial_velocity = self.velocity.copy()
    
    def load(self):
        self.position = self._initial_pos.copy()
        self.velocity = self._initial_velocity.copy()


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
        
