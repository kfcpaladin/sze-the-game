from .Bullet import Bullet

def block_if_dead(func):
    def wrapped(instance, *args, **kwargs):
        if not instance.has_died:
            return func(instance, *args, **kwargs)
    return wrapped

class GunshotSuicide(object):
    def __init__(self, bounding_box, head, gun):
        self._bounding_box = bounding_box
        self._bullets = [] 
        self._head = head
        self._gun = gun
        self._has_died = False

    def reset(self):
        self._bullets = []
        self._has_died = False

    @property
    def has_died(self):
        return self._has_died

    @property
    def bullets(self):
        return self._bullets

    @block_if_dead 
    def pull_trigger(self):
        self._gun.pull_trigger()

    @block_if_dead 
    def release_trigger(self):
        self._gun.release_trigger()

    @block_if_dead 
    def move_gun(self, position):
        self._gun.position = position.copy()

    @block_if_dead 
    def update(self, dt):
        for bullet in self._gun:
            self._bullets.append(bullet)

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
        self._has_died = True
    
