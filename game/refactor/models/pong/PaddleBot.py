from refactor.util.gametools import Controls

class PaddleBot(Controls):
    def __init__(self, ball, paddle, bounds, skill=1):
        self.ball = ball
        self.paddle = paddle
        self.skill = skill
        self.bounds = bounds
        self.inPosition = False
    
    def checkDirection(self):
        posDiff = self.paddle.position.x - self.ball.position.x
        if posDiff * self.ball.velocity.x < 0:
            return False
        else:
            return True
    
    def predictCollision(self):
        # if ball is not moving horizontally, just match y-pos
        if self.ball.velocity.x == 0:
            return self.ball.position.y
        # equation variables
        m = self.ball.velocity.y / self.ball.velocity.x
        b = self.ball.position.y - m*self.ball.position.x
        x = self.paddle.position.x
        # Get dimensions
        width = self.paddle.width/2
        bounds = self.bounds
        radius = self.ball.height
        # If coming from left side
        if self.ball.velocity.x < 0:
            direction = -1
            prediction = lambda m,x,b,width: m*(x+width)+b
        else:
            direction = 1
            prediction = lambda m,x,b,width: m*(x-width)+b
        y = bounds.bottom / 2
        # Get prediction
        for _ in range(self.skill):
            y = prediction(m,x,b,width)
            if(y < bounds.bottom and y > bounds.left):
                break
            if m*direction >= 0:
                b = 2*(bounds.bottom-radius)-b
            else:
                b = 2*(bounds.left+radius)-b
            m *= -1
        # If prediction is out of bounds
        if(y > bounds.bottom or y < bounds.left):
            y = self.ball.position.y
        
        return y
    
    def update(self):
        if self.checkDirection():
            y = self.predictCollision()
            # If the bot is not in a position where it can hit the ball
            if self.inPosition is False:
                # Get it to be within middle segment
                if y > self.paddle.position.y + self.paddle.height/3:
                    self.paddle.move_down()
                elif y < self.paddle.position.y - self.paddle.height/3:
                    self.paddle.move_up()
                else:
                    self.paddle.stop()
                    self.inPosition = True
            # If the predicte intercept is within the paddle's height
            else:
                if y > self.paddle.position.y + self.paddle.height/2:
                    self.inPosition = False
                elif y < self.paddle.position.y - self.paddle.height/2:
                    self.inPosition = False