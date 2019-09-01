label postrollcall1:
    $ autosave()
    scene bg school
    sze "I watch her from afar, but I doubt she notices arthur"
    sze "I see her, walking towards the classroom"
    scene bg classdoor
    with fade
    menu stealwillisgirl:
        "Should I go talk to her?"
        "Go talk to her":
            $ game.stealWillisGirl = True
        "Ignore her, and continue walking to your next class":
            $ game.stealWillisGirl = False
label TheKwokappears:
    if game.stealWillisGirl is True:
        $ sze.thirst += 1
        show willis normal
        with dissolve
        sze "Oh dear, its Willis Lau Kwok. He is currently in a relationship with serena, but i will win her in the end."
        kok "\"Were you tryna steal my girl just then\""
        menu stealwillisgirl2:
            "Oh shit, he would be furious if he found out i wanted to steal his girl"
            "\"No, i was just going to ask her what next period is\"":
                jump Lyingsze
            "\"Yea, so what??\"":
                jump Honestsze
            "\"I was just going to talk to Rusali; he's trying to talk to her\"":
                jump Rektrusali

    else:
        show willis normal
        with dissolve
        kok "\"Ayy, if it aint my old buddy Arthur.\""
        kok "\"I aint seen you in a while, what you been up to lately\""
        sze "Oh dear, its Willis Lau Kwok. He is currently in a relationship with serena, but i will win her in the end."
        sze "\"U-Uh nothing in particular.. umm, Just been study and yeah...\""
        kok "\"Well we should be going to next period soon, wouldnt want Fluitsma to get mad\""
        sze "\"Yea, lets go\""
        jump phys1
label Lyingsze:
        sze "\"N-No, I w-wwas going to ask her what n-next period is\""
        $ playmusic("VarienThroneOfRavens.ogg")
        $ playsfx("vpunch.ogg")
        kok "\"cool story bro\"" with vpunch
        $ playsfx("vpunch.ogg")
        kok "\"suck my dick\"" with vpunch
        $ playsfx("vpunch.ogg")
        kok "\"I'll wreck you\"" with vpunch
        hide willis normal
        with dissolve
        jump dead
label Honestsze:
        sze "\"Yea, so what\""
        $ playmusic("VarienThroneOfRavens.ogg")
        $ playsfx("vpunch.ogg")
        kok "\"so imma fuck you up\"" with vpunch
        $ playsfx("vpunch.ogg")
        kok "\"Die motherfucker\"" with vpunch
        hide willis normal
        with dissolve
        jump dead
label Rektrusali:
        sze "\"I was just going to talk to new kid Rusali, who's trying to talk to her\""
        sze "Dennis C. Rusali is new kid and try to be friend to everyone. Why I dog him?"
        $ playmusic("VarienThroneOfRavens.ogg")
        $ playsfx("vpunch.ogg")
        kok "\"Hah, funny joke mate, go suck a dick\"" with vpunch
        sze "\"Argh... no really look\""
        kok "\"Shit you're right\""
        kok "\"Oi Rusali ur fcking ded bro\""
        hide willis normal
        with dissolve
        show rusali normal
        with dissolve
        rus "\"Waah I was just asking her if she was part of HSPAS\""
        hide rusali normal
        with dissolve
        show willis normal
        with dissolve
        $ playsfx("vpunch.ogg")
        kok "\"Sure bro, let's see how long u last before i make you tell teh truth.\"" with vpunch
        hide willis normal
        show rusali normal
        rus "\"Plz stop\""
        hide rusali normal
        show willis normal
        $ playsfx("vpunch.ogg")
        kok "\"Nah brah\"" with vpunch
        hide willis normal
        show rusali normal
        $ playsfx("vpunch.ogg")
        rus "\"Waah\"" with hpunch
        hide rusali normal
        show willis normal
        $ playsfx("vpunch.ogg")
        kok "\"u wot m8, trying to hit meh!?!\"" with vpunch
        $ playsfx("vpunch.ogg")
        kok "\"git rekt m8, gg ez kill\"" with vpunch
        $ playsfx("vpunch.ogg")
        kok "\"lol imma get gaz to re-educate you with 1000 years of pain after im done\"" with vpunch
        $ playsfx("vpunch.ogg")
        kok "\"thanks arthur\"" with vpunch
        hide willis normal
        show rusali normal
        rus "\"waow arthur, why you do this?\""
        $ playsfx("hpunch.ogg")
        rus "\"just watch me\"" with hpunch
        hide rusali normal
        show willis normal
        kok "\"ow\""
        $ playsfx("vpunch.ogg")
        kok "\"jks lol weak, more weak than lemon to face\"" with vpunch
        hide willis normal
        show rusali normal
        $ playsfx("hpunch.ogg")
        rus "\"waow just watch me\"" with hpunch
        hide rusali normal
        show willis normal
        kok "\"Weak\""
        hide willis normal
        show rusali normal
        $ playsfx("hpunch.ogg")
        rus "\"Screw you guys. I'm going home\"" with hpunch
        hide rusali normal
        show moxham unhappy
        mox "\"Well, well, well, what have we here?\""
        mox "\"You little fucks better not be fighting in this school\""
        mox "\"The expression of violence is a very un-Fortian method of ejaculating your suppressed emotions\""
        hide moxham unhappy
        show willis normal
        kok "\"Dennis Rusali was attacking me\""
        kok "\"He was being dog and not very Fortian\""
        hide willis normal
        show moxham unhappy
        mox "\"One morning in this school and you are being loading dock?\""
        "You fail to understand the meaning of loading dock"
        mox "\"Bitch, you on detention. And you said you were going to truant? Double detention after school in my dungeon\""
        mox "\"Put that shit down in your diary\""
        hide moxham unhappy
        show rusali normal
        rus "\"Faaaaar\""
        rus "\"What did I do\""
        hide rusali normal
        show moxham unhappy
        mox "\"Make that triple detention in my dungeon\""
        mox "\"And you there, bitch standing by being bystander.\""
        sze "\"What did I do?\""
        mox "\"Nothing, which makes you almost as bad a shit as Rusali.\""
        sze "\"ok...\""
        mox "\"I've got my eyes on you, ya hear? punks...\""
        $ game.moxCounter += 1
        hide moxham unhappy
        with dissolve
        show rusali normal
        with dissolve
        rus "\"Waow Arthur, I was gonna hate you but you're a nice guy\""
        hide rusali normal
        $ playmusic("DeemoPaper Plane's Adventure.ogg", loop=True)
        show willis normal
        with dissolve
        kok "\"Nice one, let's go physics with flujtsma, don't want her to go psychotic\""
        sze "\"K\""
        $ kok.friendship += 1
        jump phys1
