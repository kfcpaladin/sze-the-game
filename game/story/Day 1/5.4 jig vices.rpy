label asszemblyjigoloviceland:
    sze "\"whooo!!!vices!!!!\""
    jit "\"k...\""
    jit "\"wait a minute...vices can be used for bdsm, if you really think about it\""
    if sze.thirst > 1:
        sze "\"Gotta admit, every now and then I do enjoy to engage in some more aggressive play\""
        jit "\"I see you are a man of culture as well.\""
        jit "\"May I interest you in a few of my own Re-education lessons\""
        jit "\"Willis Lau can attest to their quality\""
        sze "\"Why of course, how could one refuse such a marvellous offer\""
        jit "\"Well then, if you desire, please follow me\""
        call garyreeducation
        jump recess1
    elif sze.intellect > 5:
        sze "\"It is despicable that you would even think to suggest such a thing\""
        sze "\"Such digusting behaviour, it is against the school code of conduct, and more importantly against the societies moral standards\""
        jit "\"Yeaa, whatever dude.\""
        jit "\"Your honestly sounding like the SRC right now\""
        jit "\"I think you need some re-education boi.\""
        call garyreeducation
        jump recess1
    else:
        sze "\"wtf is bdsm\""
        jit "\"Wow\""
        jit "\"Are you retarded dude?\""
        $ sze.intellect -= 1
        jit "\"Even fucking Li Xu knows, and hes legit autistic\""
        $ jit.friendship -= 1
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
                $ sze.thirst += 1
                jit "\"It's been a while since I had a {b}willing{/b} participant\""
                $ jit.friendship += 1
                "You start to regret your hasty hormone-led decision"
                call garyreeducation
                jump recess1
            "No, this seems too shifty":
                sze "He does make a good point, but then again this is coming from Jittian"
                sze "No, I must resist the temptation"
                $ sze.thirst -= 1
                sze "Who knows what dark secrets, Gary has planned"
                sze "\"That sounds pretty sus, gonna sit out on this one\""
                "Jittian's welcoming smile turns into a malovent smirk"
                jit "\"Did I imply you had a choice?\""
                jit "\"Because you didn't\""
                $ jit.friendship -= 1
                call garyreeducation
                jump recess1


