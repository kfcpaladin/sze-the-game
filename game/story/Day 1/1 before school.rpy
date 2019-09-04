label schoolday1:
    $ autosave()
    scene bg school
    with fade
    $ clock.set_time("morning")
    "Wednesday Morning"
    sze "I arrived at school 3 hours early to show my dedication to the system"
    sze "Well, more so because I didn't know what else to do, as I couldn't fall asleep after that weird dream"
    sze "But perhaps, maybe this effort will pay off..."
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
        $ sze.fort += 1
        mox "\"As a reward, I shall give you this experimental new Fort Street Diary prototype mk.1.RBY.\""
        mox "\"Among its features, it records your subjects, the progress of your interpersonal relationships and academic studies\""
        mox "\"All in a non-invasive system, designed to allow the school to monitor your life, and allows for early intervention with problem students\""
        mox "\"It's so advanced that, by the time it's viable for a school-wide rollout, it'll probably be outdated\""
        # check if person has diary yet
        if not game.hasDiary:
            sze "\"...\""
            sze "\"But I don't want it\""
            mox "\"It's an offer you can't refuse\""
            mox "\"And if the diary is more than 10m from your person at any time, as regional director of educational shit, I will use my elite B.R.A.S.I. squad to apprehend you\"" 
            $ _string = "{b}{grow}{rainbow}B.R.A.S.I.{/rainbow}{/grow}{/b}"
            sze "\"wtf is [_string]?\""
            mox "\"The {b}B{/b}oard of Studies {b}R{/b}egulatory {b}A{/b}ction {b}S{/b}quad for {b}I{/b}ntervention\""
            mox "\"Good, you are demonstrating the critical and inquiring nature that is expected of all Fortians. I am confidant that my decision to use you as the guinea pig for the diary was a good one\""
            sze "\"Wow it also has a bookmark string thingy\""
            "You walk away with your shiny new toy"
            "This time try not to put it up your ass"
            $ _string = "{i}{rainbow}{grow}Blushes violently{/grow}{/rainbow}{/i}"
            $ playsfx("vpunch.ogg")
            sze "[_string]" with vpunch
            "Nevermind..."
            $ game.hasDiary = True
            "You notice the bookmark string thingy is labelled with \"kms\""
            "As you graze the side of it, your skin tears open spilling {color=[PrimaryColours.RED]}{b}blood{/b}{/color} onto the pages"
            $ achievements.unlock_achievement("unlockSuicide")
            sze "\"How come I can kill myself with this diary\""
            mox "\"Its a new feature that students will want after they start the {b}HSC{/b}\""
            sze "\"How do I use this thing?\""
            mox "\"Here let me show you\""
            $ diary.open() 
            mox "\"Use the navigation buttons above to select a page, and press \"Close\" to exit it\""
            $ achievements.unlock_achievement("unlockDiary")
            hide screen float_menu
            show screen float_menu
            mox "\"Click on \"Open diary\" to open the diary again\""
            "...."
            "You walk away, holding this leather bound book between your {s}asscheeks{/s}hands"
#   will include a sorta psychopass system with this diary, where -ve score is good, +ve is bad; you start off as an exemplary student
#   "Exit Profile Exemplified" (best score) -> "Socially Aware" (good score) -> "Clear" (average) -> "stained" (bad) -> "in the shits" (suspended) -> "expelled waste" (expelled)
#   more so reliant on the (as of now) hidden two part moxcounter -> both add up at the same time
#   daily moxcounter -> pretty self-explanatory, resets everyday. I'm thinking 2 or 3 of these in one day = fkd by mox
#   persistent moxcounter -> maybe have it decrease by 3 every week? The idea is, this will act as an aggregate, so you would be noticed for doing naughty things
#   maybe once your persistent moxcounter hits "in the shits" you will be insta-suspended when another moxcounter is added?
#   post-suspension, moxcounter does not decrease for 4 weeks (a month); any further infraction results in expulsion, and loss of game
            
        else:
            sze "\"But you already gave me one\""
            mox "\"Since when did I give this out to anyone\""
            sze "\"Maybe you forgot? People do have a habit of forgetting me\""
            mox "\"...\""
            mox "\"Oh sorry what {b}were{/b} you saying again?\""
            "You walk off as [mox.name] lectures a new group of students"
        # jig school quest
        if not quests.is_quest_unlocked("jigschool1"):
            sze "This school kinda {color=[PrimaryColours.RED]}{b}sucks{/b}{/color}"
            $ sze.fort -= 1
            mox "What you just {b}say{/b} young man {b}!!!{/b}"
            sze "I said Michael Kirby is the epitome of social justice"
            "Your lie does not sound very convincing"
            mox "Ahhh how true that is"
            $ sze.fort += 2
            "You feel a strong temptation to jig your first day of school"
            $ quests.unlock_quest("jigschool1")
        hide moxham happy
        # rollcall
        "3 hours later"
        "I arrive at rollcall"
        "But no roll call teacher"
        "Ceebs waiting, I go to office to get timetable"
        "Got a new timetable"
        "I have Physics (Fluitsma), Engineering (Grant), English (Schlam), Chem (Webb), Extension Maths (Barton), Eco (Chapman)"
        scene bg school
        with fade
        sze "My life feels empty without her, like a photoelectric cell without UV rays"
        jump postrollcall1
