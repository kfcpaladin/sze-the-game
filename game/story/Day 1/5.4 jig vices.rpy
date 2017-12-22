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
        $ garylevel += 2
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
                call garyreeducation
                jump recess1
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
                call garyreeducation
                jump recess1

label garyreeducation:
    jit "\"Welcome to my reeducation program my young Arthur!\""
    $ quests.unlockQuest("garythirst1")
    "You have unlocked Gary's reeducation program"
    "Check your achievements to start Gary's reeducation quests"

label garyreeducation1:
    jit "\"Touching the peepee makes white stuff come out\""
    $ sze.gain("thirst")
label garyreeducation2:
    jit "\"Through the power of the internet one can access websites showcasing images of naked women\""
    $ sze.gain("thirst", 2)
label garyreeducation3:
    jit "\"The penis can be inserted into the vagina achieve a pleasurable sensation\""
    $ sze.gain("thirst", 3)
label garyreeducation4:
    jit "\"In certain areas known as Brothels, one may exchange currency for sex\""
    $ sze.gain("thirst", 4)
label garyreeducation5:
    jit "\"When one grows tired of watching porn, they graduate to viewing 2-dimensional substitutes. This art form is known as Hentai.\""
    $ sze.gain("thirst", 5)
label garyreeducation6:
    jit "\"Contrary to popular belief Traps are not gay\""
    $ sze.gain("thirst", 6)
label garyreeducation7:
    jit "\"It is said that upon remaining a virgin for 30 years, one will gain wizardly powers.\""
    $ sze.gain("thirst", 7)
label garyreeducation8:
    jit "\"Autofellatio is a sacred technique, known to only the most skilled perverts.\""
    $ sze.gain("thirst", 8)
