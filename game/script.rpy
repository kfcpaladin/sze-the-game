# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image bg intro = "arthur.jpg"
image bg school = "Fort_Street_High_School_Memorial_Hall.JPG"
image bg physclass = "physclass"
image bg principaldoor = "principalofficedoor"
image bg principaloffice = "principaloffice"
image bg workshop = "Workshop.jpg"
image bg hall = "hall"
image bg hallentrance = "CZ2Yss_UAAAPRqz.jpg"
image bg schoolfront = "91_big.jpg"
image bg rowecorridor = "fortrowecorridor.jpg"
# Declare characters used by this game.
define sze = Character('Sze', color="#FCFCFC", image="arthur")
define rin = Character('Rina', color="#007408", image="serena")
define kok = Character('Willis', color="#666666", image="willis")
define flu = Character('FLUITSIE', color="#FFFFFF", image="fluitsma")
define rus = Character('Rusali', color="#FFFFFF", image="rusali")
define pra = Character('Pragash', color="#FFFFFF", image="pragash")
define dea = Character('Dean', color="#FFFFFF", image="dean")
define wil = Character('Will Yang', color="#FFFFFF", image="yang")
define cha = Character('Chao', color="#FFFFFF", image="chao")
define mox = Character('MOXHAM', color="#FFFFFF", image="moxham")
define gra = Character('GRANT', color="#FFFFFF", image="grant")
define dik = Character('Richard', color="#FFFFFF", image="richard")
define drk = Character('Derek', color="#FFFFFF", image="derek")
define jit = Character('Gary', color="#FFFFFF", image="gary")
define lee = Character('Andrew', color="#FFFFFF", image="andrew")
define roy = Character('Roy', color="#FFFFFF", image="roy")
define but = Character('Aradhya', color="#FFFFFF", image="aradhya")
define dng = Character('Steven', color="#FFFFFF", image="steven")
#not sure if that's legit spelling, plz check
style window:
    left_padding 150
image side arthur ="arthurside.png"
image willis normal = "willis1.png"
image side willis = "willisside1"
image rusali normal = "rusali"
image side rusali = "rusali_side.png"
image moxham happy = "moxhamhappy"
image moxham unhappy = "moxhamunhappy"
image side moxham = "moxhamside"
image grant normal = "grant"
image pragash normal = "pragashnormal.png"
image pragash shocked = "pragash2.png"
image yang normal = "yang1.png"
# The game starts here.

label start:
    $ intelligence = 0
    $ moxcounter1 = 0
    $ moxcounter2 = 0
    $ charm = 0
    $ strength = 0
    $ strengthtutorial = False
    $ inteltutorial = False
    $ thirst = 0
    $ fort = 0
    $ friendshiptutorial = False
    $ charmtutorial = False
    $ thirsttutorial = False
    $ forttutorial = False
    $ rinfriendship = 0
    $ kokfriendship = 0
    $ flufriendship = 0
    $ rusfriendship = 3
    $ prafriendship = 0
    $ deafriendship = 0
    $ wilfriendship = 40
    $ chafriendship = 0
    $ grafriendship = 0
    $ moxfriendship = 0
    $ dikfriendship = 0
    $ drkfriendship = 0
    $ jitfriendship = 0
    $ royfriendship = 0
    $ leefriendship = 0
    $ butfriendship = 0
    $ dngfriendship = 0
    $ timetravelcount = 0
    $ phys1p3p1chaopissed = False
    $ yangrant1_2eingutidee = False
    scene black
    with fade
    scene bg intro
    with fade
    # remove this these things to enable music later
    play music "Persona 4 - Traumerei - from YouTube.mp3" loop
    "The Year is 2015"
    "It is the first day of school and you do not look forward to another miserable year of Fort Street."
    "But nevertheless, you pack your bags, and get ready, resigned to another year of mediocrity."
    sze "I had always loved her, since she first graced my eyes in Year 7."
    sze "Her name is Serena, a name which evokes images of clear, running brooks and endless fields of wildflower meadows"
    sze "Or perhaps it conjures an image of quaint Parisian cafes at night"
    sze "beside a rose garden in fragrant bloom, with the moon and stars out in full and Mascagni's Cavalleria Rusticana: Intermezzo of Act 1"
    sze "But for now, her name wrings out nought but sadness. More sadness than another year of school."
    jump schoolday1
    
label schoolday1:
    scene bg school
    with fade
    sze "I arrived at school 3 hours early to show my dedication to the system"
    sze "One day she will notice"
    #btw, the day is probably wednesday or tuesday because first day back
    show moxham happy
    with dissolve
    if timetravelcount is 1:
        if moxcounter2 > 1:
            hide moxham happy
            show moxham unhappy
            mox "\"You!\""
            mox "\"You're already causing trouble, planning on causing trouble a second time?\""
            mox "\"I'll fuck you over\""
            hide moxham unhappy
            jump dead
        else:
            hide moxham happy
            show moxham unhappy
            mox "\"You!\""
            sze "\"Wot?\""
            mox "\"I won't mind you jumping around so long as you aren't being a fuckwit\""
            mox "\"I've got my eye on you\""
            sze "\"...um...\""
            sze "\"...uh\""
            sze "\"I swear I'll be a good boy\""
            sze "\"Sze, I'm studying right now\""
            mox "\"Very well\""
            hide moxham unhappy
            jump postrollcall1
    elif timetravelcount >= 2:
        sze "\"I must avoid Moxham\""
        sze "\"She passes through the quad in 5 minutes, time to hide\""
        sze "\"...\""
        sze "\"I safe now\""
        call postrollcall1
    else:
        "Oh shit, the Principal..."
        mox "\"Wow, you are a good Fortian\""
        mox "\"I don't know who you are but, you are like next Michael Kirby, greatest of Fortians\""
        hide moxham happy
        call fortiangain from _schoolday1fortiangain
        "3 hours later"
        "Got a new timetable"
        "I have Physics (Fluitsma), Engineering (Grant), English (Schlam), Extension Maths (Barton), Chem (Webb), Eco (Chapman)"
        scene bg school
        with fade
        sze "My life feels empty without her, like a photoelectric cell without UV rays"
        jump postrollcall1
    
label postrollcall1:
    sze "I watch her from afar, but I doubt she notices arthur"
    sze "I see her, walking towards the classroom"
    menu stealwillisgirl:
        "Go talk to her":
            $ stealwillisgirl = True
        "Ignore her, and continue walking to your next class":
            $ stealwillisgirl = False

label TheKwokappears:
    if stealwillisgirl is True:
        show willis normal
        with dissolve
        sze "Oh dear, its Willis Lau Kwok. He is currently in a relationship with serena, but i will win her in the end."
        kok "\"Were you tryna steal my girl just then\""
        "Oh shit, he would be furious if he found out i wanted to steal his girl"
        menu stealwillisgirl2:
            "No, i was just going to ask her what next period is":
                jump Lyingsze
            "Yea, so what??":
                jump Honestsze
            "I was just going to talk to Rusali; he's trying to talk to her":
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
        play music "[Dubstep] - Varien - Throne of Ravens [Monstercat Christmas Album] - from YouTube.mp3"
        kok "\"cool story bro\"" with vpunch
        kok "\"suck my dick\"" with vpunch
        kok "\"I'll wreck you\"" with vpunch
        hide willis normal
        with dissolve
        jump dead
label Honestsze:
        sze "\"Yea, so what\""
        play music "[Dubstep] - Varien - Throne of Ravens [Monstercat Christmas Album] - from YouTube.mp3"
        kok "\"so imma fuck you up\"" with vpunch
        kok "\"Die motherfucker\"" with vpunch
        hide willis normal
        with dissolve
        jump dead
label Rektrusali:
        sze "\"I was just going to talk to Rusali, who's trying to talk to her\""
        sze "Dennis C. Rusali is friend to everyone. Why I dog him?"
        play music "[Dubstep] - Varien - Throne of Ravens [Monstercat Christmas Album] - from YouTube.mp3"
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
        kok "\"Sure bro, let's see how long u last before i make you tell teh truth.\"" with vpunch
        hide willis normal
        show rusali normal
        rus "\"Plz stop\""
        hide rusali normal
        show willis normal
        kok "\"Nah brah\"" with vpunch
        hide willis normal
        show rusali normal
        rus "\"Waah\"" with hpunch
        hide rusali normal
        show willis normal
        kok "\"u wot m8, trying to hit meh!?!\"" with vpunch
        kok "\"git rekt m8, gg ez kill\"" with vpunch
        kok "\"lol imma get gaz to re-educate you with 1000 years of pain after im done\"" with vpunch
        kok "\"thanks arthur\"" with vpunch
        hide willis normal
        show rusali normal
        rus "\"waow arthur, why you do this?\""
        rus "\"just watch me\"" with hpunch 
        hide rusali normal
        show willis normal
        kok "\"ow\""
        kok "\"jks lol weak, more weak than lemon to face\"" with vpunch
        hide willis normal
        show rusali normal
        rus "\"waow just watch me\"" with hpunch
        hide rusali normal
        show willis normal
        kok "\"Weak\""
        hide willis normal
        show rusali normal
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
        mox "\"One year in this school and you are being loading dock?\""
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
        call dailymoxcounter from _rektrusalidailymoxcounter
        hide moxham unhappy
        with dissolve
        show rusali normal
        with dissolve
        rus "\"Waow Arthur, I was gonna hate you but you're a nice guy\""
        hide rusali normal
        play music "Deemo - Paper Plane's Adventure - from YouTube.mp3" loop
        show willis normal
        with dissolve
        kok "\"Nice one, let's go physics with flujtsma, don't want her to go psychotic\""
        sze "\"K\""
        call kokfriendshipgain from _Rektrusalikokfriendshipgain
        jump phys1
label phys1:
    scene bg physclass
    stop music
    play music "Los Lobos - La Bamba (HQ,16-9) - from YouTube.mp3" loop
    "You enter the classroom, and glance around. It seems that there is only 1 seat left, right next to willis"
    "To your left is Willis, to your right is Pragash"
    "You spot Serena sitting at the front of the class right in front the teacher, Ms. Fluitsma"
    show willis normal
    kok "\"We should be quiet, looks like class is starting soon.\""
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
    flu "\"You should stay after school for some private tutoring ;);)\""
    call intelgain from _phys1answeredintelgain
    menu:
        "Say nothing":
            jump phys1answered_a
        "Ok...":
            jump phys1answered_b
label phys1answered_a:
    sze "\"...\""
    flu "\"What? No response?\""
    sze "\"...Wot?\""
    flu "\"I bet you go tutoring\""
    play music "[Dubstep] - Varien - Throne of Ravens [Monstercat Christmas Album] - from YouTube.mp3"
    sze "\"...um\""
    flu "\"Stop reading so far ahead its not fair on everyone else\"" with vpunch
    flu "\"In fact I bet you are doing secret tutor-homework right now\"" with hpunch
    sze "\"Wot, Ms-\""
    flu "\"Everyone, kill the heretic\"" with vpunch
    show pragash normal
    pra "\"Sorry Arthur\""
    pra "\"For the watch\"" with hpunch
    pra "\"Ow my hand\""
    hide pragash normal
    show willis normal
    kok "\"For the watch\"" with vpunch
    hide willis normal
    show rusali normal
    rus "\"For the watch\"" with hpunch
    hide rusali normal
    cha "\"...\""
    sze "\"hunh...\""
    sze "\"...urg...\""
    cha "\"...\""
    sze "\"...Chao..\""
    cha "\"...\"" with vpunch
    cha "\"For teh watch\""
    jump dead
label phys1answered_b:
    sze "\"ok...\""
    flu "\"Anything you want, anytime...\""
    kok "\"wow sugoi, you are a genius arthur\""
    pra "\"Whoa Arthur, too good\""
    jump phys1part2
    
label phys1nothing:
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
    call prafriendshipgain from _phys1talkedprafriendshipgain
    "you talk a bit more with Pragash before refocusing like electron beam from electron gun in cathode ray tube\""
    hide pragash normal
    jump phys1part2
    
label phys1part2:
    scene bg physclass
    "Suddenly a paper ball flies through the air, and hits you in the face from behind..."
    cha "\"Oh, shit. Meant to hit rusali with it\""
    sze "Chao is {s}fat{/s} a rather large individual with a larger appetite"
    menu:
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
    "You pick up the paper and throw it at rusali" with vpunch
    rus "\"Waow, what was that for.\""
    call rusfriendshiploss from _phys1p2p1callrusfriendshiploss
    call chafriendshipgain from _phys1p2p1callchafriendshipgain
    "He picks up the paper, and readies himself to through it back"
    flu "\"Stop throwing paper.\""
    rus "\"Waa, it wasnt me, arthur threw it first\""
    hide rusali normal
    $ phys1p2p1t = True
    $ phys1p2p3t = False
    call phys1p2p4 from _phys1p2p1callphys1p2p4
    if phys1p2p4t is True:
        stop music
        play music "Persona 4 - Like A Dream Come True - from YouTube.mp3" loop
        sze "\"I'm just observing the parabolic motion of a projectile with a specific focus on the horizontal component of motion\""
        sze "\"However, I had failed to take into account the effects of air resistance, which is outside of the syllabus\""
        rus "\"I was helping Arthur\""
        flu "\"I'm very proud of both of you for physically applying your theoretical physics knowledge.\""
        "Pragash and Willis gaze in awe at your remarkable talent in the art of lying"
        call intelgain from _phys1p2p1callintelgain
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
    play music "[Dubstep] - Varien - Throne of Ravens [Monstercat Christmas Album] - from YouTube.mp3"
    "you pick up the paper and throw it at chao"
    cha "\"WHAT THE HELL. DO YOU WANNA DIE M8\""
    menu:
        "Yes":
            sze "\"Yes\""
            sze "\"actually want to kill myself\""
            cha "\"Arthur Sze, i deeply care about your mental health.\""
            cha "\"If you are having issues concering suicide please call Lifeline at 13 11 14\""
            jump phys1p3p3
        "No":
            sze "\"No\""
            sze "\"no, pls dont kill me\""
            cha "\"Fuck you\""
            cha "\"I'll eat you for lunch!\"" with vpunch
            jump dead
    
label phys1p2p3:
    "You do nothing"
    flu "\"Why are there paper balls in front of you\""
    $ phys1p2p1t = False
    $ phys1p2p3t = True
    call phys1p2p4 from _call_phys1p2p4_1
    if phys1p2p4t is True:
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
        flu "\"Both of you go to the principles office, NOW\"" with hpunch
        sze "\"Wow Chao\""
        jump phys1p3principal2
        
label phys1p2p4:
    menu:
        "Use your physics knowledge to make a believable lie" if intelligence > 0:
            sze "\"I was merely testing out the validity of the projectile motion formulas.\""
            flu "\"Fair enough, my number 1 student wouldnt never throw papers\""
            $ phys1p2p4t = True
            return
        "Tell the truth":
            if phys1p2p1t is True:
                sze "\"Someone threw a paper ball at my head and in retaliation I threw it back\""
                $ phys1p2p4t = False
                return
            else:
                sze "\"A piece of paper was thrown at my head, in an vicious and inexcusable attack. The perpetrator, Chao must be punished\""
                $ phys1p2p4t = True
                call chafriendshiploss from _phys1p2p4callchafriendshiploss
                return
        "Say nothing":
            sze "\"...\""
            flu "\"Well?\""
            sze "\"These paper balls magically appeared in front of me\""
            sze "\"I blame Dean\""
            flu "\"There is more to this...\""
            $ phys1p2p4t = False
            return
label phys1p3p1:
    #Chao in trouble, you good
    "The class continues without any further issues"
    "You feel like you learnt a lot this lesson"
    "the secrets of superconductors have been revealed"
    call intelgain from _phys1p3p1callintelgain
    "As you start to leave class ..."
    cha "\"I won't forget this ..."
    $ phys1p3p1chaopissed = True
    call chafriendshiploss from _phys1p3p1callchafriendshiploss
    show willis normal
    kok "\"Isn't annoying chao the most fun thing to do.\""
    kok "\"It seems we have a lot in common\""
    hide willis normal
    call kokfriendshipgain from _phys1p3p1callkokfriendshipgain
    jump eng1p1
    
label phys1p3p2:
    #No-one in trouble
    "The class continues without any further issues"
    "You feel like you learnt a lot this lesson"
    "the secrets of superconductors have been revealed"
    call intelgain from _phys1p3p2callintelgain
    show rusali normal
    rus "\"Thanks for not reporting me, my ATAR wouldve been dead if i got a detention\""
    hide rusali normal
    call rusfriendshipgain from _phys1p3p2callrusfriendshipgain
    jump eng1p1
    
label phys1p3p3:
    #No-one in trouble
    "The class continues without any further issues"
    "You feel like you learnt a lot this lesson"
    "the secrets of superconductors have been revealed"
    call intelgain from _phys1p3p2callintelgain
    jump eng1p1    

label phys1p3principal1:
    #You and rusali
    scene bg principaldoor
    rus "\"Oh no, ive never had a detention before.\""
    "He starts muttering in Indonesian"
    rus "\"Better tell my parents otherwise I'll get rekt\""
    sze "\"If you don't tell your parents, wouldn't you get less rekt?\""
    rus "\"Waow, stop roasting me\""
    "It seems that Rusali does not appreciate this comment of yours"
    call rusfriendshiploss from _phys1p3principal1acallrusfriendshiploss
    scene bg principaloffice
    call dailymoxcounter from _phys1p3principal1acalldailymoxcounter
    if moxcounter2 > 1:
        mox "\"You two again?\""
        play music "[Dubstep] - Varien - Throne of Ravens [Monstercat Christmas Album] - from YouTube.mp3"
        mox "\"You're already in my shit books\""
        rus "\"Oh no...\""
        mox "\"I didn't say you could speak\"" with hpunch
        rus "\"Aowwww\""
        sze "\"Oh shit\""
        mox "\"You're both dead\"" with vpunch
        rus "\"Run, ru-\""
        mox "\"I'll clear all your records of loading dockness if you rek Arthur and spend afternoon of re-education with me\""
        show rusali normal
        rus "\Soz man. Need to ace trials\"" with vpunch
        sze "\"faarrrr\""
        jump dead
    else:
        show moxham unhappy
        call dailymoxcounter from _phys1p3principal1bcalldailymoxcounter
        mox "\"I've been told you two have been disrupting the propogation of education by being dropkicks\""
        mox "\"In this school we have a no tolerance policy on throwing balls (except in my dungeon *wink *wink)\""
        mox "\"Do you understand?\""
        menu:
            "\"Yes\"":
                jump phys1p3principal3
            "\"No\"":
                jump phys1p3principal4
label phys1p3principal2:
    #Sze and Chao - David cos Zhichao geddit? no
    scene bg principaldoor
    cha "\"Fuck, i cant go to an afternoon detention, i have to slay my gfs after school\""
    sze "\"Wow, how do you slay so many LG's\""
    cha "\"You just do\""
    call charmgain from _phys1p3principal2callcharmgain
    scene bg principaloffice
    call dailymoxcounter from _phys1p3principal2adailymoxcounter
    if moxcounter2 > 1:
        show moxham unhappy
        mox "\"You again?\""
        play music "[Dubstep] - Varien - Throne of Ravens [Monstercat Christmas Album] - from YouTube.mp3"
        mox "\"Chao, I'll clear you of your dropkickness records if you beat the shit out of him\""
        cha "\"Yes ma'am\""
        sze "\"nope\""
        jump dead
    else:
        show moxham unhappy
        call dailymoxcounter from _phys1p3principal2bdailymoxcounter
        mox "\"I have been told of two boys who were displaying unsatisfactory behaviour in class\""
        mox "\"Especially you Joshua, you have a history of being drop kick\""
        mox "\"This behaviour is intolerable at Fort Street High School\""
        mox "\"You two are lucky you arent expelled\""
        hide moxham unhappy
        jump eng1p1
        
label phys1p3principal3:
    # said yes
    sze "\"Yes\""
    mox "\"I hope that this is the end of the matter\""
    mox "\"Go to your next period, here's a note excusing your lateness.\""
    mox "\"Now scram\""
    hide moxham unhappy
    show rusali
    rus "\"WAOW, this is my first detention.\""
    rus "\"How will i ever ace trials with a detention\""
    rus "\"I can no longer spend my afternoon doing tutoring and writing textbooks\""
    call rusfriendshiploss from _phys1p3principal3rusfriendshiploss
    hide rusali
    jump eng1p1
    
label phys1p3principal4:
    # said no
    sze "\"...No\""
    mox "\"Wow, you must be retarded\""
    mox "\"Our school offers support programs for retarded fucks like you, so i am giving you 2 afterschool detentions for the price of 1.\""
    mox "\"This way you will be exit profile\""
    call fortiangain from _phys1p3princpal4fortiangain
    mox "\"And DCR, i had expected better of a student wanting ace trials\""
    call dailymoxcounter from _phys1p3principal4dailymoxcounter
    hide moxham unhappy
    show rusali
    rus "\"FUARR, my trials can no longer be aced\""
    rus "\"I'll have to become a drop kick, or worse, go to the loading dock\""
    sze "\"Calm down trials are still 1.5 years away\""
    rus "\"Why do i always get roasted\""
    rus "\"Stop roasting me arthur\""
    hide rusali
    jump eng1p1
    
label eng1p1:
    "I should probably be heading to the next period then."
    scene bg workshop
    with dissolve
    play music "Los Lobos - La Bamba (HQ,16-9) - from YouTube.mp3" loop
    show yang normal
    wil "\"Heil hitler\""
    wil "\"Are you ready for engineering?\""
    sze "\"uhh, not really\""
    wil "\"I love engineering, i think about constructing planes and bridges every day\""
    wil "\"Not a day goes without me thinking up a new bridge design\""
    sze "\"k.\""
    sze "\"...when is Grant arriving?\""
    wil "\"He's usually half a lesson late\""
    hide yang normal
    show grant normal
    gra "\"Good morning class. Lets do some engineering.\""
    gra "\"I'm glad all of you made it to class on time\""
    hide grant normal
    show yang normal
    wil "\"That's a new record sir\""
    wil "\"You made it to class only 15min and 27s late\""
    hide yang normal
    gra "\"Thank you all, I would like to dedicate this new record to my friends and family for their continued support and their pies\""
    gra "\"Today we are going to learn about planes\""
    gra "\"What does a plane do?\""
    menu:
        "\"It flies\"":
            sze "\"Planes fly through the air\""
            sze "\"Wings can make lift because of air\""
            gra "\"Excellent answer, mr sze\""
            gra "\"Mingle around children, let us achieve band 6's together\""
            hide grant normal
            show yang normal
            wil "\"Nice arthur, so smart, rank double 1\""
            hide yang normal
            call intelgain from _eng1p2intelgain
            call wilfriendshipgain from _eng1p2wilfriendshipgain
            jump eng1p1p1
        "\"It swims\"":
            sze "\"Everybody knows that planes swim on the water\""
            hide grant normal
            show yang normal
            wil "\"WTF!!!\""
            wil "\"How did 9/11 happen then?\""
            wil "\"Was it all an inside job?\""
            sze "\"The plane swam on the water, and then hit the towers\""
            wil "\"Ur a fckin idiot\""
            wil "\"U deserve to die\""
            play music "[Dubstep] - Varien - Throne of Ravens [Monstercat Christmas Album] - from YouTube.mp3"
            sze "\"Actually hydroplanes do kinda swim\""
            stop music
            wil "\"Fuck you, I'm unfriending you\""
            call wilfriendshiploss from _eng1p2wilfriendshiploss
            wil "\"I swear this engineering class is so dropkick\""
            wil "\"Im rank 1 but i feel im still only going to get a 99.90 ATAR\""
            wil "\"actual RIP ATAR\""
            hide yang normal
            call intelloss from _eng1p2intelloss
            jump eng1p1p2
        "\"...\"":
            dea "\"A plane is like a flat surface.\""
            "*collective facepalming from the class*"
            gra "\"Wrong plane fool\""
            dea "\"Ummm\""
            dea "\"Its like a level of existence or something\""
            gra "\"still wrong\""
            dea "\"Then you must be talking about that woodworking tool, man\""
            gra "\"...I give up on this class\""
            jump eng1p1p3
        "Play with vices":
            "you are unable to contain yourself, your hands inexorably moving towards the vices"
            "with a swift movement, you gracefully turn the handle a half-revolution, the two plates inching closer"
            "your palm glide across its surface, each pore, each bump upon the slick steel surface"
            "you rotate the handle, slowly, feeling the tightening vice plates in your hand"
            "the exhilarating pleasure of the vice consumes you, tears of elation drip down your eyes"
            "you feel the pressure rising, resisting against you, soon to overwhelm you"
            "your mind fades away, replaced only by the words"
            "vice, Vice, VICE"
            gra "\"Aaaaah\""
            gra "\"STOP PLAYING WITH VICES\""
            gra "\"You're in trouble\""
            sze "\"FUCK\""
            gra "\"GO STAND IN THE NAUGHTY CORNER\""
            jump eng1p1naughtycorner
            
label eng1p1naughtycorner:
    hide grant normal
    show pragash normal
    pra "\"...\""
    pra "\"You here as well? At least you weren't put here for life...\""
    sze "\"What? How\""
    stop music
    play music "The Room Soundtrack Main Theme - from YouTube.mp3"
    pra "\"I thought this time I might get the Matrix brain plug for engi or maybe Grant might forgive me...\""
    sze "\"For what?\""
    pra "\"Idk\""
    pra "\"I think it was because I was watching some guy destroy an engineering project, when someone told me to hold a hammer...\""
    pra "\"And then Grant turned around and saw me holding the hammer over the smashed project\""
    sze "\"Oh shit\""
    pra "\"And then he said \"AAAAahhh, you're in trouble, go to the naughty corner for life\"\""
    sze "\"wow\""
    pra "\"Here, in the naughty corner, time behaves differently and space warps\""
    sze "\"Wot\""
    call intelloss from _eng1p1naughtycorneraintelloss
    pra "\"In fact, the mass of the retardedness of this corner is such that it enhances Earth's warping of the space-time continuum\""
    sze "\"Wot\""
    call intelloss from _eng1p1naughtycornereintelloss
    pra "\"The massiveness of the retardedness of this corner draws you further into the retardedness\""
    sze "\"Wot\""
    call intelloss from _eng1p1naughtycornerbintelloss
    pra "\"In fact, this corner seems to allow for, not just the interaction with past light from Minkowski's spacetime cones\""
    sze "\"Wot\""
    call intelloss from _eng1p1naughtycornerfintelloss
    pra "\"It allows one to interact with the past light, to in fact, redo one's actions\""
    sze "\"Wot\""
    call intelloss from _eng1p1naughtycornergintelloss
    pra "\"However, unlike Harry Potter's time turner, instead of being simultaneously present with your previous self, you literally replace your previous self\""
    sze "\"Wot\""
    call intelloss from _eng1p1naughtycornerhintelloss
    pra "\"Even at this distance, somehow, the mass of retardedness must be emitting some undiscovered form of radiation, spreading its influence\""
    sze "\"Wot\""
    call intelloss from _eng1p1naughtycorneriintelloss
    pra "\"Over time, I have adapted to this anomalous curvature in spacetime by studying economics and meditating\""
    sze "\"Wot\""
    call intelloss from _eng1p1naughtycornercintelloss
    pra "\"But this process takes many years of being in the corner\""
    sze "\"Wot\""
    call intelloss from _eng1p1naughtycornerdintelloss 
    pra "\"So, you are more likely to just become retarded and dropkick here\""
    sze "\"ok\""
    gra "\"Bitches, do your work!!!!\""
    pra "\"Don't listen to him, the corner needs you.\""
    gra "\"Oi, that's right: you two naughty-corner grunts, do nothing as punishment\""
    pra "\"The school's fate and yours are entwined, like a changing magnetic field and a changing electric field\""
    menu:
        "Stay in the corner":
            pra "\"Goood\""
            pra "\"Feel the corner's strength overwhelming your feeble mind\""
            pra "\"With the Corner, a day is like a thousand years, and a thousand years are like a day.\""
            sze "\"I finally sze the truth. Time was never linear, in its fractal loop there is no end, there is no beginning\""
            menu:
                #rewrite this stuff as you wish
                "Head deeper into the corner":
                    "You walk a steep closer towards the corner"
                    "The edges of the classroom contort around you,\""
                    "One second ago, Pragash stood merely half a metre behind you"
                    "The next, Pragash was a mile away. Or is he closer...\""
                    if timetravelcount >= 4:
                        scene bg black
                        "Yet again you step inside the corner, but this time it feels different"
                        "...It feels"
                        "...wrong"
                        "You wake up in bed next to...someone"
                        sze "\"Urgh, mornings are shit\""
                        sze "\"Wait what\"" with hpunch
                        sze "\"Wha- what the fuck are you\"" with vpunch
                        sze "\"Huh? You\""
                        sze "\"No, I'm me, you're...\""
                        sze "\"You\""
                        sze "\"No, not me, you\""
                        sze "\"Yes, I am you\""
                        sze "\"Just answer the damn question, who are you?\""
                        sze "\"I have told you\""
                        sze "\"This is retarded, I'm going to go now...\""
                        "The past light cone is warping, you find yourself flashing through time and space to find..."
                        "Wow"
                        "Eoarchaen Era Earth is retardedly unsuitable for human life"
                        jump dead
                    elif timetravelcount >= 3:    
                        "Yet again you step inside the corner"
                        "By now you are used to it, no longer disturbed by its seemingly illogical content"
                        "But in the distance you hear a voice calling to you"
                        gra "\"Arthur, stop this madness...\""
                        gra "\"You are damaging the integrity of the world system\""
                        gra "\"Soon time and space will merge, and the multiple timelines of this world will collapse into one\""
                        gra "\"Aaaaah, we're all in trouble\""
                        "his voices fades into the distance as you start to awaken"
                        $ timetravelcount +=1
                        jump timetravel1
                    elif timetravelcount >= 1:
                        "You enter further into the familiar corner and repeat the process again"
                        $ timetravelcount += 1
                        jump timetravel1
                    else:
                        "You step further into the corner, your body now inches from the wall"
                        "You blink, and the inches now seem like lightyears"
                        "You look back, the aeons old light from an old Earth finally reaching your eyes"
                        "But ahead, your future lays, your 60 ATAR, Serena's rejection of your love, and your eventual suicide"
                        "To your sides, the many paths that could've, should've been"
                        "Acing trials,"
                        "Slaying Serena,"
                        "99.95 ATAR"
                        "Becoming surgical engineering legal financial software adviser"
                        "You start running into the darkness, determined to make good of your short life"
                        "And as you run, you start to lose track of time, of where you are, of who you are"
                        "..."
                        "..."
                        "And then you start to stir from your slumber, the first light of a school morning illuminating your eyes"
                        $ timetravelcount += 1
                        jump timetravel1
                "Escape whilst you still can":
                    "You turn away from the corner, and take a step away from it"
                    "It tries to pull you back in, but you resist your feeble strength barely holding out against its immense pressure"
                    "But slowly you make an advancement, and manage to return to the world of the living"
                    gra "\"So planes have wings, and wings let them fly and you will learn this in a year and a half's time\""
                    "you have never felt this relieved to be in a shitty engineering classroom"
                    jump eng1p2
        "Go to assembly":
            pra "\"How could you?\""
            pra "\"You were the chosen one\""
            pra "\"It was said you would destroy the Grant, not join him\""
            sze "\"...k\""
            "You hurriedly leave, avoiding eye contact with the madman on your way to assembly"
            dea "\"Where you going?\""
            sze "\"Asszembly\""
            dea "\"Wtf? It's at the end of the period\""
            sze "Wow, after that I feel so retarded and loading dock"
            sze "Wow, I thikn I ded becuz of rtrdednesszes"
            #call loadingdockness?
            jump dead
        
label timetravel1:
    hide grant normal
    scene black
    "You wake up in a familiar bed"
    "You check your phone, it's the first day of year 11"
    sze "\"Deja vu\""
    "You pack your bags, munch down your breakfast, ready for another day of school"
    jump schoolday1

label eng1p1p1:
    # answer correctly, All dat foreshadowing
    show yang normal
    wil "\"You would make a leader as part of my fourth reich\""
    wil "\"Together we can purge the world of jews and non-Band 6 students\""
    sze "\"lol, what a joke\""
    wil "\"Yes...indeed what a joke\""
    sze "\"k.....\""
    jump eng1p2
    
label eng1p1p2:
    # answers wrong
    show yang normal
    wil "\"Unfortunate, i had thought you to be smarter.\""
    wil "\"Under my Fourth Reich's eugenics program you shall be one of the first to be removed\""
    sze "\"You're joking right?\""
    wil "\"Only one way to find out\""
    wil "\"MWAHAHAHAHAHAHAHAHAHAHHA!!\""
    sze "\"You had two consecutive Hs in your laugh, therefore that was just a joke\""
    wil "\"Ur a faggot; if I already unfriended you, I'll unfriend you again\""
    call wilfriendshiploss from _eng1p1p2wilfriendshiploss
    sze "\"You are weird\""
    sze "\"I think sir is trying to say something\""
    jump eng1p2
    
label eng1p1p3:
    #doesnt talk
    show yang normal
    wil "\"Dean Hou is a dissapointment\""
    wil "\"Dean is a mess\""
    wil "\"When I achieve the Fourth Reich, dean shall be processed under the eugenics program\""
    wil "\"We cannot tolerate any non Band 6 students\""
    menu yangrant1:
        "Heil the Fourth Reich!":
            jump yangrantp1_1
        "Heil Moxham!":
            jump yangrantp1_2
        "Indeed":
            jump yangrantp1_3

label yangrantp1_1:
    sze "\"Heil the Fourth Reich!\""
    "Yang nods dissmissively"
    wil "\"I need not hear it now: in the future all humanity will be saying it\""
    sze "\"Ok friend\""
    wil "\"There is a fine line between friend and tool...\""
    wil "\"Which are you?\""
    sze "\"...\""
    wil "\"Just joking, let's continue learning planes\""
    jump eng1p2
    
label yangrantp1_2:
    sze "\"Heil Moxham!\""
    wil "The leader of my Sturmabeteilung- I mean the SRC and P&C - is deserving of praise, especially in regards to the art of special methods of questioning\""     
    sze "\"Praise... Akuete\""
    wil "\"We must learn to blend in so that we may takeover the SRC/P&C and bring the 4th Reich into fruition\""
    call fortiangain from _yangrantp1_2fortiangain
    wil "\"The question is... how? hmmmmm\""
    menu:
            "\"We pressure Sarah Desney\"":
                sze "\"We pressure Sarah Desney\""
                wil "\"That's a brilliant idea\""
                sze "\"Wow really? Senpai finally noticed me!\""
                wil "\"For an amoebic brained cretinous slime without a sense of political intrigue\""
                call wilfriendshiploss from _yangrantp1_2op1awilfriendshiploss
                sze "\"Why is Senpai always so mean to me?\""
                sze "\"Baka-senpai\""
                wil "\"Sze baka-desu\""
                call wilfriendshiploss from _yangrantp1_2op1bwilfriendshiploss
                wil "\"Be quite now, I need to learn how to jet engine for strategic bomber development\""
                jump eng1p2
            "\"We vote in Wesley Lai\"":
                $ yangrant1_2eingutidee = True
                sze "\"We vote in Wesley Lai\""
                wil "\"That's retarded\""
                pra "\"That's retarded\""
                wil "\"But... his biggest political rival...now that might work...\""
                sze "\"uh... yeah... that's who I meant\""
                sze "\"Wait, who is he again?\""
                wil "\"Actually somewhat smart\""
                wil "\"But since I thought of that, you still retarded...\""
                gra "\"Now listen here, you little runts, gather around the front table\""
                wil "\"Be quite now, I need to find Pragash\""
                jump eng1p2
            "\"Pragash Haran will be the figurehead\"":
                $ yangrant1_2eingutidee = True
                sze "\"Pragash Haran will be the figurehead\""
                wil "\"Hmmmmm....\""
                wil "\"A true stroke of genius\""
                sze "\"...I'm waiting for you to say \"Just Joking\"...\""
                wil "\"Why would I say that? It is a good idea, one for immediate implementation\""
                call intelgain from _yangrantp1_2op3intelgain
                wil "\"Perhaps you do have your uses\""
                call wilfriendshipgain from _yangrantp1_2op3wilfriendshipgain
                "You see Grant waddling to the front"
                gra "\"Now listen here, you little runts, gather around the front table\""
                sze "\"Yang, what's going on?\""
                wil "\"Be quite now, I need to learn how to jet engine for strategic bomber development\""
                jump eng1p2
    # Note to self: include refined interrogation techniques later on
    
label yangrantp1_3:
    sze "\"Indeed\""
    wil "\"I am glad to see that we are in agreement\""
    call wilfriendshipgain from _yangrantp1_3wilfriendshipgain
    wil "\"But all this talking is distracting me from my true joy, ENGINEERING!!\""
    wil "\"So without further ado let us learn more engineering\""
    jump eng1p2
    
label eng1p2:
    show grant normal
    gra "\"AAAHH, MINGLE!!\"" with hpunch
    gra "\"Gather around the front table, grunts\""
    gra "\"Before we learn about planes, do these worksheets\""
    gra "\"Actually no, do these safety tests on doing work sheets before you can do the worksheets\""
    wil "\"But sir, We still havent learnt about Vapor cones and the Prandtl–Glauert singularity\""
    gra "\"...Whats that???\""
    gra "\"If it's not chocolate, I don't want to hear about it\""
    wil "\"But-\""
    gra "\"Do whatever, just hand in these worksheets whenever\""
    menu:
        "\"Do worksheets\"":
            "You decide to do worksheets"
            "..."
            "..."
            sze "\"Sir, I have completed the worksheets\""
            gra "\"Hmmm...\""
            gra "\"You are good Fortian, now just do whatever you want\""
            sze "These worksheets are fucking useless"
            sze "I learnt all this stuff in primary school"
            call fortiangain from _eng1p2fortiangain
            "As you sit down, you see someone at the door"
            menu:
                "\"Open door\"":
                    "You open the door"
                    sze "\"Sir, someon-\""
                    dik "\"...\"" with hpunch
                    "You find yourself being garotted by earphones"
                    dik "\"Whoops, that was for Dean\""
                    dik "\"Uh... my bad\""
                    sze "\"Gurg... Sir, someone has a message for you\""
                    gra "\"Give it to me\""
                    gra "\"...yes...indeed\""
                    dik "\"Lol, Pragash is still in naughty corner\""
                    gra "\"He has inappropriate footwear\""
                    pra "\"What?!? These are leather shoes\""
                    gra "\"Richard, give me the specs of your shoes\""
                    dik "\"Very well...custom made Steel Blue work boots, leather upper, quarter and tongue\""
                    dik "\"Underneath the upper, the toe cap is made of bullet resistant AR500 steel, with 9mm Level IIIA kevlar padding underneath\""
                    dik "\"Shoe laces double as garottes with carbide diamond edge to double as file, aglets double as laser and UV light\""
                    dik "\"The insole contains an advanced ventilation system for optimum comfort. Both the vulcanised rubber heel and outsole contain compartments\""
                    sze "\"...wtf\""
                    pra "\"...wtf\""
                    gra "\"Now those are leather shoes\""
                    dik "\"Sorry for strangling you earlier, I'll be sure to right my wongs later on\""
                    "Richard left"
                    call dikfriendshipgain from _eng1p2dikfriendshipgain
                    gra "\"Turns out that there is assembly today, got message from O'Neill who got message from office because fuck intercom system\""
                    jump asszembly1
                "\"Don't open door\"":
                    "*Knock *knock\"" 
                    sze "\"...\""
                    sze "\"szeebs\""
                    dea "\"I'll get it\""
                    "Sudden movement catches your peripheral vision"
                    dea "\"Gaaaafuuuuccc\"" with hpunch
                    dea "\"heeelllllppppp\""
                    dik "\"Sorry, you had your back to me...\""
                    dik "\"Message for Mr. Grant\""
                    "Richard {s}is a dick{/s} is a quick-witted {s}bastard{/s} gentleman; etiquette and pron{s}o{/s}unciation are important to him..." 
                    "Richard left {cps=*3}leaving Dean cowering on the ground moaning in feverish pitch{/cps}"
                    dea "\"...fuck u arthur, ur a coward\""
                    call strengthloss from _eng1p2strengthloss
                    sze "\"What did I do?\""
                    dea "\"nuthing\""
                    call fortianloss from _eng1p2fortianloss
                    dea "\"Sir, message for you\""
                    gra "\"k\""
                    gra "\"Turns out that there is assembly today, got message from O'Neill who got message from office because fuck intercom system\""
                    jump asszembly1
        "\"Don't do worksheets\"":
            sze "Ceebs to worksheet"
            sze "I'll just do maths..."
            dea "\"Whoa, are those maths questions?\""
            dea "\"Aaw shit, they are...you must be good at maths, help me\""
            sze "\"...ok\""
            dea "\"I cannot differentiate this integral properly\""
            "It turned out that the question was a difficult question relating to permutations and combinations"
            call intelgain from _eng1p2intelgain
            dea "\"shit you smart\""
            "Whilst basking in your glory, you hear knocking on the door"
            menu:
                "\"Open door\"":
                    "You open the door"
                    sze "\"Sir, someon-\""
                    dik "\"...\"" with hpunch
                    "You find yourself being garotted by earphones"
                    dik "\"Whoops, that was for Dean\""
                    dik "\"Uh... my bad\""
                    sze "\"Gurg... Sir, someone has a message for you\""
                    gra "\"Give it to me\""
                    gra "\"...yes...indeed\""
                    dik "\"Lol, Pragash is still in naughty corner\""
                    gra "\"He has inappropriate footwear\""
                    pra "\"What?!? These are leather shoes\""
                    gra "\"Richard, give me the specs of your shoes\""
                    dik "\"Very well...custom made Steel Blue work boots, leather upper, quarter and tongue\""
                    dik "\"Underneath the upper, the toe cap is made of AR500 steel, with 9mm Level IIIA kevlar padding underneath\""
                    dik "\"Shoe laces double as garottes with carbide diamond edge to double as file, aglets double as laser and UV light\""
                    dik "\"The insole contains an advanced ventilation system for optimum comfort and the vulcanised rubber heel and outsole contain compartments\""
                    sze "\"...wtf\""
                    pra "\"...wtf\""
                    gra "\"Now those are leather shoes\""
                    dik "\"Sorry for strangling you earlier, I'll be sure to right my wongs later on\""
                    "Richard left"
                    call dikfriendshipgain from _eng1p2dikfriendshipgain
                    gra "\"Turns out that there is assembly today, got message from O'Neill who got message from office because fuck intercom system\""
                    jump asszembly1
                "\"Don't open door\"":
                    "*Knock *knock\"" 
                    sze "\"...\""
                    sze "\"szeebs\""
                    dea "\"I'll get it\""
                    "Sudden movement catches your peripheral vision"
                    dea "\"Gaaaafuuuuccc\"" with hpunch
                    dea "\"heeelllllppppp\""
                    dik "\"Sorry, you had your back to me...\""
                    dik "\"Message for Mr. Grant\""
                    "Richard {s}is a dick{/s} is a quick-witted {s}bastard{/s} gentleman; etiquette and pron{s}o{/s}unciation are important to him..."
                    "Richard left {cps=*3}leaving Dean cowering on the ground moaning in feverish pitch and Derek has a booboo{/cps}"
                    dea "\"...fuck u arthur, ur a coward\""
                    call strengthloss from _eng1p2strengthloss
                    sze "\"What did I do?\""
                    dea "\"nuthing\""
                    call fortianloss from _eng1p2fortianloss
                    dea "\"Sir, message for you\""
                    gra "\"k\""
                    gra "\"Turns out that there is assembly today, got message from O'Neill who got message from office because fuck intercom system\""
                    jump asszembly1
        "\"Play with vices\"":
            "you are unable to contain yourself, your hands inexorably moving towards the vices"
            "with a swift movement, you gracefully turn the handle a half-revolution, the two plates inching closer"
            "your palm glide across its surface, each pore, each bump upon the slick steel surface"
            "you rotate the handle, slowly, feeling the tightening vice plates in your hand"
            "the exhilarating pleasure of the vice consumes you, tears of elation drip down your eyes"
            "you feel the pressure rising, resisting against you, soon to overwhelm you"
            "your mind fades away, replaced only by the words"
            "vice, Vice, VICE"
            gra "\"Aaaaah\""
            gra "\"STOP PLAYING WITH VICES\""
            gra "\"You're in trouble\""
            sze "\"FUCK\""
            gra "\"GO STAND IN THE NAUGHTY CORNER\""
            jump eng1p1naughtycorner

label asszembly1:
    stop music
    play music "Persona 3 - Iwatodai Dorm - from YouTube.mp3" loop
    scene bg rowecorridor
    with fade
    sze "\"Time for my first assembly of the year\""
    wil "\"Indeed, I wonder whether Moxham will be here\""
    pra "\"I'm finally free from the Engineering room...\""
    sze "\"Why not drop it?\""
    pra "\"Not just yet... I need to enact my revenge\""
    if yangrant1_2eingutidee is True:
        wil "\"That reminds me, Pragash, I have a proposal of sorts\""
        pra "\"What kind?\""
        wil "\"One that might facilitate for such an enactment of revenge, in return for a minor favour\""
        sze "\"Aaah, yes, indeed\""
        "Yang appreciates the backup, allowing Pragash to hear the proposal for his election onto the SRC"
        call wilfriendshipgain from _asszembly1wilfriendshipgain
        pra "\"Unfortunately, the SRC&PNC hate me, I will need something really hero from a PR team to pull this off\""
        pra "\"Otherwise, I would love to help\""
        wil "\"Hmmm... Arthur, I don't suppose you could be a good friend and help out here...\""
        menu:
            "\"Ok\"":
                sze "\"Ok\""
                pra "\"There's the Fortian spirit\""
                call fortiangain from _asszembly1fortiangain
                wil "\"My plan will come into fruition then\""
                pra "\"I owe much to the two of you then\""
                call prafriendshipgain from _asszembly1prafriendshipgain
                sze "\"np\""
                $ quest1electionpromise = True
                jump asszembly1p1
            "\"I'll pass\"":
                sze "\"I'll pass\""
                pra "\"Wow, what a little shit\""
                call prafriendshiploss from _asszembly1prafriendshiploss
                wil "\"Indeed\""
                call wilfriendshiploss from _asszembly1wilfriendshiploss
                sze "\"Calm down, fine\""
                $ quest1electionpromise = True
                jump asszembly1p1
            "\"Play with vices\"":
                sze "\"I wanna play with vices\""
                wil "\"The fuck you talking about?\""
                sze "\"Nevermind\""
                call intelloss from _asszembly1intelloss
                pra "\"Just do it\""
                sze "\"...\""
                sze "\"fine\""
                $ quest1electionpromise = True
                jump asszembly1p1
    else:
        wil "\"Why would you want to enact revenge upon engineering\""
        wil "\"It is the greatest subject to have ever existed\""
        pra "\"...You will never understand\""
        jump asszembly1p1
        
label asszembly1p1:
    dea "\"Hey guys, looking forward to assembly?\""
    wil "\"It would be un-Fortian to skip it\""
    pra "\"I hear Gary might be...\""
    "The conversation gets you thinking about your options..."
    #wil fuck you derek lol totes 
    #wow calm down wil, plus I wrote it not derk ;)
    menu:
        "\"I need to put some stuff in my locker\"":
            jump asszembly1jigolo
        "\"Lol, actually ceebs skipping asszembly though\"":
            jump asszembly1_2

label asszembly1jigolo:
    sze "\"I need to put some stuff in my locker\""
    wil "\"...\""
    pra "\"Alright, see you at assembly\""
    sze "\"uh...yeah...\""
    dea "\"BYEEEE!!!\""
    "You hurry off back to the Rowe corridor, trying not to look suss"
    scene bg rowecorridor
    jit "\"Who's that?\""
    sze "\"Fuck\""
    menu:
        "\"Run\"":
            "You run to assembly like the chicken that you are"
            sze "{cps=*3}BOk BOk BOk BOk BOk{/cps}{nw}"
            sze "That was a close call"
            call strengthloss from _asszemblyjigolostrengthloss
            jump asszembly1_2
        "\"Sneak up on the source of the sound\"":
            "You sneak up on the source of the sound"
            sze "\"...\""
            jit "\"Whoa, SHIT!\"" with vpunch
            sze "\"Oh, it's just Gary\""
            sze "{cps=*3}Gary/Jitian is a shady, food-smuggling, hentai-watching{/cps} {nw}"
            sze "Gary/Jitian is a great guy with a taste for questionable animes..."
            call jitfriendshiploss from _asszemblyjigolojitfriendshiploss
            jit "\"Can u not, like plz? I thought you were teacher\""
            sze "\"Soz, why you here?\""
            jump asszemblyjigolo2
        "\"You confront the speaker\"":
            "You walk up to the speaker, without attempting to disguise your approach"
            jit "\"Oh, hi Arthur\""
            sze "{cps=*3}Gary/Jitian is a shady, food-smuggling, hentai-watching{/cps} {nw}"
            sze "Gary/Jitian is a great guy with a taste for questionable animes..."
            sze "\"lol, why you so scared?\""
            call strengthgain from _asszemblyjigolostrengthgain
            jit "\"Calm down, mate\""
            jit "\"Shut the fuck up, there might be teachers...\""
            sze "\"Well, I'm planning on ditching\""
            jump asszemblyjigolo1_2
    
label asszembly1_2:
    scene bg hallentrance
    with fade
    sze "\"Lol, actually ceebs skipping asszembly though\""
    call fortiangain from _asszembly1_2fortiangain
    wil "\"You are true Fortian, Moxham would be proud of you\""
    sze "\"Really?\""
    wil "\"No, I don't think she cares\""
    show willis normal
    with dissolve
    kok "\"Arthur, my man!\""
    kok "\"Nice to see you all faggots\""
    kok "\"and Arthur, my friend, my rock, the Chosen One...\""
    sze "\"Eh?\""
    kok "\"the Uberfaggot\""
    sze "\"...\""
    sze "\"...Willis\""
    pra "\"Willis, I thought we were friends, how could you forget me?\""
    kok "\"I haven't\""
    hide willis normal
    with dissolve
    dea "\"Oh hey, fucktard\""
    wil "\"Why you still following us?\""
    dea "\"Looking for Mon and Pang\""
    dea "\"Oh, they're there, cya suckaz\""
    "Dean left"
    dik "\"Greetings and salutations to all and Willy la Willy\""
    kok "\"Fuck you\""
    dik "\"No thank you, I don't swing that way\""
    kok "\"Fuc- never mind\""
    pra "\"Tell you what fucks with the mind? Simple harmonic motio{nw}\""
    wil "\"I'm just revising simple harmonic motion and permutations and combinations\""
    wil "\"Don't worry, they're easy topics, ez 100 in tests\""
    pra "\"Teach me William, show me the way to your greatness...\""
    wil "\"Relax, just do 20,000 tests.\""
    kok "\"Tests? I think Chao should get one of his LGs to do one, make sure- {nw}\""
    cha "\"Fee\"" with vpunch
    cha "\"Fi\"" with vpunch
    cha "\"Fo\"" with vpunch
    cha "\"Fum\"" with vpunch
    cha "\"Imma fuck you up the bum\""
    if phys1p3p1chaopissed is True:
        "Chao is blocking me"
        cha "\"I promised I would have my revenge...\"" with vpunch
        sze "\"Shit\""
        "You try to run but the crowd blocks you and Chao grabs you"
        sze "\"Aarrgh, fuck off, don't touch me\""
        cha "\"Huehue\"" with hpunch
        sze "\"Ow, fuck, my head...\""
        call intelloss from _asszembly1_2chaopisssedintelloss1
        cha "\"Fuck your head? Ok\"" with hpunch
        sze "\"Nooo, raep, raep\""
        if dikfriendship > 0:
            dik "\"Oi, fat ass, pick on people your own size, like Gabe Newell or someone of similar girth\""
            cha "\"Lemme think...\""
            cha "\"Nah...\""
            dik "\"My apologies, then\""
            cha "\"?\""
            dik "\"For {b}this{/b}\"" with hpunch
            cha "\"FUUUUUUCCCCKKKKK, what the shit was that?!?!?!\""
            dik "\"Steel toes, bitch\""
            cha "\"Arrgh, don't make me angry\""
            dik "\"Don't make me make Chao Mein\""
            cha "\"...\""
            cha "\"Fuck off\""
            "You observed how to some combat technique"
            call strengthgain from __asszembly1_2chaopisssedstrengthgain
            jump asszembly1_3
        elif dikfriendship < 1:
            cha "\"I go full frontal\"" with vpunch
            call intelloss from _asszembly1_2chaopisssedintelloss2
            sze "\"Aaah, plz stop\""
            cha "\"Why should I? Beg slave, you know you like it\""
            call intelloss from _asszembly1_2chaopisssedintelloss3
            sze "\"No... No means no\""
            "Chao slams you down onto the ground"
            cha "\"I will ravage you to Chaoder\"" with vpunch
            call intelloss from _asszembly1_2chaopisssedintelloss4
            call intelloss from _asszembly1_2chaopisssedintelloss5
            call intelloss from _asszembly1_2chaopisssedintelloss6
            sze "\"Raep, raep\""
            sze "\"I positively assert that no means no\""
            call strengthloss from _asszembly1_2chaopissedthenraepedyou
            "You faintly hear people shouting at Chao and through your blurred vision you can make out a crowd of people swarming Chao..."
            "The whities have heard you positively asserting yourself against Chao's desecration of your physical form, one is helping you up"
            "They praise the Fortianness of your actions"
            call fortiangain from _asszembly1_2chaopisssedfortiangain
            "You proceed to weakly move your battered and bruised assemblage into asszembly"
            jump asszembly1_3
    else:
        cha "\"Hi\""
        rus "\"Oi, don't roast me\""
        cha "\"Chill, I'm just here to raep Pragga\""
        pra "\"No, fuck off...\""
        "You feel it best not to intervene" with hpunch
        "Despite Pragash's attempts to positively assert himself, the whites call him out for not accepting non-heterosexual practices"
        "They must've really hated him being on the Student Representative Council..."
        cha "\"Let's go in\""
        pra "\"...Nooo...not again\""
        cha "\"I meant the hall...\""
        jump asszembly1_3
label asszembly1_3:
    scene bg hall
    with fade
    "Gaudeamus igitur...something something...venit mors velociter, rapit nos atrociter..."
    mox "\"I would like to acknowledge the traditional owners of the land...\""
    sze "Wow, this is boring"
    menu:
        "\"Sleep\"":
        #derk, leaving this part up to you
            sze "\"I sleep\""
            sze "{i}I dream {/i}"
            sze "{size=+100} {b} {i} {color=#9400D3}C{/color} . {color=#4B0082}O{/color} . {color=#0000FF}L{/color} . {color=#00FF00}O{/color} . {color=#FFFF00}U{/color} . {color=#FF7F00}R{/color} . {color=#FF0000}F{/color} . {color=#ff69b4}U{/color} . {color=#d2691e}L{/color} {/i} {/b} {/size}" with hpunch
            drk "\"I will now finish the rest of this dream sequence later someday when I not ceebs\""
            jump dead
        "\"Talk\"":
            "You turn to talk to Derek and Richard"
            if quest1electionpromise is True:
                pra "\"urgh...\""
                "You are reminded of your quest"
                sze "\"I wonder what it would be like for Pragash to be on the SRC...\""
                dik "\"Wow, that is an interesting idea\""
                dik "\"And retarded at the same time\""
                pra "\"Hey, I heard that\""
                drk "\"Well actually, we could probably make this work. First, identify likely opponents.\""
                sze "{cps=*3}Derkie Derk has high pitch wail like Willy and Chao{/cps}{nw}"
                sze "Derek is {s}a Machiavellian bastard{/s} a intelligent guy {s}whose morals are as fluid as his loyalties{/s}"  
                drk "\"There are many but we focus on getting him a nemesis and then lock on\""
                dik "\"Then spin policy which will get him elected\""
                drk "\"Sigh... you conservatives... Character attacks are the only ways to guarantee election\""
                dik "\"But surely he needs to be able to back up his attacks with something of substance\""
                "You have an epiphany"
                call intelgain from _asszembly1_3intelgain
                sze "\"Maybe, we can get together a campaign team...\""
                pra "\"Is that even necessa-\""
                drk "\"Good idea\""
                sze "\"How about I get a bunch of guys to work with Pragash to figure out policy, so that he can debate\""
                dik "\"First he needs to figure out how to debate...\""
                pra "\"Rap battle\""
                drk "\"Indeed, something which the populace can relate and rally to\""
                drk "\"What will we do?\""
                sze "\"Both of you lead the attack with PR, make Pragash the Vox Populi\""
                dik "\"Yes... and then we cross the Rubicon-er, the bridge from Kilgour to Wilkins building- and force them to flee...\""
                drk "\"Figuratively, of course, yes?\""
                dik "\"errr.....\""
                pra "\"Thanks all of you\""
                call prafriendshipgain from _asszembly1_3quest1prafriendshipgain
                pra "\"By the way, have you heard that Chelsea destroyed ManU last night\""
                dik "\"I was just watching news about that. I thought it was the other way around; the government destroyed the rebels\""
                pra "\"Get your hearing checked\""
                "You should relay this news to William Yang - he is currently engaged in conversation with his hand"
                "You engage in mindless conversation with Richard, Derek and Pragash"
                $ metderek = true
                jump asszembly1_4
            else:
                dik "\"I reckon a 16in High Explosive shell fired from a battleship can destroy the hall\""
                sze "\"Why would that even happen?\""
                "A 16in High Explosive shell fired from a battleship destroyed the hall" with hpunch
                sze "\"Fuck\""
                jump dead
        "\"Pay attention\"":
            "30 minutes later"
            mox "\"Michael Kirby is great, let us worship Michael Kirby\""
            "You worship Michael Kirby, allowing yourself to absorb the power of social justice"
            call fortgain from _asszembly1_3fortgain
            "40 minutes later"
            jump asszembly1_4
label asszembly1_4:
    mox "\"It's ok if half the previous year's Year 12 got band 4, Fortians are the epitome of social justice and exit profile\""
    mox "\"Quoting some Latin 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Pedicabo ego vos et irrumabo. There is more to high school than ATAR\""
    "20 minutes later"
    sze "\"Well that was fucking useless\""
    call fortiangain from _asszembly1_3fortiangain
    wil "\"Pah, talking about helping the community; only I know of what must be done for the greater good\""
    jump recess1
label asszemblyjigolo1_2:
    jit "\"Arrite, so long as you don't be dog, we'll be fine with you here\""
    jit "\"Follow me, and listen, yeh? If u see a teacher, bail yeh.\""
    "You see a couple of other people milling about"
    sze "\"Where are we going?\""
    jit "\"The Rowe Dungeon\""
    sze "\"Fuck, not there! We'll get destroyed by the principal\""
    jit "\"That's not it, son! Y would we use that one? That one's the legendary Cohen Dungeon\""
    jit "\"U must be munted to not know dat\""
    "You follow Gary to Rowe Dungeon"
    sze "\"Why is there shifty BDSM gear hanging on the wall?\""
    jump dead
#    Yang-kor Wat -> Yang's Ministry of Public Relations (e.g. Yang's Church of Yangology)
label recess1:
    if $ metderek is true:
        sze "\"Why does my raw fugu salmon green potato half-smoked beef roll make me feel funny?\""
        jump dead
    else:
        "You go to Rowe Corner"
        sze "I sze Serena... I should talk"
        menu:
            "Talk":
               "You move like a panther, with slick moves and predatory focus"
               "..." with vpunch
               "Until you bump into Richard and Derek"
               drk "\"Watch where you going, fgt\""
               dik "\"Actually it's pronounced \"faggot\"\""
               drk "\"Whatevs\""
               sze "\"Wow soz...geez\""
               sze "Derek is {s}a Machiavellian bastard{/s} a intelligent guy {s}whose morals are as fluid as his loyalties{/s}"
               "You turn around continuing on your hunt for {nw}"
               "Foot + banana peel + concrete = dead"
               jump dead
               
            "Do not talk":
                "You stand on the spot trying to muster up some courage but find it futile"
                sze "{cps=*3}BOk BOk BOk BOk BOk{/cps}{nw}"
                call strengthloss from _recess1chickenstrengthloss
                "You notice you look retarded frozen in mid-stride with your mouth wide open"
                drk "\"Wow, Arthur looks retarded frozen in mid-stride with his mouth wide open\""
                sze "Derek is {s}a Machiavellian bastard{/s} a intelligent guy {s}whose morals are as fluid as his loyalties{/s}"
                sze "\"whaa- can you not...geez\""
                sze "I die of embarassment"
                jump dead
label dead:
    scene black
    sze "I dead"
    return

label deadrestart:
    scene black
    sze "I dead"
    jump start
