##############################################################################
screen kms:
    modal True
    default totalSuicides = 2
    default randomIndex = renpy.random.randint(0, totalSuicides-1) 
    if randomIndex == 0:
        use kmsGun
    elif randomIndex == 1:
        use kmsHanging
    else:
        use kmsGun
    textbutton "{i}Don't kms{/i}":
        xalign 0.9
        yalign 0.1
        action [
            Hide("kms"),
            Function(deleteList, bullets),
        ]
    
##############################################################################
# All suicide scenes
screen kmsGun(bullets=bullets):
    modal True
    add loadImage("kms_bg_bedroom.png")
    # positions
    default pos = Vector(200, 200)
    default size = Vector(200, 300)
    default gunSize = Vector(200, 150)
    default bulletSpeed = 100
    default bulletSize = 20
    default szeDead = False
    # arthur
    imagebutton:
        idle Frame(loadImage("char_arthurside.png"))
        xsize size.x
        ysize size.y
        xoffset pos.x
        yoffset pos.y
    # gun
    $ mousePos = getMousePosition()
    $ mousePos.add(gunSize.getMult(-1/3.0))
    imagebutton:
        idle Frame(loadImage("kms_icon_glockNoTrigger.png"))
        xsize gunSize.x
        ysize gunSize.y
        xoffset mousePos.x
        yoffset mousePos.y
        action [
            Function(bullets.append, Bullet(pos=Vector(mousePos.x, mousePos.y+30), vel=Vector(-bulletSpeed, 0), size=Vector(bulletSize, bulletSize))),
            Function(playsfx, "gunSound.ogg"),
        ]
        hovered [
            Function(playsfx, "gunClick.ogg"),
        ]
    # bullets
    if not szeDead:
        for bullet in bullets:
            $ bullet.update()
            use pong_object(bullet.pos.x, bullet.pos.y, bullet.size.x, bullet.size.y, icon=loadImage("icon_rina.png"))
            if bullet.checkCollide(pos, size):
                $ szeDead = True
        $ bullets[:] = [bullet for bullet in bullets if bullet.checkBounds(Vector(1366, 768))]
    # separate timers
    if szeDead:
        timer 0.05:
            repeat False
            action [
                Function(deleteList, bullets),
                Hide("screen_game_loop"),
                Hide("kmsGun", Fade(2.5, 0.0, 1.0)),
                Show("deathFade"),
                Function(playsfx, "vpunch.ogg"),
                Function(game.gain, "suicideCount", 1),
            ]
    else:
        # update gun position if sze not dead
        timer 0.05:
            repeat True
            action [
                SetScreenVariable("mousePos", None),
            ]


init python:
    class Bullet:
        def __init__(self, pos=Vector(0, 0), vel=Vector(0, 0), size=Vector(10, 10)):
            self.create(pos, vel, size)
        
        def create(self, pos, vel, size):
            self.pos = pos
            self.vel = vel
            self.size = size
        
        def update(self, dt=1.0):
            self.pos.add(self.vel.getMult(dt))

        def checkBounds(self, bounds):
            if((self.pos.x < 0 or self.pos.x+self.size.x > bounds.x) or
               (self.pos.y < 0 or self.pos.y+self.size.y > bounds.y)):
                return False
            else:
                return True

        def checkCollide(self, targetPos, targetSize):
            if((self.pos.x > targetPos.x and self.pos.x+self.size.x < targetPos.x+targetSize.x)
                and (self.pos.y > targetPos.y and self.pos.y+self.size.y < targetPos.y+targetSize.y)):
                return True
            else:
                return False
    
    def deleteList(fullList):
        del fullList[:]
    bullets = []

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
            Function(game.gain, "suicideCount", 1),
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

    
