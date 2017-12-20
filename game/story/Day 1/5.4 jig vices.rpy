label asszemblyjigoloviceland:
    sze "\"whooo!!!vices!!!!\""
    jit "\"k...\""
    jit "\"wait a minute...vices can be used for bdsm, if you really think about it\""
    if thirst > 1:
        sze "\"Gotta admit, every now and then I do enjoy to engage in some more \""
    elif sze.intellect > 5:
        sze "\"It is despicable that you would even think to suggest such a thing\""
    else:
        sze "\"wtf is bdsm\""
        jit "\"Wow\""
        jit "\"Are you retarded dude?\""
        $ sze.loss("intellect")
        jit "\"Even fucking Li Xu knows, and hes legit autistic\""
        $ jit.loss()
        jit "\"Honestly Arthur, ya need to learn some shit\""
        jit "\"Read a book, or watch some porn or some shit\""
        sze "\"Wait, what. Watch some porn???\""
        "Gary seems to go on as if he hasn't heard you"
        jit "\"Wait I have an idea, how about you go through my re-education program\""
        jit "\"Willis went through the program in Year 7, and now he's slaying Serena. Maybe the program could do you some good\""
        jit "\"Well??\""
        menu:
            "Should I participate in the re-education program?"
            "If it worked for Willis, it will work for me":
                sze "I would sacrifice anything to have Serena"
                sze "Even my own sanity"
                $ sze.gain("thirst")
                jit "\"It's been a while since I had a {b}willing{/b} participant\""
                $ jit.gain()
                "You start to regret your hasty hormone-led decision"

            "No, this seems too shifty":
                sze "He does make a good point, but then again this is coming from Jittian"
                sze "No, I must resist the temptation"
                $ sze.loss("thirst")
                sze "Who knows what dark secrets, Gary has planned"
                sze "\"That sounds pretty sus, gonna sit out on this one\""
                "Jittian's welcoming smile turns into a malovent smirk"
                jit "\"Did I imply you had a choice?\""
                jit "\"Because you didn't\""
                $ jit.loss()



label asszembly1garyreeducation:
    jit "\"diks\""
