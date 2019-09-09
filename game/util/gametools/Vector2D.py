class Vector2D(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __neg__(self):
        return Vector2D(-self.x, -self.y)
    
    def __pos__(self):
        return self
    
    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5
    
    def __add__(self, v):
        return Vector2D(self.x+v.x, self.y+v.y)
    
    def __sub__(self, v):
        return Vector2D(self.x-v.x, self.y-v.y)
    
    def __mul__(self, k):
        return Vector2D(k*self.x, k*self.y)
    
    def __div__(self, k):
        return Vector2D(self.x/k, self.y/k)

    def copy(self):
        return Vector2D(self.x, self.y)
