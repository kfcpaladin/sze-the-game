init -2 python:
    class Paddle:   
        import pygame
        """
            Defining control constants
        """
        UP = 0
        DOWN = 1
        LEFT = 2
        RIGHT = 3

        """
            __init__ = initialises all paddle info
            __default__ = will initialise default values if parameters are not specified
        """
        def __init__(self, **kwargs):
            self.__default__(**kwargs)
            self.initialPos = self.pos.getCopy()

        def __default__(self, **kwargs):
            defaultOptions = {
                "ball": None,
                "bounds": (0, 0, 1366, 768),
                "colour": "#ffffff",
                "height": 100,
                "keys": None,
                "pos": Vector(0, 0),
                "speed": 10,
                "vel": Vector(0, 0),
                "width": 20,
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
            Bounce a given ball
        """
        # Takes paddle and bounces accordingly
        def bounce(self):
            if self.ball is None:
                return
            # Bounce if collide left and right
            if(self.checkYInside(self.ball.pos.y + self.ball.radius) or
               self.checkYInside(self.ball.pos.y - self.ball.radius)):
                # Left side
                if self.checkXInside(self.ball.pos.x + self.ball.radius):
                    self.ball.bounceUsingVector(self)
                # Right side
                elif self.checkXInside(self.ball.pos.x - self.ball.radius):
                    self.ball.bounceUsingVector(self)
            # Bounce if collide up and down
            if(self.checkXInside(self.ball.pos.x + self.ball.radius) or
               self.checkXInside(self.ball.pos.x - self.ball.radius)):
                # Top edge
                if self.checkYInside(self.ball.pos.y + self.ball.radius):
                    self.ball.bounceUsingVector(self)
                # Bottom edge
                elif self.checkYInside(self.ball.pos.y - self.ball.radius):
                    self.ball.bounceUsingVector(self)

        """
            Used to move the paddle
        """ 
        def move(self, direction=None):
            if direction == Paddle.UP:
                self.vel.y = -self.speed
            elif direction == Paddle.DOWN:
                self.vel.y = +self.speed
            elif direction == Paddle.LEFT:
                self.vel.x = -self.speed
            elif direction == Paddle.RIGHT:
                self.vel.x = +self.speed
            else:
                self.vel.x = 0
                self.vel.y = 0

        """
            control = Control a paddle using keypresses
            update = update velocity and check bounces and bounds
            reset = reset to original location and stop moving
        """
        def control(self):
            if not self.keys:
                return 
            pressed = pygame.key.get_pressed()
            keyPressed = False
            for keyName, direction in self.keys.iteritems():
                if pressed[keyName]:
                    self.move(direction)
                    keyPressed = True
            if not keyPressed:
                self.move()
        
        # updates game info on the position of paddle
        def update(self, dt=1.0):
            self.control()
            self.pos += self.vel*dt
            self.checkBounds()
            self.bounce()

        def reset(self):
            self.pos = self.initialPos.getCopy()
            self.move()

        """
            Used to check if a coordinate is within the x/y range
            of the paddle (Used by ball)
        """
        
        # Check if a x-coordinate is inline
        def checkXInside(self, x):
            if(x >= self.pos.x - self.width/2 and x <= self.pos.x + self.width/2):
                return True
            return False

        # Check if a y-coordinate is inline
        def checkYInside(self, y):
            if(y >= self.pos.y - self.height/2 and y <= self.pos.y + self.height/2):
                return True
            return False

        """
            render = render the paddle
            event = provide events to the paddle
        """
        def render(self, width, height, st, at):
            return renpy.render(Solid(self.colour), self.width, self.height, st, at) 

        def getRenderPos(self):
            return (self.pos.x-self.width/2, self.pos.y-self.height/2)
