label asszemblyjigolokindagaytoilet:
    scene bg toilet
    with fade
    sze "\"Looks like we're here\""
    call thirstgain from _toiletkindagaythereforethirstgained
    jit "\"...\""
    stop music 
    play music "TheRoomOSTMainTheme.mp3" loop
    jit "\"Bruh, you just {b}had{/b} to pick the shiftiest place in school\""
    sze "\"stfu, you couldn't think of anywhere better\""
    sze "How is this place so dodgy"
    jit "\"Mate, I swear the toilets aren't meant to be this creepy...\""
    "You seem to hear a sound coming from the stall at the very end"
    menu:
        "\"Investigate the sound\"":
            sze "\"Oi Gary, back me up, yeah?\""
                if jitfriendship >= 4:
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
                    call strengthloss from _triedtobegaybutfailedstrengthloss
                    jit "\"So what now?\""
                    jump toiletstudies1
        "\"Study\"":
            jump toiletstudies1
            
label toiletstudies1:
    sze "\"I guess I'll just try to be diligent Fortian and study...\""
    call fortiangain from _fortiangainattoiletswhichiskindagay
    jit "\"wtf, actually?\""
    "You go to cubicle as far away from disturbing sound as possible and first textbook you could find"
    call intelgain from _intelgainattoiletswhichiskindagay
    jit "\"wow, you're making me feel bad, I bring great dishonour to my famirii\""
    jit "\"Now what? This was worst idea ever\""
    call jitfriendshiploss from _jitianthinksyourgayinthegaytoilet
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
    jump recess1a
# will finish later cos it's 2am
    pra "\"to be continued...\""
