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
                    mox "\"So I'll extend to you an invitation to visit my office after school\""
                    sze "\"Oh...\""
                    mox "\"But you were being gutsy and honest, so if you turn around now, I might forgive you, just this once\""
                    sze "Damn, that was close"
                    call dead from _ceebswiththisfornowwillcontinue
                "I wouldn't":
                    sze "\"N-n-no\""
                    mox "\"You lie\""
                    mox "\"You ded\""
                    call dead from _ceebsenglishplaceholder
            jump dead
        "Actually I need to pass":
            "Captian's report, {s}February 4th, 2531{/s} first day of year 11"
            "{s}Five year, five long years.{/s} 15 minutes, 15 long minutes. That's how long it took to get {s}Harvest back{/s} what the fuck was going on."
            "At first it was going well...{s}then setback after setback, loss after loss...{/s} book after book,questions after questions..."
            "Made what was going to be a {s}quick and decisive win{/s} a bludge lesson..."
            "Into fifty minutes of hell..."
            sze "\"Bullshittery at it's finest\""
            jump mthext1day1
