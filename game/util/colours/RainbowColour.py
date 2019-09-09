"""
Sequence of the colour:
    (255, 0->255, 0) => (255, 255, 0)   # Rising    i=0, j=i+1=1
    (255->0, 255, 0) => (0, 255, 0)     # Falling   i=0, j=i=0
    (0, 255, 0->255) => (0, 255, 255)   # Rising    i=1, j=i+1=2
    (0, 255->0, 255) => (0, 0, 255)     # Falling   i=1, j=i=1
    (0->255, 0, 255) => (255, 0, 255)   # Rising    i=2, j=(i+1)%3=0
    (255, 0, 255->0) => (255, 0, 0)     # Falling   i=2, j=i=2
"""
class RainbowColour(object):
    
    def __init__(self, alpha=255):
        self._index = 0
        self._current_edge = self._rising_edge
        self._components = [255, 0, 0, alpha]

    def update(self, amount=1):
        self._current_edge(amount)

    def __str__(self):
        return "#{:02x}{:02x}{:02x}{:02x}".format(*self._components)

    @property
    def alpha(self):
        return self._components[3]
    
    @alpha.setter
    def alpha(self, value):
        self._components[3] = self._clamp(value)
    
    @property
    def components(self):
        return tuple(self._components)

    @property
    def rgb(self):
        return tuple(self._components[0:3])
    
    @property
    def rgba(self):
        return tuple(self._components)
    
    def _falling_edge(self, amount):
        i = self._index
        self._components[i] = self._clamp(self._components[i]-amount)
        if self._components[i] == 0:
            self._index = (self._index + 1) % 3
            self._current_edge = self._rising_edge
    
    def _rising_edge(self, amount):
        i = (self._index + 1) % 3
        self._components[i] = self._clamp(self._components[i]+amount)
        if self._components[i] == 255:
            self._current_edge = self._falling_edge

    def _clamp(self, value):
        value = int(value)
        if value < 0:
            return 0
        elif value > 255:
            return 255
        return value