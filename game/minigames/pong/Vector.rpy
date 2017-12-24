python early:
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