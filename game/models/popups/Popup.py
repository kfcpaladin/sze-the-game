class Popup(object):
    def __init__(self, message, icon=None, colour=None, lifespan=2):
        self._message = message
        self._icon = icon
        self._colour = colour
        self._lifespan = lifespan

    @property
    def message(self):
        return self._message
    
    @property
    def icon(self):
        return self._icon
    
    @property
    def colour(self):
        return self._colour
    
    @property
    def lifespan(self):
        return self._lifespan

    def update(self, dt):
        if self._lifespan > 0:
            self._lifespan -= dt
            if self._lifespan < 0:
                self._lifespan = 0

    @property
    def is_alive(self):
        return self._lifespan > 0

    def __eq__(self, other):
        return self.message == other.message
        