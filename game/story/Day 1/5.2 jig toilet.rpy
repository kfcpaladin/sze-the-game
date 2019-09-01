label asszemblyjigolokindagaytoilet:
    scene bg toilet
    with fade
    sze "\"Looks like we're here\""
    $ sze.thirst += 1
    jit "\"...\""
    $ stopmusic()
    $ playmusic("TheRoomOSTMainTheme.ogg", loop=True)
    jit "\"Bruh, you just {b}had{/b} to pick the shiftiest place in school\""
    sze "\"stfu, you couldn't think of anywhere better\""
    sze "How is this place so dodgy"
    jit "\"Mate, I swear the toilets aren't meant to be this creepy...\""
    "You seem to hear a sound coming from the stall at the very end"
    menu:
        "\"Investigate the sound\"":
                if jit.friendship >= 4:
                    sze "\"Oi Gary, back me up\""
                    jit "\"Nah mate, that's a bit disturbing\""
                    sze "\"C'mon, think of this as budget urbex\""
                    jit "\"...It's the frigging school toilet tho\""
                    jit "\"Fine\""
                    jump szemeettheleatgaytoilet
                else:
                    sze "\"Oi, Jitian back me up, yeah?\""
                    jit "\"Nah mate, that's some fucking creepy shit going on there...\""
                    sze "\"But-\""
                    jit "\"But two guys in the same cubicle is pretty gay, even without butt-stuff\""
                    sze "\"Fine then\""
                    jit "\"If you wanna check it out, check it out yourself\""
                    sze "\"...\""
                    sze "\"Szeebs\""
                    jit "\"Pussies aren't meant to be in men's toilets, you know?\""
                    $ sze.strength -= 1
                    jit "\"So what now?\""
                    jump toiletstudies1
        "\"Study\"":
            jump toiletstudies1

label toiletstudies1:
    sze "\"I guess I'll just try to be diligent Fortian and study...\""
    $ sze.fort += 1
    jit "\"wtf, actually?\""
    "You go to cubicle as far away from disturbing sound as possible and first textbook you could find"
    $ sze.intellect += 1
    jit "\"wow, you're making me feel bad, I bring great dishonour to my famirii\""
    jit "\"Now what? This was worst idea ever\""
    $ jit.friendship -= 1
    "You ignore Jitian until recess arrives"
    jump recess1a

label szemeettheleatgaytoilet:
    "You cautiously walk towards the sound, faintly coming from behind the cubicle door"
    "You look behind you and notice Jitian raise an eyebrow"
    "With sweaty palms, you slowly push open the door, enduring the squeal of the rusted hinges"
    sze "..."
    jit "\"...\""
    jit "\"wtf...\""
    show le calculetor
    sze "\"what the actual fuck???\""
    ale "\"I am Anthony of the CalcuLetor\""
    ale "\"I am, in fact, an afterimage of the, I guess, real Anthony Le\""
    jit "\"wtf is going on?\""
    ale "\"Well, the real me was so advanced in accelerated maths that his skill surpassed physical limitations\""
    ale "\"I am, essentially, a form of Cherenkov radiation, which animated this calculator with one touch\""
    jit "\"whoa whoa whoa, wait. That doesn't make sense; Cherenkov Radiation should be blue and only happens in {nw}"
    show pragash normal
    with fade
    pra "\"It is\""
    jit "\"I don't think I should've bought the white powder from Winson...\""
    sze "\"What's going on?\""
    hide pragash normal
    with fade
    ale "\"He is another afterimage, caused by his economics and cricket skill.\""
    jit "\"But he isn't in any accelerated course, like you\""
    ale "\"His mastery of the distortion in the Naughty Corner has allowed him to leave afterimages\""
    jit "\"Alright mate alright\""
    ale "\"You must not allow anyone else to know of this\""
    jit "\"I've already forgotten everything\""
    ale "\"I may sze you around then\""
    hide le calculetor
    with fade
    sze "\"That was fucking trippy\""
    jit "\"What was?\""
    sze "\"Anthony Le in a calculetor\""
    jit "\"What? You high mate?\""
    jit "\"Anthony Le in a calculator? Funny joke\""
    sze "..."
    jit "\"Mate, let's get out of this one cubicle, cos no homo\""
    sze "It seems only I remember this now"
    jump recess1a
