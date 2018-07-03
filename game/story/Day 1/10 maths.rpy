# maths class
label mthext1day1:
    "Next class is Extension 1 maths, with Mr Barton."
    "Rumors have it that even on the last day of school, Mr Barton won't let you celebrate."
    "You grit your teeth as you prep urself for some hardcore maths."
    "Perhaps you should kill yourself now, i mean, what do you think? I doubt i can think of any better dialogue after this scene."
    "Or is the chance that kahoot is after this period worth living for?"
    menu:
        "kms":
            "wow you suck at keeping yourself alive"
            call screen kms
        "don't":
            "You don't, killing urself means u might not be able to play kahoot later, and kahoot is always worth living for"
            "In the first 15 minutes of maths class the drama starts."
            "In the beginning it was quiet, then the tapping started, and it was clear that someone was doing some dodgy shit in class"
            "You sze in the corner, Anthony Lin, a big but quiet kid, hunched over his laptop"
            "It's not long before Barton szes this as well, and then the shit storm begins..."
            jump mthext1shitstorm

label mthext1shitstorm:
    $ autosave()
    "The Barton asks, Anthony what are you doing on your computer?"
    "Geogebrah sir is the reply" #create anthony lin character later
    "No your not, bring your laptop over here"
    "It's just geogebrah sir"
    $ playsfx("vpunch.ogg")
    "No bring it here" with vpunch
    "Anthony brings is computer to Barton and in a few moments gets sent to the principal's office, and is never seen again"
    sze "lol"
    "In your pencil case your calculator lights up"
    jump econ1
