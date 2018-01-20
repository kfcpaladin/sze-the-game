label schoolday1:
    $ autosave()
    scene bg school
    with fade
    $ game.setTime("morning")
    "Wednesday Morning"
    sze "I arrived at school 3 hours early to show my dedication to the system"
    sze "One day she will notice"
    #btw, the day is probably wednesday or tuesday because first day back
    show moxham happy
    with dissolve
    if game.timeTravelCounter is 1:
        if game.moxCounter > 1:
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
            sze "\"As you can Sze, I'm studying right now\""
            mox "\"Very well\""
            hide moxham unhappy
            jump postrollcall1
    elif game.timeTravelCounter >= 2:
        sze "\"I must avoid Moxham\""
        sze "\"She passes through the quad in 5 minutes, time to hide\""
        sze "\"...\""
        sze "\"I safe now\""
        call postrollcall1
    else:
        "Oh shit, the Principal..."
        mox "\"Wow, you are a good Fortian\""
        mox "\"I don't know who you are but, you are like next Michael Kirby, greatest of Fortians\""
        $ sze.gain("fort")
        mox "\"As a reward, I shall give you this experimental new Fort Street Diary prototype mk.1.RBY.\""
        mox "\"Among its features, it records your subjects, the progress of your interpersonal relationships and academic studies\""
        mox "\"All in a non-invasive system, designed to allow the school to monitor your life, and allows for early intervention with problem students\""
        mox "\"It's so advanced that, by the time it's viable for a school-wide rollout, it'll probably be outdated\""
        sze "\"...\""
        sze "\"But I don't want it\""
        mox "\"It's an offer you can't refuse\""
        mox "\"And if the diary is more than 10m from your person at any time, as regional director of educational shit, I will use my elite B.R.A.S.I. squad to apprehend you\"" 
        sze "\"wtf is B.R.A.S.I.?\""
        mox "\"The {b}B{/b}oard of Studies {b}R{/b}egulatory {b}A{/b}ction {b}S{/b}quad for {b}I{/b}ntervention\""
        mox "\"Good, you are demonstrating the critical and inquiring nature that is expected of all Fortians. I am confidant that my decision to use you as the guinea pig for the diary was a good one\""
        hide moxham happy
        "3 hours later"
        "I arrive at rollcall"
        "But no roll call teacher"
        "Ceebs waiting, I go to office to get timetable"
        "Got a new timetable"
        "I have Physics (Fluitsma), Engineering (Grant), English (Schlam), Extension Maths (Barton), Chem (Webb), Eco (Chapman)"
        scene bg school
        with fade
        sze "My life feels empty without her, like a photoelectric cell without UV rays"
        jump postrollcall1
