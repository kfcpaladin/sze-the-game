python early:
    class Paddle:   
        import pygame
        def __init__(self, **kargs):
            self.defaultOptions = {
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
            self.setOptions(**kargs)
            
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
            Control a paddle using keypresses
        """
        def control(self):
            if not self.keys:
                return 
            pressed = pygame.key.get_pressed()
            keyPressed = False
            for keyName, keyCode in self.keys.iteritems():
                if pressed[getattr(pygame, keyCode)]:
                    self.move(keyName)
                    keyPressed = True
            if not keyPressed:
                self.vel.x = self.vel.y = 0

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
        def update(self, dt=1.0):
            self.control()
            self.pos.add(self.vel.getMult(dt))
            self.checkBounds()
            self.bounce()

        """
            Used to check if a coordinate is within the x/y range
            of the paddle (Used by ball)
        """
        
        # Check if a x-coordinate is inline
        def checkXInside(self, x):
            if(x >= self.pos.x - self.width/2 and
                    x <= self.pos.x + self.width/2):
                return True
            return False
        # Check if a y-coordinate is inline
        def checkYInside(self, y):
            if(y >= self.pos.y - self.height/2 and
                    y <= self.pos.y + self.height/2):
                return True
            return False
