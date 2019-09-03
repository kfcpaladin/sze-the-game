from refactor.util.gametools import Entity, Renderable, Vector2D
from .Bullet import Bullet

class Gun(Entity, Renderable):
    def __init__(self, width, height, bullet_velocity, round_size):
        Entity.__init__(self, width, height)
        self._bullet_velocity = bullet_velocity
        self._round_size = round_size
    
    def fire_bullet(self):
        bullet = Bullet(self._round_size, self._round_size)
        bullet.position = self.position.copy()
        bullet.velocity = Vector2D(-self._bullet_velocity, 0) 

        return bullet
    
    def render(self, renderer):
        return renderer.render_gun(self)
