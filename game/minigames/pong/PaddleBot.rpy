python early:
    class PaddleBot:
        def __init__(self, ball, paddle, skill=1):
            self.ball = ball
            self.paddle = paddle
            self.skill = skill
            self.inPosition = False
        
        def checkDirection(self):
            posDiff = self.paddle.pos.x - self.ball.pos.x
            if posDiff * self.ball.vel.x < 0:
                return False
            else:
                return True
        
        def predictCollision(self):
            # if ball is not moving horizontally, just match y-pos
            if(self.ball.vel.x == 0):
                return self.ball.pos.y
            # equation variables
            m = self.ball.vel.y / self.ball.vel.x
            b = self.ball.pos.y - m*self.ball.pos.x
            x = self.paddle.pos.x
            # Get dimensions
            width = self.paddle.width/2
            bounds = self.paddle.bounds
            radius = self.ball.radius
            # If coming from left side
            if self.ball.vel.x < 0:
                direction = -1
                prediction = lambda m,x,b,width: m*(x+width)+b
            else:
                direction = 1
                prediction = lambda m,x,b,width: m*(x-width)+b
            y = bounds[3] / 2
            # Get prediction
            for i in xrange(self.skill):
                y = prediction(m,x,b,width)
                if(y < bounds[3] and y > bounds[1]):
                    break
                if m*direction >= 0:
                    b = 2*(bounds[3]-radius)-b
                else:
                    b = 2*(bounds[1]+radius)-b
                m *= -1
            # If prediction is out of bounds
            if(y > bounds[3] or y < bounds[1]):
                y = self.ball.pos.y
            
            return y
        
        def movePaddle(self):
            if self.checkDirection():
                y = self.predictCollision()
                # If the bot is not in a position where it can hit the ball
                if self.inPosition is False:
                    # Get it to be within middle segment
                    if y > self.paddle.pos.y + self.paddle.height/3:
                        self.paddle.move("down")
                    elif y < self.paddle.pos.y - self.paddle.height/3:
                        self.paddle.move("up")
                    else:
                        self.paddle.move()
                        self.inPosition = True
                # If the predicte intercept is within the paddle's height
                else:
                    if y > self.paddle.pos.y + self.paddle.height/2:
                        self.inPosition = False
                    elif y < self.paddle.pos.y - self.paddle.height/2:
                        self.inPosition = False
        
                
