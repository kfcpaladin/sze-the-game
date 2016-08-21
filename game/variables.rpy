
label tutorialfriendship:
    # edit this stuff
    "Friendship is a measure of how close you are with someone"
    $ friendshiptutorial = True
    return

label dailymoxcounter:
    $ moxcounter2 += 1
    $ moxcounter1 += 1
label overallmoxcountergain:
    $ moxcounter1 += 1
label overallmoxcounterloss:
    $ moxcounter 1 -= 1
label rusfriendshiploss:
    $ rusfriendship -= 1
    "You lost a friendship point with Rusali. It is currently at [rusfriendship]"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return
        
label rusfriendshipgain:
    $ rusfriendship += 1
    "You gained a friendship point with Rusali. It is currently at [rusfriendship]"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return
        
label kokfriendshipgain:
    $ kokfriendship += 1
    "You gained a friendship point with Willis. It is currently at [kokfriendship]"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return
        
label kokfriendshiploss:
    $ kokfriendship -= 1
    "You gained a friendship point with Willis. It is currently at [kokfriendship]"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return
        
label chafriendshipgain:
    $ chafriendship += 1
    "You gained a friendship point with Chao. It is currently at [chafriendship]"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return
        
label chafriendshiploss:
    $ chafriendship -= 1
    "You lost a friendship point with Chao. It is currently at [chafriendship]"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return
        
label prafriendshipincrease:
    $ prafriendship += 1
    "You gained a friendship point with Pragash. It is currently at [prafriendship]"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return
    
label prafriendshipdecrease:
    $ prafriendship -= 1
    "You lost a friendship point with Pragash. It is currently at [prafriendship]"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return
        
label intelincrease:
    if inteltutorial is True:
        $ intelligence += 1
        "Your intelligence just increased. It is now at [intelligence]"
        return
    else:
        $ intelligence += 1
        "Your intelligence just increased. Intelligence is a measure of how smart you are. Currently you are a retard, however this may be changed through diligent studying and participating in class."
        $ inteltutorial = True
        return
        
label inteldecrease:
    if inteltutorial is True:
        $ intelligence -= 1
        "Your intelligence just decreased. It is now at [intelligence]"
        return
    else:
        "Your intelligence just decreased. Intelligence is a measure of how smart you are. Currently you are a retard, however this may be changed through diligent studying and participating in class."
        $ intelligence -= 1
        $ inteltutorial = True
        return
        
label charmincrease:
    if charmtutorial is True:
        $ charm += 1
        "Your charm just increased. It is now at [charm]"
        return
    else:
        $ charm += 1
        "Your Charm just increased. Charm is a measure of how well you slay. Currently you are a faggot, however this may be changed through slaying not being retarded in day to day life."
        $ charmtutorial = True
        return
        
label charmdecrease:
    if charmtutorial is True:
        $ charm -= 1
        "Your charm just decreased. It is now at [charm]"
        return
    else:
        "Your Charm just decreased. Charm is a measure of how well you slay. Currently you are a faggot, however this may be changed through slaying not being retarded in day to day life."
        $ charm -= 1
        $ charmtutorial = True
        return
