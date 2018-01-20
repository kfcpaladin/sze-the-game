python early:
    import random
    class Ball:
        def __init__(self, **kargs):
            self.defaultOptions = {
                "bounds": (0, 0, 1366, 768),
                "colour": "#ffffff",
                "pos": Vector(0, 0),
                "radius": 10,
                "score": {
                    "left": 0,
                    "right": 0,
                },
                "speed": 20,
                "vel": Vector(0, 0),
            }
            self.setOptions(**kargs)
            self._start()

        """
            Set options given keyword arguments
        """
        def setOptions(self, **kargs):
            for key, value in self.defaultOptions.iteritems():
                if key in kargs:
                    setattr(self, key, kargs[key])
                else:
                    setattr(self, key, value)

        """
            Update physics
        """
        def update(self, dt=1.0):
            self._limitSpeed() 
            self.pos.add(self.vel.getMult(dt))
            self.checkBounds()

        """
            Limit ball to game window
        """
        def checkBounds(self):
            # Bounce off top and bottom boundary
            if self.pos.y - self.radius <= self.bounds[1]:
                self.vel.y = abs(self.vel.y)
            if self.pos.y + self.radius >= self.bounds[3]:
                self.vel.y = -abs(self.vel.y)
            # Reset if left or right boundaries
            if self.pos.x - self.radius <= self.bounds[0]:
                self.reset("left")
            if self.pos.x + self.radius >= self.bounds[2]:
                self.reset("right")

        """
            Given a paddle, bounce according to position difference
        """
        def bounceUsingVector(self, paddle):
            playsfx("vpunch.ogg")
            diff = self.pos.getSub(paddle.pos)
            diff.y /= (paddle.height/2.0)
            diff.x /= (paddle.width/2.0)
            yThreshold = 0.8
            xThreshold = 0.6
            # bounce horizontal
            if diff.x > xThreshold:
                self.vel.x = self.speed
                self.vel.y += paddle.vel.y
            elif diff.x < -xThreshold:
                self.vel.x = -self.speed
                self.vel.y += paddle.vel.y
            # bounce vertical
            if diff.y > yThreshold:
                self.vel.y = self.speed
                self.vel.x += paddle.vel.x
            elif diff.y < -yThreshold:
                self.vel.y = -self.speed
                self.vel.x += paddle.vel.x

        """
            reset the ball and add score to the correct side
        """
        def reset(self, side):    
            self.pos.x = self.bounds[2]/2.0
            self.pos.y = self.bounds[3]/2.0
            if side == "left":
                self.score["right"] += 1
                self.vel = Vector(
                    -self.speed/2.0 + random.randint(-2, 2), 
                    self.speed * random.randint(-5, 5) / 5.0
                )
            elif side == "right":
                self.score["left"] += 1
                self.vel = Vector(
                    self.speed/2.0 + random.randint(-2, 2), 
                    self.speed * random.randint(-5, 5) / 5.0
                )
        
        # Resets the ball position and nulls the score
        def resetScore(self):
            self.reset("left")
            self.score = {
                "left": 0,
                "right": 0
            }

        # Cap the velocity if it goes above the maximum limit
        def _limitSpeed(self, factor=2):
            maxSpeed = factor * self.speed
            if self.vel.x > maxSpeed:
                self.vel.x = maxSpeed
            if self.vel.y > maxSpeed:
                self.vel.y = maxSpeed

        # This will start the ball moving at a random direction
        def _start(self):
            if random.randint(0, 1) == 1:
                self.vel = Vector(
                    self.speed,
                    random.randint(-self.speed, self.speed),
                )
            else:
                self.vel = Vector(
                    -self.speed,
                    random.randint(-self.speed, self.speed),
                )
        
        

        
            


