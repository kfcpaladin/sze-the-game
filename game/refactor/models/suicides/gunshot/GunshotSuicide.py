from .Bullet import Bullet

class GunshotSuicide(object):
    def __init__(self, bounding_box, head, gun):
        self._bounding_box = bounding_box
        self._bullets = [] 
        self._head = head
        self._gun = gun
        self._has_died = False

    def reset(self):
        self._bullets.clear()
        self._has_died = False

    @property
    def has_died(self):
        return self._has_died

    @property
    def bullets(self):
        return self._bullets

    def fire_gun(self):
        if self.has_died:
            return 
        bullet = self._gun.fire_bullet()
        self._bullets.append(bullet)
    
    def update(self, dt):
        for bullet in self._bullets:
            bullet.update(dt)
            if bullet.check_collision(self._head):
                return self._on_hit()
        self._bullets = [b for b in self._bullets if not b.check_despawned(self._bounding_box)]
    

    def render(self, renderer):
        for bullet in self._bullets:
            bullet.render(renderer)

        self._gun.render(renderer)
        self._head.render(renderer)

    def _on_hit(self):
        self._bullets.clear()
        self._has_died = True
    
