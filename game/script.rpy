# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image bg school = "Fort_Street_High_School_Memorial_Hall.JPG"
image bg physclass = "physclass"
image bg principaldoor = "principal office door"
image bg principaloffice = "principal office"
image bg workshop = "Workshop.jpg"
image bg hall = "hall"
image bg hallentrance = "CZ2Yss_UAAAPRqz"
# Declare characters used by this game.
define sze = Character('Sze', color="#FCFCFC", image="arthur")
define rin = Character('Rina', color="#007408", image="serena")
define kok = Character('Willis', color="#666666", image="willis")
define flu = Character('FLUITSMA', color="#FFFFFF", image="fluitsma")
define rus = Character('Rusali', color="#FFFFFF", image="rusali")
define pra = Character('Pragash', color="#FFFFFF", image="pragash")
define dea = Character('Dean', color="#FFFFFF", image="dean")
define wil = Character('Will Yang', color="#FFFFFF", image="will")
define cha = Character('Chao', color="#FFFFFF", image="chao")
define mox = Character('MOXHAM', color="#FFFFFF", image="moxham")
define gra = Character('GRANT', color="#FFFFFF", image="grant")
style window:
    left_padding 150
image side arthur ="arthur see through.png"
image willis normal = "willis1.png"
image side willis = "willisside1"
image rusali normal = "rusali"
image moxham happy = "moxham happy"
image moxham unhappy = "moxham unhappy"
image side moxham = "moxhamside"
image grant normal = "grant"
# The game starts here.

label start:
    scene black
    # remove this these things to enable music later
    # play music "Nasheed-Saleel_Al_Sawarim.mp3"
    "The Year is 2016"
    "It is the first day of school and you do not look forward to another miserable year of Fort Street."
    "But nevertheless, you pack your bags, and get ready, resigned to another year of mediocrity."
    sze "I had always loved her, since she first graced my eyes in Year 7."
    
    scene bg school
    with fade
    sze "My life feels empty without her, like a photoelectric cell without UV rays"
    sze "I watch her from afar, but I doubt she notices arthur"
    sze "I see her, walking towards the library"
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
            "I was just going to talk to Rusali; he's trying to talk to her"
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
        kok "\"cool story bro\"" with vpunch
        kok "\"suck my dick\"" with vpunch
        kok "\"I'll wreck you\"" with vpunch
        hide willis normal
        with dissolve
        jump dead
label Honestsze:
        sze "\"Yea, so what\""
        kok "\"so imma fuck you up\"" with vpunch
        kok "\"Die motherfucker\"" with vpunch
        hide willis normal
        with dissolve
        jump dead
label Rektrusali
        sze "\I was just going to talk to Rusali, who's trying to talk to her\""
        kok "\Hah, funny joke mate, go suck a dick\"" with vpunch
        sze "\Argh... no really look\""
        kok "\Shit you're right\""
        kok "\Oi Rusali ur fcking ded bro\""
        hide willis normal
        with dissolve
        show rusali normal
        with dissolve
        rus "\Waah I was just asking how to ace trials\""
        hide rusali normal
        with dissolve
        show willis normal
        with dissolve
        kok "\Sure bro, let's see how long u last before i make you tell teh truth.\"" with vpunch
        hide willis normal
        show rusali normal
        rus "\Plz stop\""
        hide rusali normal
        show willis normal
        kok "\Nah brah\"" with vpunch
        hide willis normal
        show rusali normal
        rus "\Waah\"" with vpunch
        hide rusali normal
        show willis normal
        kok "\u wot m8, trying to hit meh!?!\"" with vpunch
        kok "\git rekt m8, gg ez kill\"" with vpunch
        kok "\lol imma get gaz to re-educate you with 1000 years of pain after im done\"" with vpunch
        kok "\thanks arthur\"" with vpunch
        hide willis normal
        show rusali normal
        rus "\waow arthur, why you do this?\""
        rus "\just watch me\"" with vpunch 
        hide rusali normal
        show willis normal
        kok "\ow\""
        kok "\jks lol weak, more weak than lemon to face\"" with vpunch
        hide willis normal
        show rusali normal
        rus "\waow just watch me\"" with vpunch
        hide rusali normal
        show willis normal
        kok "\Weak\""
        hide willis normal
        show rusali normal
        rus "\Screw you guys. I'm going home\""
        hide rusali normal
        show willis normal
        mox "\Well, well, well, what have we here?\""
        kok "\Dennis Rusali was attacking me\""
        mox "\One year in this school and you are being loading dock?\""
        mox "\Bitch, you on detention. And you said you were going to truant? Double detention after school in my dungeon\""
        rus "\Faaaaar\""
        mox "\Make that triple\""
        call rusfriendshiploss from _call_rusfriendshiploss
        rus "\Waow Arthur\""
        show willis normal
        with dissolve
        kok "\Nice one, let's go physics with flujtsma, don't want her to go psychotic\""
        sze "\K\""
        jump phys1
label phys1:
    scene bg physclass
    "You enter the classroom, and glance around. It seems that there is only 1 seat left, right next to willis"
    "To your left is Willis, to your right is Pragash"
    "You spot Serena sitting at the front of the class right in front the teacher"
    show willis normal
    kok "\"We should be quiet, looks like class is starting soon.\""
    hide willis normal
    flu "\"Since it's the first lesson, I think we showed start right in the midst of the topic\""
    flu "\"Can someone explain what a superconductor is?\""
    flu "\"Anyone?\""
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
    call intelincrease from _call_intelincrease
    kok "\"wow sugoi, you are a genius arthur\""
    jump phys1part2
    
label phys1nothing:
    "No-one says anything"
    "..."
    "..."
    "suddenly you see a hand being raised at the back of the classroom"
    flu "\"yes?\""
    dea "\"Is it, like dude, when wires are really strong or something\""
    "*collective facepalming from the class*"
    flu "\"Not exactly, I think we need to revise the basics\""
    jump phys1part2
    
label phys1talked:
    "you turn to your right, and start talking to your neighbour, Pragash"
    sze "\"How has your holidays been?\""
    pra "\"Pretty good. Been playing cricket daily all summer. Also i did 200 past papers for economics\""
    sze "Wow, this guy is diligent"
    call prafriendshipincrease from _call_prafriendshipincrease
    jump phys1part2
    
label phys1part2:
    scene bg physclass
    "Suddenly a paper ball flies through the air, and hits you in the face"
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
    call rusfriendshiploss from _call_rusfriendshiploss
    call chafriendshipgain from _call_chafriendshipgain
    "He picks up the paper, and readies himself to through it back"
    flu "\"Stop throwing paper.\""
    rus "\"Waa, it wasnt me, arthur threw it first\""
    hide rusali normal
    $ phys1p2p1t = True
    $ phys1p2p3t = False
    call phys1p2p4 from _call_phys1p2p4
    if phys1p2p4t is True:
        flu "\"I'm very proud of both of you for physically applying your theoretical physics knowledge.\""
        "Pragash and Willis gaze in awe at your remarkable talent at lying"
        call intelincrease from _call_intelincrease_1
        show willis normal
        kok "\"Teach me senpai\""
        hide willis normal
        pra "\"I will forever be your pupil\""
        jump phys1p3p2
    else:
        flu "\"Both of you go to the principles office, NOW\""
        jump phys1p3principal1
        
label phys1p2p2:
    "you pick up the paper and throw it at chao"
    cha "\"WHAT THE HELL. DO YOU WANNA DIE M8\""
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
                call chafriendshiploss from _call_chafriendshiploss
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
    call intelincrease from _call_intelincrease_2
    "As you start to leave class ..."
    cha "\"I won't forget this ..."
    call chafriendshiploss from _call_chafriendshiploss_1
    show willis normal
    kok "\"Isn't annoying chao the most fun thing to do.\""
    kok "\"It seems we have a lot in common\""
    hide willis normal
    call kokfriendshipgain from _call_kokfriendshipgain
    jump eng1p1
label phys1p3p2:
    #No-one in trouble
    "The class continues without any further issues"
    "You feel like you learnt a lot this lesson"
    "the secrets of superconductors have been revealed"
    call intelincrease from _call_intelincrease_3
    show rusali normal
    rus "\"Thanks for not reporting me, my ATAR wouldve been dead if i got a detention\""
    hide rusali normal
    call rusfriendshipgain from _call_rusfriendshipgain
    jump eng1p1
label phys1p3principal1:
    #You and rusali
    scene bg principaldoor
    rus "\"Oh no, ive never had a detention before.\""
    "He adopts a praying position"
    rus "\"Jesus please absolve me of my sins\""
    sze "\"Religion is a lie\""
    sze "\"Science is the truth\""
    "It seems that rusali does not appreciate this comment of yours"
    call rusfriendshiploss from _call_rusfriendshiploss_1
    scene bg principaloffice
    show moxham unhappy
    mox "\"I've been told of two boys who were displaying unsatisfactory behaviour in class\""
    mox "\"In this school we have a no tolerance policy on throwing paper balls\""
    mox "\"Do you understand\""
    menu:
        "\"Yes\"":
            jump phys1p3principal3
        "\"No\"":
            jump phys1p3principal4
    jump eng1p1
label phys1p3principal2:
    #You and Chao
    scene bg principaldoor
    cha "\"Fuck, i cant go to an afternoon detention, i have to slay my gfs after school\""
    sze "\"Wow, how do you slay so many LG's\""
    cha "\"You just do\""
    call charmincrease from _call_charmincrease
    scene bg principaloffice
    show moxham unhappy
    mox "\"I've been told of two boys who were displaying unsatisfactory behaviour in class\""
    mox "\"Especially you Joshua, you have a history of being drop kick\""
    mox "\"This behaviour is intolerable at Fort Street High School\""
    mox "\"You two are lucky you arent expelled\""
    jump eng1p1
label eng1p1:
    "I should probably be heading to the next period then."
    wil "\"Ayy, sup arthur\""
    wil "\"U keen for engineering m8\""
    sze "\"uhh, not really\""
    wil "\"I love engineering, i think about constructing planes and bridges every day\""
    wil "\"Not a day goes without me thinking up a new bridge design\""
    sze "\"k.\""
    scene bg workshop
    show grant normal
    gra "\"Good morning class. Lets do some engineering.\""
    

        
label dead:
    scene black
    sze "I dead"
    return
