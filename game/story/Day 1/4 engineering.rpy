label eng1p1:
    $ autosave()
    "I should probably be heading to the next period then."
    scene bg workshop
    with dissolve
    $ playmusic("CongressNeptune.ogg", loop=True)
    show yang normal
    wil "\"Heil Hitler\""
    sze "\"...\""
    sze "My apologies if you are German and the German thought police arrest you"
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
    gra "\"And we will {b}not{/b} be playing with vices\""
    gra "\"What does a plane do?\""
    menu:
        "What does a plane do?"
        "\"It flies\"":
            sze "\"Planes fly through the air\""
            sze "\"Wings can make lift because of air\""
            gra "\"Excellent answer, mr sze\""
            gra "\"Mingle around children, let us achieve band 6's together\""
            hide grant normal
            show yang normal
            wil "\"Nice arthur, so smart, rank double 1 out of 11\""
            hide yang normal
            $ sze.intellect += 1
            $ kok.friendship += 1
            wil "\"Perhaps you may have a use after all\""
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
            wil "\"U must be thirst as fuck to be thinking of water all day\""
            $ sze.thirst += 1
            wil "\"U deserve to die\""
            sze "\"Actually hydroplanes do kinda swim\""
            wil "\"Fuck you, I'm unfriending you\""
            $ kok.friendship -= 1
            wil "\"I swear this engineering class is so dropkick\""
            wil "\"Im rank 1 but i feel im still only going to get a 99 ATAR\""
            wil "\"actual RIP ATAR\""
            hide yang normal
            $ sze.intellect -= 1
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
            $ playsfx("vpunch.ogg")
            gra "\"Aaaaah\"" with vpunch
            gra "\"STOP PLAYING WITH THE VICES\""
            gra "\"You're in trouble\""
            sze "\"FUCK\""
            gra "\"GO STAND IN THE NAUGHTY CORNER\""
            jump eng1p1naughtycorner

label eng1p1naughtycorner:
    scene bg workshop
    hide grant normal
    show pragash normal
    pra "\"...\""
    pra "\"You here as well? At least you weren't put here for every Engi lesson...\""
    sze "\"What? How\""
    $ stopmusic()
    $ playmusic("TheRoomOSTMainTheme.ogg")
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
    $ sze.intellect -= 1
    pra "\"In fact, the mass of the retardedness of this corner is such that it enhances Earth's warping of the space-time continuum\""
    sze "\"Wot\""
    $ sze.intellect -= 1
    pra "\"The massiveness of the retardedness of this corner draws you further into the retardedness\""
    sze "\"Wot\""
    $ sze.intellect -= 1
    pra "\"In fact, this corner seems to allow for, not just the interaction with past light from Minkowski's spacetime cones\""
    sze "\"Wot\""
    $ sze.intellect -= 1
    pra "\"It allows one to interact with the past light, to in fact, redo one's actions\""
    sze "\"Wot\""
    $ sze.intellect -= 1
    pra "\"However, unlike Harry Potter's time turner, instead of being simultaneously present with your previous self, you literally replace your previous self\""
    sze "\"Wot\""
    $ sze.intellect -= 1
    pra "\"Even at this distance, somehow, the mass of retardedness must be emitting some undiscovered form of radiation, spreading its influence\""
    sze "\"Wot\""
    $ sze.intellect -= 1
    pra "\"Over time, I have adapted to this anomalous curvature in spacetime by studying economics and meditating\""
    sze "\"Wot\""
    $ sze.intellect -= 1
    pra "\"But this process takes many years of being in the corner\""
    sze "\"Wot\""
    $ sze.intellect -= 1
    pra "\"So, you are more likely to just become retarded and dropkick here\""
    sze "\"ok\""
    gra "\"Bitches, do your work!!!!\""
    pra "\"Don't listen to him, the corner needs you.\""
    gra "\"Aaaah, that's right: you two children in the naughty-corner, do nothing as punishment\""
    pra "\"The school's fate and yours are entwined, like a changing magnetic field and a changing electric field\""
    menu:
        "Should I stay in the naughty corner?"
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
                    "You feel like you are dying because of the retardedness"
                    scene bg ded
                    with dissolve
                    "The retardedness stab you like a dozen knife"
                    if game.timeTravelCounter >= 4:
                        scene bg black
                        "Yet again you step inside the corner, but this time it feels different"
                        "...It feels"
                        "...wrong"
                        $ playmusic("VarienThroneOfRavens.ogg")
                        "You wake up in bed next to...someone"
                        sze "\"Urgh, mornings are shit\""
                        $ playsfx("hpunch.ogg")
                        sze "\"Wait what\"" with hpunch
                        $ playsfx("vpunch.ogg")
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
                        scene bg dream
                        "This place looks pretty neat, but no oxygen"
                        "Eoarchaen Era Earth is retardedly unsuitable for human life"
                        jump dead
                    elif game.timeTravelCounter >= 3:
                        "Yet again you step inside the corner"
                        "By now you are used to it, no longer disturbed by its seemingly illogical content"
                        "But in the distance you hear a voice calling to you"
                        gra "\"Arthur, stop this madness...\""
                        gra "\"You are damaging the integrity of the world system\""
                        gra "\"Soon time and space will merge, and the multiple timelines of this world will collapse into one\""
                        gra "\"Aaaaah, we're all in trouble\""
                        "his voices fades into the distance as you start to awaken"
                        $ game.timeTravelCounter += 1
                        jump timetravel1
                    elif game.timeTravelCounter >= 1:
                        "You enter further into the familiar corner and repeat the process again"
                        $ game.timeTravelCounter += 1
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
                        $ game.timeTravelCounter += 1
                        jump timetravel1
                "Escape while you still can":
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
            $ playmusic("VarienThroneOfRavens.ogg")
            dea "\"Wtf? It's at the end of the period\""
            sze "Wow, after that I feel so retarded and loading dock"
            sze "Wow, I thikn I ded becuz of rtrdednesszes"
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
    wil "\"You would make a leader as part of my fourth reich, a possible replacement for Moxham\""
    wil "\"Together we can purge the world of non-Band 6 students and similar unwashed masses\""
    sze "\"lol, what a joke\""
    wil "\"Yes...indeed what a joke\""
    sze "\"k.....\""
    wil "\"Although it would be interesting if we could replace Moxham with a student...\""
    dea "\"Oh me, pick me!\""
    sze "\"lol Dean?\""
    dea "\"Wut, i forget why i wanted to picked for something, lulz\""
    "Will glares at Dean until he leaves"
    dea "\"Uhhh yea, I might just go now and stuff, gud luck have fun or something\""
    jump eng1p1p3

label eng1p1p2:
    # answers wrong
    show yang normal
    wil "\"Unfortunate, i had thought you to be smarter.\""
    wil "\"Under my Fourth Reich's eugenics program you shall be one of the first to be removed\""
    sze "\"You're joking right?\""
    wil "\"Only one way to find out\""
    wil "\"MWAHAHAHAHAHAHAHAHAHAHHA!!\""
    sze "\"You had two consecutive Hs in your laugh, therefore that was just a joke\""
    wil "\"Ur a faggot; if I already unfriended you, I'll friend you just to unfriend you again\""
    $ wil.friendship -= 1
    sze "\"You are weird\""
    sze "\"I think sir is trying to say something\""
    jump eng1p2

label eng1p1p3:
    #doesnt talk
    show yang normal
    wil "\"Dean Hou is a dissapointment\""
    wil "\"Dean is a mess\""
    wil "\"When I achieve the Fourth Reich, Dean shall be processed under the eugenics program\""
    wil "\"Or perhaps he shall serve as the basis of a soylent green prototype\""
    wil "\"We cannot tolerate any non Band 6 students\""
    menu yangrant1:
        "Err..."
        "\"Heil the Fourth Reich!\"":
            jump yangrantp1_1
        "\"Heil Moxham!\"":
            jump yangrantp1_2
        "\"Indeed\"":
            jump yangrantp1_3

label yangrantp1_1:
    sze "\"Heil the Fourth Reich!\""
    "Yang nods dissmissively"
    wil "\"I need not hear it now: in the future all humanity will be saying it\""
    sze "\"Ok friend, funny joke\""
    wil "\"There is a fine line between friend and tool...\""
    wil "\"Which are you?\""
    sze "\"...\""
    wil "\"I kid, let's continue learning planes\""
    jump eng1p2

label yangrantp1_2:
    sze "\"Heil Moxham!\""
    wil "\"The leader of {s}my Sturmabeteilung{/s} the SRC and P&C is deserving of praise, especially in regards to the art of special methods of investigating\""
    sze "\"Lol, since when did you have a hard on for our principal...?{nw}\""
    wil "\"Silence\""
    wil "\"We must learn to blend in so that we may takeover the SRC/P&C and bring the 4th Reich into fruition\""
    $ sze.fort += 1
    wil "\"The question is... how? hmmmmm\""
    menu:
            "How should we take over the SRC?"
            "\"We pressure Sarah Desney\"":
#   we do have picture of weeb sze don't we?
                sze "\"We pressure Sarah Desney\""
                wil "\"That's a brilliant idea\""
                sze "\"Wow really? Senpai finally noticed me!\""
                wil "\"For an amoebic brained cretinous slime without a sense of political intrigue\""
                $ wil.friendship -= 1
                sze "\"Why is Senpai always so mean to me?\""
                sze "\"Baka-sempai\""
                wil "\"Sze baka-desu\""
                $ wil.friendship -= 1
                wil "\"Be quiet now, I need to learn how to jet engine for strategic bomber development\""
                jump eng1p2
            "\"We vote in Wesley Lai\"":
                $ game.yangRant = True
                sze "\"We vote in Wesley Lai\""
                wil "\"That's retarded\""
                pra "\"That's retarded\""
                wil "\"But... his biggest political rival...now that might work...\""
                sze "\"uh... yeah... that's who I meant\""
                sze "\"Wait, who is he again?\""
                wil "\"Actually somewhat smart\""
                wil "\"But since I thought of that, you still retarded...\""
                gra "\"Now listen here, little children, gather around the front table\""
                sze "\"We should probs, like, go there {nw}\""
                wil "\"Be quiet now, I need to talk to Pragash\""
                jump eng1p2
            "\"Pragash Haran will be the figurehead\"":
                $ game.yangRant = True
                sze "\"Pragash Haran will be the figurehead\""
                wil "\"Hmmmmm....\""
                wil "\"A true stroke of genius, considering he was on the SRC previously\""
                sze "\"...I'm waiting for you to say \"Just Joking\"...\""
                wil "\"Why would I say that? It is a good idea, one for immediate implementation\""
                $ sze.intellect += 1
                wil "\"Perhaps you do have your uses\""
                $ wil.friendship += 1
                "You see Grant waddling to the front"
                gra "\"Now listen here, little children, gather around the front table\""
                sze "\"Yang, what's going on?\""
                wil "\"Be quite now, I need to learn how to jet engine for strategic bomber development\""
                jump eng1p2
    # Note to self: include refined interrogation techniques later on

label yangrantp1_3:
    sze "\"Indeed\""
    wil "\"I am glad to see that we are in agreement\""
    $ wil.friendship += 1
    wil "\"But all this talking is distracting me from my true joy, ENGINEERING!!\""
    wil "\"So without further ado let us learn more engineering\""
    jump eng1p2

label eng1p2:
    show grant normal
    $ playsfx("hpunch.ogg")
    gra "\"AAAHH, MINGLE!!\"" with hpunch
    gra "\"Gather around the front table, children\""
    gra "\"Before we learn about planes, do these worksheets\""
    gra "\"Actually no, do these safety tests on doing work sheets before you can do the worksheets\""
    wil "\"But sir, We still havent learnt about Vapor cones and why the Prandtl–Glauert singularity doesn't {nw}\""
    gra "\"Whats that???\""
    gra "\"If it's not chocolate, I don't want to hear about it\""
    wil "\"But-\""
    gra "\"Do whatever, just hand in these worksheets whenever\""
    menu:
        "Should I do these worksheets?"
        "Do worksheets":
            "You decide to do worksheets"
            "..."
            "Don't put your hand under a drill press"
            "..."
            "Should you tickle a band saw operator?"
            "..."
            sze "\"Sir, I have completed the worksheets\""
            gra "\"Hmmm...\""
            gra "\"You are a good Fortian, now just do whatever you want, so long as it isn't playing with vices\""
            sze "These worksheets are fucking useless"
            sze "A primary school student could easily do this"
            sze "And no one has the right to tell me whether or not I am allowed to play with vices"
            $ sze.fort += 1
            "As you sit down, you see someone at the door"
            menu:
                "*Knock *knock\""
                "Open door":
                    jump engyesdoor
                "Don't open door":
                    jump engnodoor
        "Don't do worksheets":
            sze "Ceebs to worksheet"
            sze "I'll just do maths..."
            dea "\"Whoa, are those maths questions?\""
            dea "\"Aaw shit, they are...you must be good at maths, help me\""
            sze "\"...ok\""
            dea "\"I cannot differentiate this integral properly\""
            "It turned out that the question was a difficult question relating to permutations and combinations"
            $ sze.intellect += 1
            dea "\"shit you smart\""
            "Whilst basking in your glory, you hear knocking on the door"
            menu:
                "*Knock *knock\""
                "Open door":
                    jump engyesdoor
                "Don't open door":
                    jump engnodoor
        "Play with vices":
            "you are unable to contain yourself, your hands inexorably moving towards the vices"
            "with a swift movement, you gracefully turn the handle a half-revolution, the two plates inching closer"
            "your palm glide across its surface, each pore, each bump upon the slick steel surface"
            "you rotate the handle, slowly, feeling the tightening vice plates in your hand"
            "the exhilarating pleasure of the vice consumes you, tears of elation drip down your eyes"
            "you feel the pressure rising, resisting against you, soon to overwhelm you"
            "your mind fades away, replaced only by the words"
            "vice, Vice, VICE"
            $ playsfx("vpunch.ogg")
            gra "\"Aaaaah\"" with vpunch
            gra "\"STOP PLAYING WITH VICES\""
            gra "\"You're in trouble\""
            sze "\"FUCK\""
            gra "\"GO STAND IN THE NAUGHTY CORNER\""
            jump eng1p1naughtycorner

label engyesdoor:
    "You open the door"
    sze "\"Sir, someon-\""
    $ stopmusic()
    $ playmusic("RaxlenSliceBG8bit.ogg")
    $ playsfx("hpunch.ogg")
    dik "\"...\"" with hpunch
    "You find yourself being garotted by earphones"
    dik "\"My apologies, good sir, these machinations, twere not meant for thee.\""
    dik "\"I do pray that thou'st injuries are not grievous and thou grievances are not severe.\""
    sze "\"Gurg... Sir, someone has a message for you\""
    gra "\"Give it to me\""
    gra "\"...yes...indeed\""
    dik "\"Humourous indeed, it seems that our poor fellow, Sir Haran, has yet again been exiled to the Alcove of Degeneracy.\""
    gra "\"He has inappropriate footwear\""
    pra "\"What?!? These are leather shoes\""
    gra "\"Richard, give me the specs of your shoes\""
    dik "\"Very well...Work boots, leather upper, quarter and tongue, all put together by the finest cobbler of Sydney, whom goes by the name Steel Blue\""
    dik "\"Underneath the upper, the toe cap is made of bullet resistant AR500 steel, with 9mm Level IIIA kevlar padding underneath\""
    dik "\"Shoe laces double as garottes with carbide diamond edge to double as file, aglets double as laser and UV light\""
    dik "\"The insole contains an advanced ventilation system for optimum comfort. Both the vulcanised rubber heel and outsole contain compartments\""
    sze "\"...wtf\""
    pra "\"...wtf\""
    gra "\"Now those are leather shoes\""
    dik "\"Once more, I must apologise for my trangressions; If god wills it I'll be sure to right my wongs later on\""
    "Richard left"
    $ stopmusic()
    $ dik.friendship += 1
    gra "\"Turns out that there is assembly today, got message from O'Neill who got message from office because fuck intercom system\""
    jump asszembly1

label engnodoor:
    sze "\"...\""
    sze "\"szeebs\""
    dea "\"I'll get it\""
    "Sudden movement catches your peripheral vision"
    $ playsfx("hpunch.ogg")
    dea "\"Gaaaafuuuuccc\"" with hpunch
    dea "\"heeelllllppppp\""
    $ stopmusic()
    $ playmusic("RaxlenSliceBG8bit.ogg")
    dik "\"Fool! T'is is a rookie mistake to leave ones backside exposed.\""
    dik "\"Fortunately for thou, I am on an errand, with an urgent message for Sir Grant.\""
    "Richard left {cps=*1.5}leaving Dean cowering on the ground moaning in feverish pitch and Derek has a booboo{/cps}"
    $ stopmusic()
    dea "\"...fuck u arthur, ur a coward\""
    $ sze.strength -= 1
    sze "\"What did I do?\""
    dea "\"nuthing\""
    $ sze.fort -= 1
    dea "\"Sir, message for you\""
    gra "\"k\""
    gra "\"Turns out that there is assembly today, got message from O'Neill who got message from office because fuck intercom system\""
    jump asszembly1
