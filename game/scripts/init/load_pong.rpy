init 1 python:
    pong = load_basic_pong_game()

init python:
    def load_basic_pong_game():
        from models.pong import *
        from util.gametools import Vector2D, Rect2D
        from util.colours import PrimaryColours
        import pygame

        bounding_box = Rect2D(right=config.screen_width, bottom=config.screen_height)
        padding = 20

        pong = Pong(bounding_box)


        top_wall = Wall(width=bounding_box.width, height=100)
        top_wall.position.y = -100
        bottom_wall = Wall(width=bounding_box.width, height=100)
        bottom_wall.position.y = bounding_box.bottom

        ball = Ball(width=30, height=30, speed=config.screen_width/1.5, colour=PrimaryColours.WHITE)
        ball.position = Vector2D(1366/2, 768/2)
        ball.velocity.x = ball.speed

        left_paddle = Paddle(width=40, height=150, speed=500, colour=PrimaryColours.WHITE)
        left_paddle.position = Vector2D(padding, 768/2 - left_paddle.height/2)
        left_paddle_controls = PaddleControls(left_paddle, up_key=pygame.K_UP, down_key=pygame.K_DOWN)

        right_paddle = Paddle(width=40, height=150, speed=500, colour=PrimaryColours.WHITE)
        right_paddle.position = Vector2D(1366-left_paddle.width-padding, 768/2 - left_paddle.height/2)
        right_paddle_bot = PaddleBot(right_paddle, bounding_box, skill=10)


        extra_ball = Ball(width=30, height=30, speed=config.screen_width/1.5, colour=PrimaryColours.GREEN)
        extra_ball.position = Vector2D(1366/2, 768/2)
        extra_ball.velocity.x = extra_ball.speed

        right_paddle_bot.track_ball(ball)
        right_paddle_bot.track_ball(extra_ball)

        pong.add(top_wall)
        pong.add(bottom_wall)
        pong.add(ball)
        pong.add(extra_ball)
        pong.add(left_paddle)
        pong.add(right_paddle)
        pong.add(left_paddle_controls)
        pong.add(right_paddle_bot)

        return pong
