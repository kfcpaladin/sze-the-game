# give dialog for the pong game
label playPong(pong=pong):
    menu:
        "Play pong":
            call screen pong(pong)
            "You finished playing pong!"
            "You got a net score of [_return]"
            return
        "Pass":
            "You pussy out"
            return

# run the pong game
screen pong(pong, fps=70, tickrate=50, duration=60):
    add screenBackgroundDir + "pong.jpg" 
    # default variables
    default rate = 1/float(fps)
    default dt = tickrate/float(fps)
    default time_remain = duration
    # score
    $ ball = pong.balls["ball"]
    $ score = ball.score["left"] - ball.score["right"]
    # Timer
    timer rate:
        repeat True
        action If(
            time_remain > 0, 
            true = [
                SetScreenVariable('time_remain', time_remain-rate)
            ], 
            false = [
                Function(ball.resetScore), 
                Hide('pong', dissolve),
                Return(score)
            ]
        )
    # update and render objects
    $ pong.update(dt)
    use render_pong_objects(pong)
    # Render timer and score
    use pong_timer(time_remain, duration)
    use pong_score(ball.score["left"], ball.score["right"])

# pong timer
screen pong_timer(time_remain, duration):
    # Bar will have a value proportional to the time remaining
    bar:
        value time_remain 
        range duration 
        xalign 0.5 
        yoffset 68 
        xmaximum 300 at alpha_dissolve # This is the timer bar.


# display pong score
screen pong_score(left, right):
    default scorePos = {
        "left":  (1366/4, 50),
        "right": (3*1366/4, 50),
    }
    default clearColour = "#ffffff00"
    default font = {
        "size": 60,
        "name": "DejaVuSans.ttf",
    }
    # Left score
    frame:
        xoffset scorePos["left"][0]
        yoffset scorePos["left"][1]
        background Color(clearColour)
        text "{0}".format(left):
            font font["name"]
            size font["size"]
    # Draw the right score
    frame:
        xoffset scorePos["right"][0]
        yoffset scorePos["right"][1]
        background Color(clearColour)
        text "{0}".format(right):
            font font["name"]
            size font["size"]

# render all pong objects
screen render_pong_objects(pong):
    for name, ball in pong.balls.iteritems():
        use pong_object(ball.pos.x, ball.pos.y, 2*ball.radius, 2*ball.radius, ball.colour)
    for name, paddle in pong.paddles.iteritems():
        use pong_object(paddle.pos.x, paddle.pos.y, paddle.width, paddle.height, paddle.colour)

# display a pong object
screen pong_object(x, y, width, height, colour="#ffffff"):
    frame:
        xoffset (x - width/2.0)
        yoffset (y - height/2.0)
        xsize width
        ysize height
        background Color(colour)