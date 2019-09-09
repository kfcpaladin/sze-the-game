from util.gametools import Vector2D
from util import RenpyCallbacks
from .Bullet import Bullet
from .Gun import Gun

class Pistol(Gun):
    def __init__(self, width, height, bullet_velocity, round_size):
        Gun.__init__(self, width, height)
        self._bullet_velocity = bullet_velocity
        self._round_size = round_size

    def pull_trigger(self):
        RenpyCallbacks.get_instance().play_sfx("gunClick.ogg")
    
    def release_trigger(self):
        RenpyCallbacks.get_instance().play_sfx("gunSound.ogg")
        self.fire_bullet(self.create_bullet())
    
    def create_bullet(self):
        bullet = Bullet(self._round_size, self._round_size)
        bullet.position = self.position.copy()
        bullet.velocity = Vector2D(-self._bullet_velocity, 0) 

        return bullet
    
    def render(self, renderer):
        return renderer.render_gun(self)