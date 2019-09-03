##############################################################################
screen kms:
    modal True
    default totalSuicides = 2
    default randomIndex = renpy.random.randint(0, totalSuicides-1) 
    use refreshTimer
    if randomIndex == 0:
        use kmsGun
    elif randomIndex == 1:
        use kmsHanging
    else:
        use kmsGun
    textbutton "{color=[PrimaryColours.WHITE]}{b}{i}Don't kms{/i}{b}{/color}":
        background Solid(themes.default.rainbow)
        xalign 0.84
        yalign 0.1
        action [Hide("kms")]
    
screen kmsHanging:
    modal True
    add loadImage("kms_bg_hangingSuicide.png")
    imagebutton:
        idle Frame(loadImage("char_arthurside.png"))
        xsize 200
        ysize 300
        xoffset 200
        yoffset 200
        action [
            Hide("screen_game_loop"),
            Hide("kmsHanging", Fade(2.5,0.0,1.0)),
            Show("deathFade"),
            Function(playsfx, "vpunch.ogg"),
            Function(game.set, "suicideCount", game.suicideCount + 1),
        ]
        hovered [
            Function(playsfx, "mlady.ogg")
        ]

##############################################################################
# fade to black before restarting
screen deathFade(delay=2.5):
    timer delay:
        action [
            Hide("kms"),
            Hide("deathFade"),
            Jump("deadrestart"),
        ]

    
