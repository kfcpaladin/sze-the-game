init -1 python:
    class Pong(renpy.Displayable):
        def __init__(self, **kwargs):
            renpy.Displayable.__init__(self)
            self.__default__(**kwargs)
            self.initPhysics()

        def __default__(self, **kwargs):
            defaultParam = {
                "fps": config.framerate,
                "tickrate": 30,
                "balls": {},
                "paddles": {},
                "bots": {},
                "duration": 30,
            }
            defaultParam.update(kwargs)
            self.applyParameters(**defaultParam)

        def applyParameters(self, **kwargs):
            for param, value in kwargs.iteritems():
                setattr(self, param, value)

        def initPhysics(self):
            self.dt = 1/float(self.fps)
            self.timeRemain = self.duration

        def initStandard(self):
            import pygame
            # ball
            self.balls["ball"] = Ball(
                colour = "#c2d12a",
                pos = Vector2D(1366/2, 768/2),
                radius = 15,
                speed = 20,
            )
            # left paddle
            self.paddles["leftPaddle"] = Paddle(
                ball = self.balls["ball"],
                bounds = (0, 0, 1366/2, 768),
                colour = "#32b1cb",
                height = 150,
                keys = {
                    pygame.K_UP: Paddle.UP, 
                    pygame.K_DOWN: Paddle.DOWN, 
                    pygame.K_LEFT: Paddle.LEFT, 
                    pygame.K_RIGHT: Paddle.RIGHT,
                },
                pos = Vector2D(50, 768/2),
                speed = 20,
                width = 40,
            )
            # right paddle
            self.paddles["rightPaddle"] = Paddle(
                ball = self.balls["ball"],
                bounds = (1366/2, 0, 1366, 768),
                colour = "#cb3932",
                height = 150,
                pos = Vector2D(1366-50, 768/2),
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
            self.balls.update(balls)

        def addPaddles(self, paddles):
            self.paddles.update(paddles)
        
        """
            update = update all objects
            reset = reset all game objects
        """
        def update(self, dt=1.0):
            for name, ball in self.balls.iteritems():
                ball.update(dt)
            for name, paddle in self.paddles.iteritems():
                paddle.update(dt)
            for name, bot in self.bots.iteritems():
                bot.update()

        def reset(self):
            self.timeRemain = self.duration
            for name, ball in self.balls.iteritems():
                ball.resetScore()
            for name, paddle in self.paddles.iteritems():
                paddle.reset()

        """
            Using it as a renpy displayable
            render = passes width, height, st, at
                - st = time since the displayable was shown
                - at = time since a tag that the displayable shares was used?
            event = passes ev, x, y, st
                - ev = event object
                - x,y = position of event
                - st = time since start
        """
        def event(self, ev, x, y, st):
            if self.timeRemain <= 0:
                score = self.balls["ball"].score
                results = {"score": score.left-score.right, "surrender": False}
                self.reset()
                return results
            else:
                raise renpy.IgnoreEvent()

        def render(self, width, height, st, at):
            screen = renpy.Render(width, height)    # get screen
            screen.blit(renpy.render(Image(loadImage("screen_bg_pong.png")), width, height, st, at), (0, 0))
            self.timeRemain -= self.dt
            self.update(self.tickrate*self.dt)
            for name, ball in self.balls.iteritems():
                screen.blit(ball.render(width, height, st, at), ball.getRenderPos())
            for name, paddle in self.paddles.iteritems():
                screen.blit(paddle.render(width, height, st, at), paddle.getRenderPos())
            screen.blit(self.renderScore("ball"), (0, 0))
            screen.blit(self.renderDuration(), (0, 20))
            renpy.redraw(self, 0)
            return screen

        """
            Render game information
        """
        def renderScore(self, ballName):
            score = self.balls[ballName].score
            scoreText = Text("{0}/{1}".format(score.left, score.right))
            return renpy.render(scoreText, 100, 100, 0, 0)

        def renderDuration(self):
            duration = Text("{:.02f}".format(self.timeRemain))
            return renpy.render(duration, 100, 100, 0, 0)



    