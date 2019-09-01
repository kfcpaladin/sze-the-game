from refactor.util import RenpyCallbacks

class PopupsViewController:
    def __init__(self, manager):
        self._manager = manager
        self._manager.listen_populate(self._show_screen)
        self._fade_time = 1

    @property
    def popups(self):
        return self._manager.popups
    
    @property
    def total(self):
        return self._manager.total

    def update(self, dt):
        self._manager.update(dt)

    def get_transparency(self, popup):
        lifespan = self._clamp(popup.lifespan, 0, self._fade_time)
        return 255 * lifespan / self._fade_time

    def _show_screen(self, _):
        RenpyCallbacks.get_instance().show_screen("popup", self)

    def _clamp(self, value, _min, _max):
        if value > _max:
            return _max
        elif value < _min:
            return _min
        return value
            