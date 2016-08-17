$ intelligence = 0
$ charm = 0
$ strength = 0
$ inteltutorial = False
$ thirst = 0
$ friendshiptutorial = False
$ charmtutorial = False
$ rinfriendship = 0
$ kokfriendship = 0
$ flufriendship = 0
$ rusfriendship = 0
$ prafriendship = 0
$ deafriendship = 0
$ wilfriendship = 0
$ chafriendship = 0
$ grafriendship = 0
$ moxfriendship = 0


label rusfriendshiploss:
    if friendshiptutorial is False:
        "You lost a friendship point with Rusali, friendship points can affect future events and decisions"
        $ rusfriendship -= 1
        $ friendshiptutorial = True
        return
    else:
        $ prafriendship -= 1
        "You lost a friendship point with Rusali. It is currently at [rusfriendship]"
        return
        
label rusfriendshipgain:
    if friendshiptutorial is False:
        "You gained a friendship point with Rusali, friendship points can affect future events and decisions"
        $ rusfriendship += 1
        $ friendshiptutorial = True
        return
    else:
        $ prafriendship += 1
        "You gained a friendship point with Rusali. It is currently at [rusfriendship]"
        return
        
label kokfriendshipgain:
    if friendshiptutorial is False:
        "You gained a friendship point with Willis, friendship points can affect future events and decisions"
        $ kokfriendship += 1
        $ friendshiptutorial = True
        return
    else:
        $ kokfriendship += 1
        "You gained a friendship point with Willis. It is currently at [chafriendship]"
        return
        
label kokfriendshiploss:
    if friendshiptutorial is False:
        "You lost a friendship point with Willis, friendship points can affect future events and decisions"
        $ kokfriendship -= 1
        $ friendshiptutorial = True
        return
    else:
        $ kokfriendship -= 1
        "You lost a friendship point with Willis. It is currently at [chafriendship]"
        return
        
label chafriendshipgain:
    if friendshiptutorial is False:
        "You gained a friendship point with Chao, friendship points can affect future events and decisions"
        $ chafriendship += 1
        $ friendshiptutorial = True
        return
    else:
        $ chafriendship += 1
        "You gained a friendship point with Chao. It is currently at [chafriendship]"
        return
        
label chafriendshiploss:
    if friendshiptutorial is False:
        "You lost a friendship point with Chao, friendship points can affect future events and decisions"
        $ chafriendship -= 1
        $ friendshiptutorial = True
        return
    else:
        $ chafriendship -= 1
        "You lost a friendship point with Chao. It is currently at [chafriendship]"
        return
        
label prafriendshipincrease:
    if friendshiptutorial is False:
        "You gained a friendship point with Pragash, friendship points can affect future events and decisions"
        $ prafriendship += 1
        $ friendshiptutorial = True
        return
    else:
        $ prafriendship += 1
        "You gained a friendship point with Pragash. It is currently at [prafriendship]"
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