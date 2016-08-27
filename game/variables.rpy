
label tutorialfriendship:
    # edit this stuff
    "Friendship is a measure of how close you are with someone, although if you are reading this, ur probs a faggot to them."
    $ friendshiptutorial = True
    return

label dailymoxcounter:
    $ moxcounter2 += 1
    $ moxcounter1 += 1
    return
label overallmoxcountergain:
    $ moxcounter1 += 1
    return
label overallmoxcounterloss:
    $ moxcounter1 -= 1
    return
label rusfriendshiploss:
    $ rusfriendship -= 1
    "You dogged Rusali, thus your friendship level with him is currently at [rusfriendship]"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return
        
label rusfriendshipgain:
    $ rusfriendship += 1
    "You're Rusali's best friend. Not really, you have to be a girl but your friendship with him is currently at [rusfriendship]"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return
        
label kokfriendshipgain:
    $ kokfriendship += 1
    "You have strategically gained friendship with Willis, hoping that he will divulge secrets to slaying Serena.
    It is currently at [kokfriendship]"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return
        
label kokfriendshiploss:
    $ kokfriendship -= 1
    "Fuck Willis. \"Friendship\" is currently at [kokfriendship]"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return
        
label wilfriendshipgain:
    $ wilfriendship += 1
    "You have further proved to Yang that you belong in his 4th Reich, friendship is currently at [wilfriendship]"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return
        
label wilfriendshiploss:
    $ wilfriendship -= 1
    "Ur a fcktard and will, at this rate, fail Yang's eugenics program. Friendship with him is currently at [wilfriendship]"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return
        
label chafriendshipgain:
    $ chafriendship += 1
    "If you were a LG, you would be one of Chao's gfs. Friendship with Chao is currently at [chafriendship]"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return
        
label chafriendshiploss:
    $ chafriendship -= 1
    "You almost made Chao raep you, friendship with Chao is currently at [chafriendship]"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return
        
label prafriendshipgain:
    $ prafriendship += 1
    "If you continue this way, maybe Dynamite Black might mention you in a future song, as friendship with Pragash is currently at [prafriendship]"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return
    
label prafriendshiploss:
    $ prafriendship -= 1
    "You weren't very cricket to Pragash, reducing your friendship with him to [prafriendship]"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return
        
label intelgain:
    if inteltutorial is True:
        $ intelligence += 1
        "Congratulations"
        "You just got smarter, maybe you'll be able to impress Serena with your mental capacity and intelligence, now at [intelligence]"
        return
    else:
        $ intelligence += 1
        "Your intelligence just increased. Intelligence is a measure of how smart you are. Currently you are a retard, however this may be changed through diligent studying and participating in class."
        $ inteltutorial = True
        return
        
label intelloss:
    if inteltutorial is True:
        $ intelligence -= 1
        "Congratulations"
        "U just got more retarded, your intelligence, or lack thereof, is now at [intelligence]"
        return
    else:
        "Your intelligence just decreased. Intelligence is a measure of how smart you are. Currently you are a retard, however this may be changed through diligent studying and participating in class."
        $ intelligence -= 1
        $ inteltutorial = True
        return
        
label charmgain:
    if charmtutorial is True:
        $ charm += 1
        "One day, you'll be dragonslayer. Your charm is now at [charm]"
        return
    else:
        $ charm += 1
        "Your Charm just increased. Charm is a measure of how well you slay. Currently you are a faggot, however this may be changed through slaying not being retarded in day to day life."
        $ charmtutorial = True
        return
        
label charmloss:
    if charmtutorial is True:
        $ charm -= 1
        "U make 3rd World fermented sewage look better than you cos your charm is now at [charm]"
        return
    else:
        "Your Charm just decreased. Charm is a measure of how well you slay. Currently you are a faggot, however this may be changed through slaying not being retarded in day to day life."
        $ charm -= 1
        $ charmtutorial = True
        return
    
label fortiangain:
    if forttutorial is True:
        $ fort += 1
        "You became more Michael Kirby maybe one day you will be proper protester, call the police "pig dogs" and be part of an artist collective, as your Fortianness is at [fort]"
        return
    else:
        $ fort += 1
        "Your Fortianness has just increased. Fortianness is how Fortian you are and can be improved by being more Michael Kirby. Currently, you aren't very Fortian."
        $ forttutorial = True
        return
        
label fortianloss:
    if forttutorial is True:
        $ fort -= 1
        "You are less Michael Kirby and are probably a dirty, capitalist, bourgeois pig who might have underlying religious affiliations as you allowed your Fortianness to drop to [fort]"
        return
    else:
        $ fort -= 1
        "Your Fortianness has just decreased. Fortianness is a measure of how Fortian you are and can be improved by being more Michael Kirby. Currently, you aren't very Fortian."
        return
