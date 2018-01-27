# give dialog for the pong game
init python:
    _score = 0
    _surrender = False

label playPong(pong=pong):
    menu:
        "Play pong":
            $ _previousMusic = getMusicHistory(-1)
            $ playmusic("VarienThroneOfRavens.ogg")
            call screen screen_pong(pong)
            $ stopmusic()
            $ _score = _return["score"]
            $ _surrender = _return["surrender"]
            if _surrender:
                "You surrender like a pussy bitch"
                "You failed by [_score] points"
            else:
                "You finished playing pong!"
                if _score > 0:
                    $ playmusic("p4LikeADreamComeTrue.ogg")
                    "You won with a net score of [_score]"
                    "After your victorious victory, you decide to masturbate furiously tonight"
                    "{i}zippppp....{/i}"
                    "You decide to zip your {b}pants{/b} back up"
                    $ sze.gain("strength", 5)
                elif _score < 0:
                    "You lose miserably by [_score] points"
                    "Perhaps it is time you killed yourself"
                    "{b}Tip: {/b}Press kms to commit suicide"
                    $ sze.loss("strength", 2)
                else:
                    "You tied with your opponent"
                    "Perhaps this is time for a truce"
                    $ sze.gain("strength", 1)
            $ playmusic(_previousMusic)
            return
        "Pass":
            "You pussy out"
            return

# run the pong game
screen screen_pong(pong, fps=60, tickrate=50, duration=30):
    modal True
    add loadImage("screen_bg_pong.png")
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
                Return({"score":score, "surrender": False}),
            ]
        )
    # surrender button
    textbutton "Surrender":
        xalign 0.9
        yalign 0.1
        action If(
            score < 0,
            true = [
                Function(ball.resetScore),
                Hide("pong", dissolve),
                Return({"score":score, "surrender": True}),
            ],
            false = [
                Function(popup, "You can only surrender if you suck shit"),
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
    default font = {
        "size": 60,
        "name": "DejaVuSans.ttf",
    }
    # Left score
    frame:
        xoffset scorePos["left"][0]
        yoffset scorePos["left"][1]
        background Color(colour.transparent)
        text "{0}".format(left):
            font font["name"]
            size font["size"]
    # Draw the right score
    frame:
        xoffset scorePos["right"][0]
        yoffset scorePos["right"][1]
        background Color(colour.transparent)
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
screen pong_object(x, y, width, height, colour="#ffffff", icon=None):
    frame:
        style "tight_icon_wrap" 
        xoffset (x - width/2.0)
        yoffset (y - height/2.0)
        xsize width
        ysize height
        # if there is an icon, use it instead of bg 
        if icon:
            imagebutton:
                xsize width
                ysize height
                idle Frame(icon)
        else:
            background Color(colour)

style tight_icon_wrap:
    ymaximum 50