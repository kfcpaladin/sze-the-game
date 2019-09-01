label phys1:
    $ autosave()
    scene bg physclass
    $ stopmusic()
    $ playmusic("PinkFloydAnotherBrickInTheWall.ogg", loop=True)
    "You enter the classroom, and glance around. It seems that there is only 1 seat left, right next to willis"
    "To your left is Willis, to your right is Pragash"
    "You spot Serena sitting at the front of the class right in front the teacher, Ms. Fluitsma"
    show willis normal
    kok "\"We should be quiet, looks like class is starting soon.\""
    kok "\"Just kidding, as if anyone actually cares.\""
    hide willis normal
    flu "\"Take your syllabuses out\""
    dea "\"We have not received syllables yet\""
    flu "\"Syllabuses\""
    dea "\"Ok, man, if you say so\""
    sze "Dean's intelligence is inconsistent and primarily revolves around Halo"
    flu "\"Oh crap, I didn't give you syllabuses yet\""
    flu "\"Ok then, let's do something else\""
    flu "\"Since it's the first lesson of year 11, I think we should start in the middle of a currently unrelated topic\""
    flu "\"Can someone explain what a superconductor is?\""
    flu "\"I know it's a year 12 topic and you kids are in year 11, but does anyone know?\""
    menu:
        "What is a superconductor?"
        "\"Superconductivity is a phenomenon of exactly zero electrical resistance and expulsion of magnetic flux fields occurring in certain materials when cooled below a characteristic critical temperature.
         It was discovered by Dutch physicist Heike Kamerlingh Onnes on April 8, 1911 in Leiden.
         Like ferromagnetism and atomic spectral lines, superconductivity is a quantum mechanical phenomenon.
         It is characterized by the Meissner effect, the complete ejection of magnetic field lines from the interior of the superconductor as it transitions into the superconducting state.
         The occurrence of the Meissner effect indicates that superconductivity cannot be understood simply as the idealization of perfect conductivity in classical physics.\"":
            jump phys1answered
        "Do nothing":
            jump phys1nothing
        "Talk to people next to you":
            jump phys1talked
label phys1answered:
    scene bg physclass
    flu "\"Great answer Arthur. It's only the first day and you are already demonstrating why you are rank double one.\""
    "You close Wikipedia"
    flu "\"You should stay after school for some private tutoring ;);)\""
    $ sze.intellect += 1
    menu:
        ";) private tutoring? ;)"
        "Say nothing":
            jump phys1answered_a
        "\"Ok...\"":
            jump phys1answered_b
label phys1answered_a:
    sze "\"...\""
    flu "\"What? No response?\""
    sze "\"...Wot?\""
    flu "\"I bet you go tutoring\""
    $ playmusic("VarienThroneOfRavens.ogg")
    sze "\"...um\""
    $ playsfx("vpunch.ogg")
    flu "\"Stop reading so far ahead its not fair on everyone else\"" with vpunch
    $ playsfx("hpunch.ogg")
    flu "\"In fact I bet you are doing secret tutor-homework right now\"" with hpunch
    sze "\"Wot, Ms-\""
    $ playsfx("vpunch.ogg")
    flu "\"Everyone, kill the heretic\"" with vpunch
    show pragash normal
    pra "\"Sorry Arthur\""
    $ playsfx("hpunch.ogg")
    pra "\"For the watch\"" with hpunch
    pra "\"Ow my hand\""
    hide pragash normal
    show willis normal
    $ playsfx("vpunch.ogg")
    kok "\"For the watch\"" with vpunch
    hide willis normal
    show rusali normal
    $ playsfx("hpunch.ogg")
    rus "\"For the watch\"" with hpunch
    hide rusali normal
    show chao normal
    cha "\"...\""
    sze "\"hunh...\""
    sze "\"...urg...\""
    cha "\"...\""
    sze "\"...Chao..\""
    $ playsfx("vpunch.ogg")
    cha "\"...\"" with vpunch
    cha "\"For teh watch\""
    hide chao normal
    cha "\"Wow, your watch is crap, that wasn't worth the effort\""
    with fade
    jump dead

label phys1answered_b:
    sze "\"ok...\""
    flu "\"Anything you want, anytime...\""
    kok "\"wow sugoi, you are a genius arthur\""
    pra "\"Whoa Arthur, too good\""
    $ flu.friendship += 1
    jump phys1part2

label phys1nothing:
    "The class actually goes quiet"
    "No-one says anything"
    "..."
    "..."
    "suddenly you see a hand being raised at the back of the classroom"
    flu "\"yes?\""
    dea "\"Dude, is it, like, um, when wires are good strong or some shit, man?\""
    "*collective facepalming from the class*"
    flu "\"Not exactly, I think we need to revise the basics\""
    flu "\"Let's start by learning some stuff about the refraction of light\""
    jump phys1part2

label phys1talked:
    "you turn to your right, and start talking to your neighbour, Pragash"
    sze "Pragash is very...cricket and has grand ambitions"
    show pragash normal
    sze "\"How have your holidays been?\""
    pra "\"Pretty good. Been playing cricket daily all summer. Also I did 200 past papers for economics\""
    sze "Wow Pragash is so smart, actually kill myself."
    $ pra.friendship += 1
    "you talk a bit more with Pragash before refocusing like electron beam from electron gun in cathode ray tube\""
    hide pragash normal
    jump phys1part2

label phys1part2:
    scene bg physclass
    "Suddenly a paper ball flies through the air, and hits you in the face from behind..."
    cha "\"Oh, shit. Meant to hit rusali with it\""
    sze "Chao is {s}fat{/s} a rather large individual with a larger appetite"
    menu:
        "What should I do with the paper ball?"
        "Throw it at rusali":
            jump phys1p2p1
        "Throw it at Chao":
            jump phys1p2p2
        "Do nothing":
            jump phys1p2p3

label phys1p2p1:
    show rusali normal
    with dissolve
    rus "\"gotta ace trials ... gotta ace trials ... gotta ace trials\""
    $ playsfx("vpunch.ogg")
    "You pick up the paper and throw it at rusali" with vpunch
    rus "\"Waow, what was that for.\""
    $ rus.friendship -= 1
    $ rus.friendship += 1
    "He picks up the paper, and readies himself to through it back"
    flu "\"Stop throwing paper.\""
    rus "\"Waa, it wasnt me, arthur threw it first\""
    hide rusali normal
    $ _phys1p2p1t = True
    $ _phys1p2p3t = False
    call phys1p2p4
    if _phys1p2p4t is True:
        $ stopmusic()
        $ playmusic("p4LikeADreamComeTrue.ogg", loop=True)
        sze "\"I'm just observing the parabolic motion of a projectile with a specific focus on the horizontal component of motion\""
        sze "\"However, I had failed to take into account the effects of air resistance, which is outside of the syllabus\""
        rus "\"I was helping Arthur\""
        flu "\"I'm very proud of both of you for physically applying your theoretical physics knowledge.\""
        "Pragash and Willis gaze in awe at your remarkable talent in the art of lying"
        "You notice that you may have caught the fleeting interest of Serena"
        $ sze.intellect += 1
        show willis normal
        kok "\"Teach me senpai\""
        hide willis normal
        pra "\"I will forever be your pupil\""
        cha "\"Niiiiice, two birds with one ball\""
        jump phys1p3p2
    else:
        flu "\"Both of you go to the principal's office, NOW!\""
        jump phys1p3principal1

label phys1p2p2:
    scene bg physclass
    $ playmusic("VarienThroneOfRavens.ogg")
    "you pick up the paper and throw it at chao"
    cha "\"WHAT THE HELL. DO YOU WANNA DIE M8\""
    menu:
        "Do I wanna die m8?"
        "\"Yes\"":
            sze "\"Yes\""
            sze "\"actually want to kill myself\""
            if sze.intellect >1:
                cha "\"Arthur Sze, i deeply care about your mental health.\""
                cha "\"If you are having issues concering suicide please call Lifeline at 13 11 14\""
                jump phys1p3p3
            else:
                cha "\"Wow, I actually don't want to eat depressed people - they upset my tummy\""
                sze "\"So we good?\""
                cha "\"No, I still fcking h8 u.\""
                jump phys1p3p1
        "\"No\"":
            sze "\"No\""
            sze "\"no, pls dont kill me\""
            cha "\"Fuck you\""
            $ playsfx("vpunch.ogg")
            cha "\"I'll eat you for lunch!\"" with vpunch
            jump dead
        "\"Ummmm...\"":
            sze "\"Ummm...lolwut?\""
            cha "\"I'll take that as a {nw}\""
            sze "\"Lemme think\""
            jump phys1p2p3

label phys1p2p3:
    "You do nothing"
    flu "\"Why are there paper balls in front of you\""
    $ _phys1p2p1t = False
    $ _phys1p2p3t = True
    call phys1p2p4
    if _phys1p2p4t is True:
        sze "\"...\""
        dea "\"Chao threw it at Arthur\""
        sze "\"He had assaulted my body\""
        flu "\"CHAO, go stand in the naughty corner\""
        cha "\"Fuck you, arthur\""
        cha "\"Fuck you, dean\""
        flu "\"As for you Arthur, if Chao ever tries to distract you again, report it immediately\""
        jump phys1p3p1
    else:
        sze "\"...\""
        dea "\"It was all Chao's fault\""
        flu "\"Both of you should stop playing around\""
        sze "\"But-\""
        $ playsfx("hpunch.ogg")
        flu "\"Both of you go to the principles office, NOW\"" with hpunch
        sze "\"Wow Chao\""
        jump phys1p3principal2

label phys1p2p4:
    menu:
        "Why are there paper balls in front of me?"
        "Use your physics knowledge to make a believable lie" if sze.intellect > 0:
            sze "\"I was merely testing out the validity of the projectile motion formulas.\""
            flu "\"Fair enough, my number 1 student wouldnt never throw papers\""
            $ _phys1p2p4t = True
            return
        "Tell the truth":
            if _phys1p2p1t is True:
                sze "\"Someone threw a paper ball at my head and in retaliation I threw it back\""
                $ _phys1p2p4t = False
                return
            else:
                sze "\"A piece of paper was thrown at my head, in an vicious and inexcusable attack. The perpetrator, Chao must be punished\""
                $ _phys1p2p4t = True
                $ cha.friendship -= 1
                return
        "Say nothing":
            sze "\"...\""
            flu "\"Well?\""
            sze "\"These paper balls magically appeared in front of me\""
            sze "\"I blame Dean\""
            flu "\"There is more to this...\""
            $ _phys1p2p4t = False
            return
label phys1p3p1:
    #Chao in trouble, you good
    "The class continues without any further issues"
    "You feel like you learnt a lot this lesson"
    "the secrets of superconductors have been revealed"
    $ sze.intellect += 1
    "As you start to leave class ..."
    cha "\"I won't forget this ..."
    $ game.chaoPissed = True
    $ cha.friendship -= 1
    show willis normal
    kok "\"Isn't annoying chao the most fun thing to do.\""
    kok "\"It seems we have a lot in common\""
    hide willis normal
    $ kok.friendship += 1
    jump eng1p1

label phys1p3p2:
    #No-one in trouble
    "The class continues without any further issues"
    "You feel like you learnt a lot this lesson"
    "the secrets of superconductors have been revealed"
    $ sze.intellect += 1
    show rusali normal
    rus "\"Thanks for not reporting me, my ATAR wouldve been dead if i got a detention\""
    hide rusali normal
    $ rus.friendship += 1
    jump eng1p1

label phys1p3p3:
    #No-one in trouble
    "The class continues without any further issues"
    "You feel like you learnt a lot this lesson"
    "the secrets of superconductors have been revealed"
    $ sze.intellect += 1
    jump eng1p1
