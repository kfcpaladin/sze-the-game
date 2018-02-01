# creates a bullet projectile
init -10 python:
    class Bullet:
        def __init__(self, pos=Vector(0, 0), vel=Vector(0, 0), size=Vector(10, 10)):
            self.create(pos, vel, size)
        
        def create(self, pos, vel, size):
            self.pos = pos
            self.vel = vel
            self.size = size
        
        def update(self, dt=1.0):
            self.pos.add(self.vel.getMult(dt))

        def checkBounds(self, bounds):
            if((self.pos.x < 0 or self.pos.x+self.size.x > bounds.x) or
               (self.pos.y < 0 or self.pos.y+self.size.y > bounds.y)):
                return False
            else:
                return True

        def checkCollide(self, targetPos, targetSize):
            if((self.pos.x > targetPos.x and self.pos.x+self.size.x < targetPos.x+targetSize.x)
                and (self.pos.y > targetPos.y and self.pos.y+self.size.y < targetPos.y+targetSize.y)):
                return True
            else:
                return False