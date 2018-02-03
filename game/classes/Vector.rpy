init -20 python:
    """
        Vector class used by pong in particular, and screen elements which
        use it for the x,y attributes for positioning and size
    """
    class Vector:
        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y

        """
            Vector operand default python methods
        """
        def __add__(self, vector):
            return Vector(self.x+vector.x, self.y+vector.y)

        def __sub__(self, vector):
            return Vector(self.x-vector.x, self.y-vector.y)

        def __mul__(self, scalar):
            return Vector(self.x*scalar, self.y*scalar)

        def __div__(self, scalar):
            return Vector(self.x/float(scalar), self.y/float(scalar))

        """
            Base vector method (TO BE REMOVED)
        """
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

        """
            Get a copy of the vector
        """
        def getCopy(self):
            return Vector(self.x, self.y)
