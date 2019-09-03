init 1 python:
    pong = load_basic_pong_game()

init python:
    def load_basic_pong_game():
        from refactor.models.pong import *
        from refactor.util import Vector2D
        from refactor.util.colours import PrimaryColours

        pong = Pong()

        ball = Ball(width=15, height=15, colour=PrimaryColours.WHITE)
        ball.position = Vector2D(1366/2, 768/2)
        ball.velocity.x = 200

        left_paddle = Paddle(width=20, height=200, speed=50, colour=PrimaryColours.WHITE)
        left_paddle.position = Vector2D(20, 768/2 - left_paddle.height/2)

        right_paddle = Paddle(width=200, height=200, speed=50, colour=PrimaryColours.WHITE)
        right_paddle.position = Vector2D(1366/2 + 50, 768/2 - left_paddle.height/2)

        pong.add(ball)
        pong.add(left_paddle)
        pong.add(right_paddle)

        return pong
