#FRIENDSHIP LEVELS
	#friends included already: Rusali, Willis, Yang, Chao, Pragash, Dean, Richard
label tutorialfriendship:
    # edit this stuff, also they are not necessarily a faggot cos of the starting friendship values
    "Friendship is a measure of how close you are with someone, although if you are reading this, ur probs a faggot to them."
    $ friendshiptutorial = True
    return
	
label rusfriendshipgain:
    $ rusfriendship += 1
    "You're Rusali's best friend. Not really, you have to be a girl but your friendship with him is currently at [rusfriendship]"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return
    
label rusfriendshiploss:
    $ rusfriendship -= 1
    "You dogged Rusali, thus your friendship level with him is currently at [rusfriendship]"
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
    
label deafriendshipgain:
    $ deafriendship += 1
    "You have Arbitrarily become more Masterchief to Dean, causing your friendship with Dean to increase to [deafriendship]"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return
        
label deafriendshiploss:
    $ deafriendship -= 1
    "You must've confused Masterchief with Masterchef cos he thinks you're a shit, resulting in friendship with Dean to drop to [deafriendship]"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return  
    
label dikfriendshipgain:
    $ dikfriendship += 1
    "You probably listened to some capitalist or historical or weapon related rant, increasing your friendship with Richard to [dikfriendship]"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return
        
label dikfriendshiploss:
    $ dikfriendship -= 1
    "You probably use wrong grammar or make rude joke, very annoy Rick Dick, Friendship now is [dikfriendship]"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return
		
label rinfriendshipgain:
    $ rinfriendship += 1
    "You grew one step closer with Serena, your friendship with her is now at [rinfriendship]"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return  
	
label rinfriendshiploss:
    $ rinfriendship -= 1
    "Friendzoned again, your advances towards her were probably rejected, unfortunately your relationship with her has suffered and is now at [rinfriendship]"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return  

label flufriendshipgain:
    $ flufriendship += 1
    "Your phys rank is rapidly rising, as is your friendship with Fluitsma, now at [flufriendship]. Maybe soon you could get some \"private lessons\""
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return  
	
label flufriendshiploss:
    $ flufriendship -= 1
    "Something you did upset Ms Fluistma. Your current predicted Phys HSC mark is [flufriendship]. Just kidding, thats your friendship with her"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return  
	
label grafriendshipgain:
    $ grafriendship += 1
    "You are probably one of the few students who actually try in engineering. This does not go unnoticed by Grant-senpai, and your friendship with him is now at [grafriendship]"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return  
	
label grafriendshiploss:
    $ grafriendship -= 1
    "Grant wasnt exactly pleased with your behaviour, resulting in friendship dropping to [grafriendship]. Looks like you might have to spend some more time in the naughty corner."
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return  
		
label moxfriendshipgain:
    $ moxfriendship += 1
    "Moxham has finally recognised you diligence and continued efforts to improve the school, resulting in your friendship rising to [moxfriendship]"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return  
	
label moxfriendshiploss:
    $ moxfriendship -= 1
    "Your friendship with Moxham dropped to [moxfriendship]. Looks like more afterschool detentions, suspensions or worse."
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return  
		
label drkfriendshipgain:
    $ drkfriendship += 1
    "?????? [drkfriendship]"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return  
	
label drkfriendshiploss:
    $ drkfriendship -= 1
    "??????? [drkfriendship]"
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return  
		
label jitfriendshipgain:
    $ jitfriendship += 1
    "Your friendship with Gary rose to [jitfriendship]. Maybe now he will allow you to access his secret hentai stash."
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return  
	
label jitfriendshiploss:
    $ jitfriendship -= 1
    "Your friendship with Gary dropped to [jitfriendship]. You probably criticized his interests in chinese cartoons or something."
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return  
		
label leefriendshipgain:
    $ leefriendship += 1
    "???? [leefriendship]. ?????."
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return  
	
label leefriendshiploss:
    $ leefriendship -= 1
    "??????[leefriendship]. ????."
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return  	
		
label royfriendshipgain:
    $ royfriendship += 1
    "You improved your friendship with Roy, it is now at [royfriendship]. You are safe from his gas attacks, for now."
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return  
	
label royfriendshiploss:
    $ royfriendship -= 1
    "Your friendship with Roy dropped to [royfriendship]. It is strongly advised you immediately evacuate the room."
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return  	
		
label butfriendshipgain:
    $ butfriendship += 1
    "????? [butfriendship]. ?????."
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return  
	
label royfriendshiploss:
    $ butfriendship -= 1
    "????? [butfriendship]. ?????."
    if friendshiptutorial is False:
        call tutorialfriendship
        return
    else:
        return  
		
#STATS
		
label intelgain:
    if inteltutorial is True:
        $ intelligence += 1
        "Congratulations"
		if intelligence > 100:
			"You have surpassed even Justin Wu, your intelligence is now at [intelligence]"
			return
		elif intelligence > 75:
			"You just got smarter, maybe you'll be able to impress Serena with your 99.95 predicted ATAR, and your intelligence of [intelligence]"
			return
		elif intelligence > 50:
			"You are quite smart already, maybe not band-6 yet, but getting there. A bit more hard work and you will truly ACE TRIALS. Your current intelligence is [intelligence]"
			return
		elif intelligence > 25:
			"At marginally above average you really shouldnt be celebrating yet. Your intelligence is at [intelligence]"
			return
		elif intelligence > 0:
			"With your remarkably average intelligence of [intelligence], Serena will probably not be impressed."
			return
		elif intelligence > -25:
			"You are a bit slow, with intelligence of [intelligence]"
			return
		elif intelligence > -50:
			"You are probably doing worse than Chao in your tests currently, with intelligence of [intelligence]"
			return
		elif intelligence > -75:
			"It's astonishing how someone with an intelligence of [intelligence] even made it to Fort Street. How many dicks did you have to suck to get here?"
			return
		elif intelligence > -100:
			"With intelligence of [intelligence], you are not even a functioning member of society."
			return
		else:
			"You're getting there, a bit more hard work and you will be smarter than a braindead ant."
			return
    else:
        $ intelligence += 1
        "Your intelligence just increased. Intelligence is a measure of how smart you are. Currently you are a retard, however this may be changed through diligent studying and participating in class."
        $ inteltutorial = True
        return
        
label intelloss:
    if inteltutorial is True:
        $ intelligence -= 1
        "You become a bit dumber"
		if intelligence > 100:
			"With intelligence of [intelligence], maybe its for the better. Your thoughts were too complex for even Stephen Hawking."
			return
		elif intelligence > 75:
			"But your predicted ATAR is still a safe 99.95, and your intelligence of [intelligence]"
			return
		elif intelligence > 50:
			"You are quite smart already, maybe not band-6 yet, but getting there. A bit more hard work and you will truly ACE TRIALS. Your current intelligence is [intelligence]"
			return
		elif intelligence > 25:
			"Your intelligence is at [intelligence], not particularly amazing."
			return
		elif intelligence > 0:
			"With your remarkably average intelligence of [intelligence], Serena will probably not be impressed."
			return
		elif intelligence > -25:
			"You are a bit slow, with intelligence of [intelligence]"
			return
		elif intelligence > -50:
			"You are probably doing worse than Chao in your tests currently, with intelligence of [intelligence]"
			return
		elif intelligence > -75:
			"It's astonishing how someone with an intelligence of [intelligence] even made it to Fort Street. How many dicks did you have to suck to get here?"
			return
		elif intelligence > -100:
			"With intelligence of [intelligence], you are not even a functioning member of society."
			return
		else:
			"You are somehow dumber than a rock, like literally. I dont know how that is even possible."
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
