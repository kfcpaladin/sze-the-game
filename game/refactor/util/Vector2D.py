class Vector2D(object):
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __neg__(self):
        return Vector2D(-self.x, -self.y)
    
    def __pos__(self):
        return self

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        self._x = value
    
    @y.setter
    def y(self, value):
        self._y = value
    
    