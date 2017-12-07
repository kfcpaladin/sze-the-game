# first english class testing
label english1:
    "You arrive at {s}base camp{/s} ground floor of Wilkins"
    "You look up at the stairs, into the gaping maws of the infinite abyss"
    sze "Am I even bothered enough for this?"
    menu:
        "Fuck this shit, I'm out":
            call fortianloss from _english1ceebsstairs1
            sze "I don't want to risk a heart attack"
            "You start turning around"
            "And stop before the forboding form of Moxham"
            mox "\"Well, well, well\""
            mox "\"You wouldn't happen to be turning away from your class, now, would you?\""
            menu:
                "I would":
                    sze "\"Yea, so what?\""
                    mox "\"So I'll extend to you an invitation to visit my {s}secret dungeon{/s} office after school\""
                    sze "\"Oh...\""
                    mox "\"But you were being honest, so if you turn around now, I might forgive you, just this once\""
                    sze "Damn, that was close"
                    jump eng1ascension
                "I wouldn't":
                    sze "\"N-n-no\""
                    mox "\"You lie\""
                    sze "\"ah, I, uh, wuz just, ah, going to go t-to the t-toilet... yeah, that's what I was doing\""
                    mox "\"Well, you do like you are about to piss yourself\""
                    call strengthloss from _eng1ceebsbutthenmoxham
                    mox "\"I expect you to be back here in 5 minutes, otherwise there will be consequences\""
                    sze "\"erm...'kay\""
                    "You have no choice but to comply"
                    jump eng1ascension
        "I actually need to pass":
            "You take a deep breath and {s}gather your qi{/s} mentally prepare yourself for the brutal climb"
            sze "I need to be {b}smart{/b} about this and {b}strong{/b} enough to make it successfully"
            jump eng1ascension
            
tag eng1ascension:
            sze "Can't be too hard, just put one foot in front of the other"
            "..."
            sze "\"Just keep swimmin'\""
            "You notice Dean walk past you"
            dea "\"man, these steps are pretty stupid. We should just use rockets\""
            "..."
            sze "\"One flight down, three to go\""
            "..."
            sze "\"I can do this\""
            if intelligence > 5:
                "You notice Richard walk past you"
                sze "\"If Pheidippides of Athens could run from Marathon to Greece, I can get up these steps\""
                dik "\"Quite so, my good fellow! Persevere but a few seconds longer, then \"Joy to you, we've won\"!\""
                call dikfriendshipgain from _eng1flight1dikfriendshipgain
                return
            else:
                "You notice Richard walk past you"
                sze "\"if that greek guy could do that mara thing, then I can do these stairs too\""
                "You notice Richard shaking his head"
                dik "\"I almost pity thee. Thine incompetence is but a miracle beholden to few\""
                call dikfriendshiploss from _eng1flight1dikfriendshiploss
                return
            "..."
            "The second flight was down, half way"
            "You find yourself at the first floor, and allow yourself one second of respite"
            "Gary/Jitian staggers past"
            jit "\"Phew, good thing I have Strauss for English. This is as high as I need to go; sucks to be everyone else\""
            sze "\"lucky\""
            "..."
#           will continue from here next time, naruto online rn
            "Captain's report, {s}February 4th, 2531{/s} January 28th, 2015"
            "{s}Five year, five long years.{/s} 5 minutes, 5 long minutes. That's how long it took to get {s}Harvest back{/s} to the top."
            "At first it was going well...{s}then setback after setback, loss after loss...{/s} book after book,questions after questions..."
            "Made what was going to be a {s}quick and decisive win{/s} a bludge lesson..."
            "Into fifty minutes of hell..."
            sze "\"Bullshittery at it's finest\""
            jump mthext1day1
