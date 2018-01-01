label playPong(**options):
    menu:
        "Play pong":
            call screen pong(**options)
            "You finished playing pong!"
            "You got a net score of [_return]"
            return
        "Pass":
            "You pussy out"
            return

screen pong(ball=ball, leftPaddle=leftPaddle, rightPaddle=rightPaddle,
                leftPaddleBot=None, rightPaddleBot=rightPaddleBot,
                rate=1.0/30.0, duration=60):
    use navigation # Include the navigation.
    tag menu
    add "pong.jpg" 
    default time_remain = duration
    $ score = ball.score["left"] - ball.score["right"]
    # Timer
    timer rate:
        repeat True
        action If(
            time_remain > 0, 
            true=[SetScreenVariable('time_remain', time_remain-rate)], 
            false=[Function(ball.resetScore), Hide('pong', dissolve),Return(score)]
        )
    
    $ colours = {
        "ball": "#ffffffff",
        "leftPaddle": "#ffffffff",
        "rightPaddle": "#ffffffff",
        "score": "#ffffff00",
    }
    $ scorePos = {
        "left": (1366/4, 50),
        "right": (3*1366/4, 50),
    }
    # Bar will have a value proportional to the time remaining
    bar:
        value time_remain 
        range duration 
        xalign 0.5 
        yoffset 68 
        xmaximum 300 at alpha_dissolve # This is the timer bar.
    # Draw the ball
    frame:
        xoffset ball.pos.x - ball.radius
        yoffset ball.pos.y - ball.radius
        xsize 2*ball.radius
        ysize 2*ball.radius
        background Color(colours["ball"])
    
    # Draw and control the left paddle
    frame:
        xoffset leftPaddle.pos.x - leftPaddle.width/2
        yoffset leftPaddle.pos.y - leftPaddle.height/2
        xsize leftPaddle.width
        ysize leftPaddle.height
        background Color(colours["leftPaddle"])

    # Draw the right paddle
    frame:
        xoffset rightPaddle.pos.x - rightPaddle.width/2
        yoffset rightPaddle.pos.y - rightPaddle.height/2
        xsize rightPaddle.width
        ysize rightPaddle.height
        background Color(colours["rightPaddle"])
    
    # Draw the left score
    frame:
        xoffset scorePos["left"][0]
        yoffset scorePos["left"][1]
        background Color(colours["score"])
        text "{0}".format(ball.score["left"]):
            font "DejaVuSans.ttf"
            size 60
    # Draw the right score
    frame:
        xoffset scorePos["right"][0]
        yoffset scorePos["right"][1]
        background Color(colours["score"])
        text "{0}".format(ball.score["right"]):
            font "DejaVuSans.ttf"
            size 60
    $ getKeyPress(leftPaddle)
    $ rightPaddleBot.movePaddle()

    # Update the game
    $ ball.update()
    $ leftPaddle.update()
    $ rightPaddle.update()
    $ ball.bounce(leftPaddle)
    $ ball.bounce(rightPaddle)

init python:
    import pygame
    def getKeyPress(paddle):
        pressed = pygame.key.get_pressed()
        keyPressed = False
        if pressed[pygame.K_UP]:
            paddle.move("up")
            keyPressed = True
        if pressed[pygame.K_DOWN]:
            paddle.move("down")
            keyPressed = True
        if pressed[pygame.K_LEFT]:
            paddle.move("left")
            keyPressed = True
        if pressed[pygame.K_RIGHT]:
            paddle.move("right")
            keyPressed = True
        if not keyPressed:
            paddle.move(None)