init -2 python:
    import random
    import collections
    class Ball:
        """
            Ball constants for determining which side
        """
        LEFT = 0
        RIGHT = 1

        """
            __init__ = initialises all paddle info
            __default__ = will initialise default values if parameters are not specified
        """
        def __init__(self, **kwargs):
            self.__default__(**kwargs)
            self._start()

        def __default__(self, **kwargs):
            defaultOptions = {
                "bounds": (0, 0, 1366, 768),
                "colour": "#ffffff",
                "pos": Vector(0, 0),
                "radius": 10,
                "score": AttrDict({
                    "left": 0,
                    "right": 0,
                }),
                "speed": 20,
                "vel": Vector(0, 0),
            }
            defaultOptions.update(kwargs)
            self.setOptions(**defaultOptions)

        """
            Set options given keyword arguments
        """
        def setOptions(self, **kwargs):
            for key, value in kwargs.iteritems():
                setattr(self, key, value)

        """
            Update physics
        """
        def update(self, dt=1.0):
            self._limitSpeed() 
            self.pos += self.vel*dt
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
                self.reset(Ball.LEFT)
            if self.pos.x + self.radius >= self.bounds[2]:
                self.reset(Ball.RIGHT)

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
            Get the rendering and events
        """
        def render(self, width, height, st, at):
            return renpy.render(Solid(self.colour), 2*self.radius, 2*self.radius, st, at) 

        def getRenderPos(self):
            return (self.pos.x-self.radius, self.pos.y-self.radius)

        """
            reset the ball and add score to the correct side
        """
        def reset(self, side):    
            self.pos.x = self.bounds[2]/2.0
            self.pos.y = self.bounds[3]/2.0
            if side == Ball.LEFT:
                self.score.right += 1
                self.vel = Vector(
                    -self.speed/2.0 + random.randint(-2, 2), 
                    self.speed * random.randint(-5, 5) / 5.0
                )
            elif side == Ball.RIGHT:
                self.score.left += 1
                self.vel = Vector(
                    self.speed/2.0 + random.randint(-2, 2), 
                    self.speed * random.randint(-5, 5) / 5.0
                )
        
        # Resets the ball position and nulls the score
        def resetScore(self):
            self.reset(Ball.LEFT)
            self.score.left = 0
            self.score.right = 0

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

        
        
        

        
            


