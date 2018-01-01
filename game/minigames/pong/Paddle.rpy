python early:
    class Paddle:   
        def __init__(self, pos, speed=10, size=(5, 10), bounds=(0,0,1366,768), player=1):
            self.pos = pos
            self.vel = Vector(0, 0)
            self.speed = speed
            self.width = size[0]
            self.height = size[1]
            self.bounds = bounds

        """
            If the paddle reaches a bound, push it back into the bounds
        """
        def checkBounds(self):
            # Top edge
            if self.pos.y - self.height/2 < self.bounds[1]:
                self.pos.y = self.bounds[1] + self.height/2
                self.vel.y = 0
            # Bottom edge
            if self.pos.y + self.height/2 > self.bounds[3]:
                self.pos.y = self.bounds[3] - self.height/2
                self.vel.y = 0
            # Left edge
            if self.pos.x - self.width/2 < self.bounds[0]:
                self.pos.x = self.bounds[0] + self.width/2
                self.vel.x = 0
            # Right edge
            if self.pos.x + self.width/2 > self.bounds[2]:
                self.pos.x = self.bounds[2] - self.width/2
                self.vel.x = 0

        """
            Used to move the paddle
        """ 
        def move(self, direction=None):
            if direction == "up":
                self.vel.y = -self.speed
            elif direction == "down":
                self.vel.y = +self.speed
            elif direction == "left":
                self.vel.x = -self.speed
            elif direction == "right":
                self.vel.x = +self.speed
            else:
                self.vel.y = 0
                self.vel.x = 0
        
        # updates game info on the position of paddle
        def update(self):
            self.pos.add(self.vel)
            self.checkBounds()

        """
            Used to check if a coordinate is within the x/y range
            of the paddle (Used by ball)
        """
        
        # Check if a x-coordinate is inline
        def _checkXInside(self, x):
            if(x >= self.pos.x - self.width/2 and
                    x <= self.pos.x + self.width/2):
                return True
            return False
        # Check if a y-coordinate is inline
        def _checkYInside(self, y):
            if(y >= self.pos.y - self.height/2 and
                    y <= self.pos.y + self.height/2):
                return True
            return False
