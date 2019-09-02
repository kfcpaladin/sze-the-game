init 1 python:
    pong = Pong()
    pong.initStandard()
    pong.addPaddles({
        "wallLeft": Paddle(
            ball = pong.balls["ball"],
            colour = "#375da8",
            height = 150,
            pos = Vector(1366/2, 0+75),
            speed = 0,
            width = 30,
        ),
        "wallRight": Paddle(
            ball = pong.balls["ball"],
            colour = "#375da8",
            height = 150,
            pos = Vector(1366/2, 768-75),
            speed = 0,
            width = 30,
        ),
    })
    pong.paddles["leftPaddle"].colour = themes.default.rainbow
