label phys1p3principal1:
    #You and rusali
    scene bg principaldoor
    rus "\"Oh no, ive never had a detention before.\""
    "He starts muttering in Indonesian"
    rus "\"Better tell my parents otherwise I'll get rekt\""
    sze "\"If you don't tell your parents, wouldn't you get less rekt?\""
    rus "\"Waow, stop roasting me\""
    "It seems that Rusali does not appreciate this comment of yours"
    $ rus.friendship -= 1
    scene bg principaloffice
    $ game.moxCounter += 1
    if game.moxCounter > 1:
        mox "\"You two again?\""
        $ playmusic("VarienThroneOfRavens.ogg")
        mox "\"You're already in my shit books\""
        rus "\"Oh no...\""
        $ playsfx("hpunch.ogg")
        mox "\"I didn't say you could speak\"" with hpunch
        rus "\"Aowwww\""
        sze "\"Oh shit\""
        $ playsfx("vpunch.ogg")
        mox "\"You're both dead\"" with vpunch
        rus "\"Run, ru-\""
        mox "\"I'll clear all your records of loading dockness if you rek Arthur and spend afternoon of re-education with me\""
        show rusali normal
        $ playsfx("vpunch.ogg")
        rus "\"Soz man. Need to ace trials\"" with vpunch
        sze "\"faarrrr\""
        jump dead
    else:
        show moxham unhappy
        mox "\"I've been told you two have been disrupting the propogation of education by being dropkicks\""
        mox "\"In this school we have a no tolerance policy on throwing balls (except in my dungeon *wink *wink)\""
        mox "\"Do you understand?\""
        menu:
            "\"Yes\"":
                jump phys1p3principal3
            "\"No\"":
                jump phys1p3principal4
label phys1p3principal2:
    #Sze and Chao - David cos Zhichao geddit? no
    scene bg principaldoor
    cha "\"Fuck, i cant go to an afternoon detention, i have to slay my gfs after school\""
    sze "\"Wow, how do you slay so many LG's\""
    $ sze.thirst += 1
    cha "\"You just do\""
    $ sze.charm += 1
    scene bg principaloffice
    $ game.moxCounter += 1
    if game.moxCounter > 1:
        show moxham unhappy
        mox "\"You again?\""
        $ playmusic("VarienThroneOfRavens.ogg")
        mox "\"Chao, I'll clear you of your dropkickness records if you beat the shit out of him\""
        cha "\"Yes ma'am\""
        sze "\"nope\""
        jump dead
    else:
        show moxham unhappy
        $ game.moxCounter += 1
        mox "\"I have been told of two boys who were displaying unsatisfactory behaviour in class\""
        mox "\"Especially you Joshua Chao Lin, you have a history of being drop kick\""
        mox "\"This behaviour is intolerable and unbefitting of the Fortian Race. I expect this from\"" #unfinished sentence?
        mox "\"You two are lucky you arent expelled\""
        mox "\"Instead you will be given after school detention...how merciful of me\""
        hide moxham unhappy
        jump eng1p1

label phys1p3principal3:
    # said yes
    sze "\"Yes\""
    mox "\"I hope that this is the end of the matter\""
    mox "\"Go to your next period, here's a note excusing your lateness and another one for after school detention.\""
    mox "\"Now scram\""
    hide moxham unhappy
    show rusali
    rus "\"WAOW, this is my first detention.\""
    rus "\"How will i ever ace trials with a detention\""
    rus "\"I can no longer spend my afternoon doing tutoring and writing textbooks\""
    $ rus.friendship -= 1
    hide rusali
    jump eng1p1

label phys1p3principal4:
    # said no
    sze "\"...No\""
    mox "\"Wow, you must be retarded\""
    mox "\"Our school offers support programs for retarded fucks like you, so i am giving you 2 afterschool detentions for the price of 1.\""
    mox "\"This way you will be exit profile\""
    $ sze.fort += 1
    mox "\"And DCR, i had expected better of a student wanting ace trials\""
    $ game.moxCounter += 1
    hide moxham unhappy
    show rusali
    rus "\"FUARR, my trials can no longer be aced\""
    rus "\"I'll have to become a drop kick, or worse, go to the loading dock\""
    sze "\"Calm down trials are still 1.5 years away\""
    rus "\"Why do i always get roasted\""
    rus "\"Stop roasting me arthur\""
    hide rusali
    jump eng1p1
