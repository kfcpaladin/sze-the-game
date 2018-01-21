init -3 python:
    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def mult(self, mag):
            self.x *= mag
            self.y *= mag

        def add(self, vector):
            self.x += vector.x
            self.y += vector.y

        def sub(self, vector):
            self.x -= vector.x
            self.y -= vector.y

        def getSub(self, vector):
            v = Vector(self.x, self.y)
            v.sub(vector)
            return v
        
        def getMult(self, scalar):
            return Vector(self.x*scalar, self.y*scalar)
