init python:
    class Pong:
        def __init__(self):
            self.balls = {}
            self.paddles = {}
            self.bots = {}

        def initStandard(self):
            # ball
            self.balls["ball"] = Ball(
                colour = "#c2d12a",
                pos = Vector(1366/2, 768/2),
                radius = 10,
                speed = 25,
            )
            # left paddle
            self.paddles["leftPaddle"] = Paddle(
                ball = self.balls["ball"],
                bounds = (0, 0, 1366/2, 768),
                colour = "#32b1cb",
                height = 150,
                keys = {
                    "up": "K_UP",
                    "down": "K_DOWN",
                    "left": "K_LEFT",
                    "right": "K_RIGHT",
                },
                pos = Vector(50, 768/2),
                speed = 20,
                width = 40,
            )
            # right paddle
            self.paddles["rightPaddle"] = Paddle(
                ball = self.balls["ball"],
                bounds = (1366/2, 0, 1366, 768),
                colour = "#cb3932",
                height = 150,
                pos = Vector(1366-50, 768/2),
                speed = 20,
                width = 40,
            )
            # right paddle bot
            self.bots["rightPaddleBot"] = PaddleBot(
                self.balls["ball"], 
                self.paddles["rightPaddle"], 
                skill=1
            )

        def addBalls(self, balls):
            if type(ball) is dict:
                self.combineDicts(self.balls, balls)
            else:
                raise TypeError("Expected dictionary of balls")

        def addPaddles(self, paddles):
            if type(paddles) is dict:
                self.combineDicts(self.paddles, paddles)
            else:
                raise TypeError("Expected dictionary of paddles")

        def combineDicts(self, dictA, dictB):
            for key, value in dictB.iteritems():
                if key not in dictA:
                    dictA[key] = value
        
        def update(self, dt=1.0):
            for name, ball in self.balls.iteritems():
                ball.update(dt)
            for name, paddle in self.paddles.iteritems():
                paddle.update(dt)
            for name, bot in self.bots.iteritems():
                bot.update()


    