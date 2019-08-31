class Popup(object):
    def __init__(self, message, icon=None, lifespan=2):
        self._message = message
        self._icon = icon
        self._lifespan = lifespan

    @property
    def message(self):
        return self._message
    
    @property
    def icon(self):
        return self._icon
    
    @property
    def lifespan(self):
        return self._lifespan

    def update(self, dt):
        self._lifespan -= dt

    @property
    def is_alive(self):
        return self._lifespan >= 0