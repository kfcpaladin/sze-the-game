# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image bg school = "Fort_Street_High_School_Memorial_Hall.JPG"
image bg physclass = "physclass"
image bg principaldoor = "principalofficedoor"
image bg principaloffice = "principaloffice"
image bg workshop = "Workshop.jpg"
image bg hall = "hall"
image bg hallentrance = "CZ2Yss_UAAAPRqz"
image bg schoolfront = "91_big.jpg"
# Declare characters used by this game.
define sze = Character('Sze', color="#FCFCFC", image="arthur")
define rin = Character('Rina', color="#007408", image="serena")
define kok = Character('Willis', color="#666666", image="willis")
define flu = Character('FLUITSMA', color="#FFFFFF", image="fluitsma")
define rus = Character('Rusali', color="#FFFFFF", image="rusali")
define pra = Character('Pragash', color="#FFFFFF", image="pragash")
define dea = Character('Dean', color="#FFFFFF", image="dean")
define wil = Character('Will Yang', color="#FFFFFF", image="yang")
define cha = Character('Chao', color="#FFFFFF", image="chao")
define mox = Character('MOXHAM', color="#FFFFFF", image="moxham")
define gra = Character('GRANT', color="#FFFFFF", image="grant")
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
    $ inteltutorial = False
    $ thirst = 0
    $ fort = 0
    $ friendshiptutorial = False
    $ charmtutorial = False
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

    scene black
    # remove this these things to enable music later
    play music "Deemo - Paper Plane's Adventure - from YouTube.mp3" loop
    "The Year is 2015"
    "It is the first day of school and you do not look forward to another miserable year of Fort Street."
    "But nevertheless, you pack your bags, and get ready, resigned to another year of mediocrity."
    sze "I had always loved her, since she first graced my eyes in Year 7."
    sze "Her name is Serena, a name which evokes images of clear, running brooks and endless fields of wildflower meadows"
    sze "Or perhaps it conjures an image of quaint Parisian cafes at night"
    sze "beside a rose garden in fragrant bloom, with the moon and stars out in full and Mascagni's Cavalleria Rusticana: Intermezzo of Act 1"
    sze "But for now, her name wrings out nought but sadness. More sadness than another year of school"
    jump schoolday1
    
label schoolday1:
    scene bg school
    with fade
    sze "I arrived at school 3 hours early to show my dedication to the system"
    sze "One day she will notice"
    #btw, the day is probably wednesday or tuesday because first day back
    show moxham happy
    with dissolve
    mox "\"Wow, you are a good Fortian\""
    mox "\"I don't know who you are but, you are like next Michael Kirby\""
    hide moxham happy
    call fortiangain from _schoolday1fortiangain
    "3 hours later"
    "Got a new timetable"
    "I have Physics (Flujtsma), Engineering (Grant), English (Schlam), Extension Maths (Barton), Chem (Webb), Eco (Chapman)"
    scene bg school
    with fade
    sze "My life feels empty without her, like a photoelectric cell without UV rays"
    sze "I watch her from afar, but I doubt she notices arthur"
    sze "I see her, walking towards the classroom"
    menu stealwillisgirl:
        "Go talk to her":
            $ stealwillisgirl=True
        "Ignore her, and continue walking to your next class":
            $ stealwillisgirl=False

label TheKwokappears:
    if stealwillisgirl is True:
        show willis normal
        with dissolve
        kok "\"Were you tryna steal my girl just then\""
        "Oh shit, its Willis. He would be furious if he found out i wanted to steal his girl"
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
        sze "Oh dear, its willis. He is currently in a relationship with serena, but i will win her in the end."
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
    "You enter the classroom, and glance around. It seems that there is only 1 seat left, right next to willis"
    "To your left is Willis, to your right is Pragash"
    "You spot Serena sitting at the front of the class right in front the teacher"
    show willis normal
    kok "\"We should be quiet, looks like class is starting soon.\""
    hide willis normal
    flu "\"Take your syllabuses out\""
    dea "\"We have not received syllables yet\""
    flu "\"Syllabuses\""
    dea "\"Ok, man, if you say so\""
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
            sze "\"actually want to kill myself\""
            cha "\"Mental health is a serious issue among male youths\""
            jump phy1p3p3
        "No":
            sze "\"no, pls dont kill me\""
            cha "\"Dissappointing\""
            cha "\"You will be a great entree in my new restaurant\""
            jump dead
    
label phys1p2p3:
    "You do nothing"
    flu "\"Why are there paper balls in front of you\""
    $ phys1p2p1t = False
    $ phys1p2p3t = True
    call phys1p2p4 from _call_phys1p2p4_1
    if phys1p2p4t is True:
        flu "\"CHAO, go stand in the naughty corner\""
        cha "\"Fuck you, arthur\""
        flu "\"As for you Arthur. If Chao ever tries to distract you again, report it immediately\""
        jump phys1p3p1
    else:
        flu "\"Both of you go to the principles office, NOW\""
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
    if moxcounter2 is > 1:
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
        jump eng1p1
        
label phys1p3principal3:
    # said yes
    mox "\"I hope that this is the end of the matter\""
    mox "\"Go to your next period, here's a note excusing your lateness.\""
    mox "\"Now scram\""
    hide moxham unhappy
    show rusali
    rus "\"WAOW, this is my first detention.\""
    rus "\"How will i ever ace trials with a detention\""
    rus "\"I can no longer spend my afternoon doing tutoring and writing textbooks\""
    call rusfriendshiploss from _phys1p3principal3rusfriendshiploss
    jump eng1p1
    
label phys1p3principal4:
    # said no
    mox "\"Show some respect young man\""
    mox "\"For that i am upgrading your punishment to 2 afterschool detentions\""
    mox "\"You are literally 1 centimetre from getting expelled\""
    mox "\"And DCR, i had expected better of a student wanting ace trials\""
    call dailymoxcounter from _phys1p3principal4dailymoxcounter
    hide moxham unhappy
    show rusali
    rus "\"FUARR, my trials can no longer be aced\""
    rus "\"I'll have to become a drop kick, or worse, go to the loading dock\""
    sze "\"Calm down trials are still 1.5 years away\""
    rus "\"Why do i always get roasted\""
    jump eng1p1
    
label eng1p1:
    "I should probably be heading to the next period then."
    scene bg workshop
    with dissolve
    play music "Edith Piaf - Non, Je ne regrette rien - from YouTube.mp3" loop
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
            jump eng1p1p3
        "Play with vices":
            "you are unable to contain yourself, your hands inexorably moving towards the vices"
            "with a swift movement, you gracefully turn the handle a half-revolution, the two plates inching closer"
            "your palm glide across its surface, each pore, each bump upon the steel surface"
            "you rotate the handle, slowly, feeling the tightening vice plates upon your hand"
            "the exhilarating pleasure of the vice consumes you, tears of elation drip down your eyes"
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
    play music "rusaliloadingdockHeyYallGotCigaretteBombsAwayRemix.mp3"
        #Can this be done in 20 seconds?
    sze "\"Uh, Grant put me here\""
    pra "\"Oi, this is my spot\""
    pra "\"Do you have a puff\""
    sze "\"You what?!?!?!?!?!?!?!?!?!?!?!\""
    pra "\"Do you have a ciggy\""
    sze "\"You smoke?!?!?!?!?!?!?!?!?!?!?!\""
    pra "\"Hey yall got a cigarette?\""
    sze "\"Um, I don't smoke\""
    pra "\"Fuck off\""
    jump dead
        
label eng1p1p1:
    # answer correctly, All dat foreshadowing
    show yang normal
    wil "\"You would make a leader as part of my fourth reich\""
    wil "\"Together we can purge the world of jews and non-Band 6 students\""
    sze "\"lol, what a joke\""
    wil "\"Yes...indeed what a joke\""
    sze "\"k.....\""
    jump dead
    
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
    sze "\"I think we have assembly next\""
    jump dead
    
label eng1p1p3:
    #doesnt talk
    show yang normal
    wil "\"Dean Hou is a dissapointment\""
    wil "\"Dean is a mess\""
    wil "\"When achieve he Fourth Reich, dean shall be processed under the eugenics program\""
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
    jump dead
    
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
                wil "\"Now, shut the fuck up, I need to learn engines. I'm only rank 1 in this class, need to get better...\""
            "\"We vote in Wesley Lai\"":
                sze "\"We vote in Wesley Lai\""
                wil "\"That's retarded\""
                pra "\"That's retarded\""
                wil "\"But... his biggest political rival...\""
                sze "\"uh... yeah... that's who I meant\""
                wil "\"Actually somewhat smart\""
                wil "\"But since I thought of that, you still retarded\""
            "\"Pragash Haran will be the figurehead\"":
                
    wil "\"Hush now, I need to learn how to jet engine for strategic bomber development\""
    jump dead
    # Note to self: include refined interrogation techniques later on

label yangrantp1_3p:
    sze "\"Indeed\""
    wil "\"I am glad to see that we are in agreement\""
    call wilfriendshipgain from _yangrantp1_3wilfriendshipgain
    wil "\"Now for assembly time\""
    jump dead
    
# sze "\"Need to go assembly\""
#    scene bg hallentrance
#    with fade
#   "Chao is blocking me from szeing anyone"
#    scene bg hall
#    with fade
#    "Gaudeamus igitur..."
#    mox "\"I would like to acknowledge the traditional owners of the land...\""
#    "30 minutes later"
#    mox "\"Michael Kirby is great, let us worship Michael Kirby\""
#    "40 minutes later"
#    mox "\"It's ok if half the previous year's Year 12 got band 4, Fortians are the epitome of social justice and exit profile\""
#    mox "\"Quoting some Latin 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Pedicabo ego vos et irrumabo.'
#        There is more to high school than ATAR\""
#    "20 minutes later"
#    sze "..."
#    sze "..."
#    "Everyone is leaving, better wake up"
#    Yang-kor Wat -> Yang's Ministry of Public Relations (e.g. Yang's Church of Yangology)
label dead:
    scene black
    sze "I dead"
    return
