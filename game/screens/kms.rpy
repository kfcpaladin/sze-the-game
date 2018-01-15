##############################################################################
screen kms:
    add "bedroom.jpg"
    imagebutton:
        idle Frame("arthurside.png")
        xsize 200
        ysize 300
        xoffset 200
        yoffset 200
    imagebutton:
        idle Frame("glockNoTrigger.png")
        xsize 200
        ysize 150
        xoffset 600
        yoffset 300
        action [
            Function(playsfx, "gunSound.ogg"),
            Hide("kms", Fade(2.5,0.0,1.0)),
            Show("gunDeath"),
        ],
        hovered [
            Function(playsfx, "gunClick.ogg"),
        ]

screen gunDeath(delay=2.5):
    timer delay:
        action [
            Start("deadrestart")
        ]

    
