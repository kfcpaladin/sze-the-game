from .Entity import Entity

def add_persistence(cls):
    class PersistentEntity(cls):
        def __init__(self, *args, **kwargs):
            cls.__init__(self, *args, **kwargs)
            self.store()

        def store(self):
            self._initial_position = self.position.copy()
            self._initial_velocity = self.velocity.copy()

        def load(self):
            self.position = self._initial_position
            self.velocity = self._initial_velocity
    return PersistentEntity
    