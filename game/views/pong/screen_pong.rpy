# give dialog for the pong game
init python:
    _score = 0
    _surrender = False

label playPong(pong=pong):
    menu:
        "Play pong":
            $ _previousMusic = getMusicHistory(-1)
            $ playmusic("VarienThroneOfRavens.ogg")
            $ controller = PongViewController(pong)
            call screen_pong(controller)
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
                    $ sze.strength += 5
                elif _score < 0:
                    "You lose miserably by [_score] points"
                    "Perhaps it is time you killed yourself"
                    "{b}Tip: {/b}Press kms to commit suicide"
                    $ sze.strength -= 2
                else:
                    "You tied with your opponent"
                    "Perhaps this is time for a truce"
                    $ sze.strength += 1
            $ playmusic(_previousMusic)
            return
        "Pass":
            "You pussy out"
            return

# run the pong game
label screen_pong(controller):
    hide screen float_menu
    python:
        ui.add(controller)
        score = ui.interact()
    show screen float_menu
    return score
    

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