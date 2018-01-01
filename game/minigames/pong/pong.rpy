init python:
    ball = Ball(
        pos = Vector(1366/2, 768/2),
        radius = 20,
    )

    leftPaddle = Paddle(
        pos = Vector(50, 768/2),
        size = (50, 200),
        speed=20,
        player=1,
    )

    rightPaddle = Paddle(
        pos = Vector(1366-50, 768/2),
        size = (50, 200),
        speed=20,
        player=0,
    )

    rightPaddleBot = PaddleBot(ball, rightPaddle, skill=1)
