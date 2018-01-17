##############################################################################
screen kms:
    default totalSuicides = 2
    default randomIndex = renpy.random.randint(0, totalSuicides-1) 
    if randomIndex == 0:
        use kmsGun
    elif randomIndex == 1:
        use kmsHanging
    else:
        use kmsGun
    
##############################################################################
# All suicide scenes
screen kmsGun:
    add loadImage("bedroom.jpg")
    imagebutton:
        idle Frame(loadImage("arthurside.png"))
        xsize 200
        ysize 300
        xoffset 200
        yoffset 200
    imagebutton:
        idle Frame(loadImage("glockNoTrigger.png"))
        xsize 200
        ysize 150
        xoffset 600
        yoffset 300
        action [
            Function(playsfx, "gunSound.ogg"),
            Function(game.gain, "suicideCount", 1),
            Hide("kmsGun", Fade(2.5,0.0,1.0)),
            Show("deathFade"),
        ]
        hovered [
            Function(playsfx, "gunClick.ogg"),
        ]

screen kmsHanging:
    add loadImage("hangingSuicide.jpg")
    imagebutton:
        idle Frame(loadImage("arthurside.png"))
        xsize 200
        ysize 300
        xoffset 200
        yoffset 200
        action [
            Function(playsfx, "vpunch.ogg"),
            Function(game.gain, "suicideCount", 1),
            Hide("kmsHanging", Fade(2.5,0.0,1.0)),
            Show("deathFade")
        ]
        hovered [
            Function(playsfx, "mlady.ogg")
        ]

##############################################################################
# fade to black before restarting
screen deathFade(delay=2.5):
    timer delay:
        action [
            Start("deadrestart")
        ]

    
