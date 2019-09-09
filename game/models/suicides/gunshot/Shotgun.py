from util.gametools import Vector2D
from util import RenpyCallbacks
from .Bullet import Bullet
from .Gun import Gun

import random
import math

class Shotgun(Gun):
    def __init__(self, width, height, bullet_velocity, round_size, spread_angle):
        Gun.__init__(self, width, height)
        self._bullet_velocity = bullet_velocity
        self._round_size = round_size
        self._spread_angle = spread_angle

    def pull_trigger(self):
        RenpyCallbacks.get_instance().play_sfx("shotgun_fire.ogg")
        for _ in range(8):
            bullet = self.create_bullet()
            angle = random.uniform(-self._spread_angle, self._spread_angle)
            # cos(90-angle) = dy/dx
            # dy = dx * cos(90-angle) = -dx*sin(angle) 
            bullet.velocity.y = self._bullet_velocity * math.sin(angle * math.pi / 180)
            self.fire_bullet(bullet)
    
    def release_trigger(self):
        pass
        # RenpyCallbacks.get_instance().play_sfx("shotgun_reload.ogg")
    
    def create_bullet(self):
        bullet = Bullet(self._round_size, self._round_size)
        bullet.position = self.position.copy()
        bullet.velocity = Vector2D(-self._bullet_velocity, 0) 

        return bullet
    
    def render(self, renderer):
        return renderer.render_shotgun(self)