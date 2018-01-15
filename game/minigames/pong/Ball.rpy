python early:
    import random
    class Ball:
        def __init__(self, pos, radius=10, speed=20, bounds=(0,0,1366,768)):
            self.pos = pos
            self.vel = Vector(0, 0)
            self.speed = speed
            self.radius = radius
            self.bounds = bounds    # bounds = (0, 0, 1366, 768)
            self.score = {
                "left": 0,
                "right": 0
            }
            self._start()

        def update(self, dt=1.0):
            self._limitSpeed()
            self.pos.add(self.vel.getMult(dt))
            self.checkBounds()

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

        # Takes paddle and bounces accordingly
        def bounce(self, paddle):
            # Bounce if collide left and right
            if(paddle._checkYInside(self.pos.y + self.radius) or
                    paddle._checkYInside(self.pos.y - self.radius)):
                # Left side
                if paddle._checkXInside(self.pos.x + self.radius):
                    self.bounceUsingVector(paddle)
                # Right side
                elif paddle._checkXInside(self.pos.x - self.radius):
                    self.bounceUsingVector(paddle)
            # Bounce if collide up and down
            if(paddle._checkXInside(self.pos.x + self.radius) or
                    paddle._checkXInside(self.pos.x - self.radius)):
                # Top edge
                if paddle._checkYInside(self.pos.y + self.radius):
                    self.bounceUsingVector(paddle)
                # Bottom edge
                elif paddle._checkYInside(self.pos.y - self.radius):
                    self.bounceUsingVector(paddle)

        def bounceUsingVector(self, paddle):
            playsfx("vpunch.ogg")
            diff = self.pos.getSub(paddle.pos)
            diff.y /= (paddle.height/2.0)
            diff.x /= (paddle.width/2.0)
            # bounce horizontal
            if diff.x > 0.8:
                self.vel.x = self.speed
            elif diff.x < -0.8:
                self.vel.x = -self.speed
            # bounce vertical
            if diff.y > 0.8:
                self.vel.y = self.speed
            elif diff.y < -0.8:
                self.vel.y = -self.speed


        def reset(self, side):    
            self.pos.x = self.bounds[2]/2.0
            self.pos.y = self.bounds[3]/2.0
            if side == "left":
                self.score["right"] += 1
                self.vel = Vector(
                    self.speed + random.randint(-2, 2), 
                    self.speed + random.randint(0, 2)
                )
            elif side == "right":
                self.score["left"] += 1
                self.vel = Vector(
                    self.speed + random.randint(-2, 2), 
                    -self.speed - random.randint(0, 2)
                )
        
        # Resets the ball position and nulls the score
        def resetScore(self):
            self.reset("left")
            self.score = {
                "left": 0,
                "right": 0
            }

        # Cap the velocity if it goes above the maximum limit
        def _limitSpeed(self):
            if self.vel.x > self.speed:
                self.vel.x = self.speed
            if self.vel.y > self.speed:
                self.vel.y = self.speed

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
        
        

        
            


