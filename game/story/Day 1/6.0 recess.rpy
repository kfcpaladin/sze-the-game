label recess1:
    $ clock.set_time("recess")
    $ autosave()
    "As you leave assembly hall you see a shadow fliting across Kilgour Quad"
    jit "\"Sup sze, How was assembly? Should've jigged with me, I never get caught\""
    jump recess1a

label recess1a:
    $ clock.set_time("recess")
    $ autosave()
    "It is now recess, which has unfortunately been cut short to 10 minutes to due an extended assembly"
    sze "Hmm, what should I do today for recess?"
    call screen fortmap
    if _return == 1:
        "Rowe"
        scene bg rowecorridor
        sze "\"Wow, it's Rowe\""
        if game.metDerek is True:
            sze "Should I try to talk to anyone?"
            menu:
                "Talk to Will Yang":
                    sze "\"Hey Yang\""
                    wil "\"Heil\""
                    wil "\"I have heard that there is a hidden group in our grade, subverting the control of Moxham and the SRC/PNC\""
                    sze "\"Eh?...\""
                    wil "\"The rats should be found and destroyed; but there is a problem. I need this irritation called \"evidence\"...\""
                    sze "\"I guess...\""
                    if sze.intellect > 5:
                        sze "\"But I thought you wanted to get rid of the SRC/PNC influence from the school\""
                        wil "\"Only someone as un-fortian as you could say that\""
                        $ sze.fort -= 1
                        if wil.friendship > 40:
                            wil "\"But since you have proven your worth\""
                            wil "\"Indeed, I do. I foresee that Moxham will have outlived her usefulness by {nw}\""
                            wil "\"Ahem\""
                            wil "\"You do raise an interesting and compelling point...\""
                            wil "\"Hypothetically...\""
                            wil "\"It is an uncharacteristically intelligent suggestion\""
                            sze "\"...\""
                            wil "\"But I digress\""
                            $ sze.intellect += 1
                            sze "\"Why is senpai always so cruel?\""
                            wil "\"Quiet, I have just developed brilliant plan\""
                            wil "\"I may require a certain someone to snoop around and try to infiltrate this secret society, this Illuminati\""
# the illuminati is a council of halfies, who have infiltrated almost all the groups in the grade, besides one or two (one of which is Rowe)
                            sze "\"...me?\""
                            wil "\"Perhaps\""
                            wil "\"Anyhow, enough of this for now\""
                            wil "\"I do believe we have English\""
                            jump english1
                        else:
                            wil "\"In fact, I should probably unfriend you for being such an un-fortian monster\""
                            $ wil.friendship -= 1
                            wil "\"But I shall ignore that interruption and think on this later\""
                            jump english1
                    else:
                        wil "\"Very well, I have a brilliant plan\""
                        wil "\"I may require a certain someone to snoop around and try to infiltrate this secret society, this Illuminati\""
# the illuminati is a council of halfies, who have infiltrated almost all the groups in the grade, besides one or two (one of which is Rowe)
                        sze "\"...me?\""
                        wil "\"Maybe... I'll think about it\""
                        wil "\"Anyhow, enough of this for now\""
                        wil "\"I do believe we have English\""
                        jump english1
                "Talk to Derek" if game.electionPromise is True:
                    sze "\"Hey Derk\""
                    drk "\"Ey\""
                    sze "\"I have a couple of ideas regarding Pragga's political campaign that will take the SRC by storm and{nw}\""
                    drk "\"Ceebs\""
                    sze "\"Eh?...\""
                    drk "\"I'm ceebs right now; let's talk about this later\""
                    sze "\"I guess...\""
                    sze "\"How did you arrive late? Didn't see you at roll call\""
                    drk "\"I was just ceebs with getting out of bed for ten minutes and was playing Kancolle\""
                    drk "\"You should try playing Idolm@ster\""
                    sze "\"But that's what Gary played, I thought\""
                    drk "\"No that's Idolm@lester"
                    sze "\"wtf\""
                    drk "\"Oh, looks like recess is ending, what class do you have?\""
                    sze "\"Check your own timetable\""
                    drk "\"ceebs\""
                    sze "\"Fine, I have English with Schlam\""
                    drk "\"Well, everyone has English at same time, so I'll follow you\""
                    $ drk.friendship += 1
                    jump english1
                "Talk to Richard":
                    sze "Maybe I should talk to Richard, since he's not really talking to anyone"
                    sze "\"Hey Rick\""
                    dik "\"Hey Arthur, anything you want to discuss in particular?\""
                    sze "\"Well, not really, but I just figured I might ask about {nw}\""
                    roy "\"Heeeeeeeyyyyyyyy, it's Arthur\""
                    dik "\"Hi Roy, butting into anything you can, as always ;)\""
                    sze "\"Hello Roy\""
                    sze "It's Roy. He's sorta the school clowm, a bit autistic, literally. He likes nerf guns, rants and loves humanoid robots {s}to an unhealthy extent{/s}}\""
                    sze "\"Is it true that you make ass burgers?\""
                    roy "\"Whenever I go to the toilet, I do. But I also do have Asperger's\""
                    roy "\"Oh yeah, Richard, I was gonna ask about the function of a pump action shotgun, in order to mod a nerf gun\""
                    dik "\"Hmm, seems cool, but I don't know anything about Nerf guns; all I know are wikipedia articles on actual guns\""
                    dik "\"But since Arthur is here, let us discuss something else\""
                    sze "\"Ok...like?\""
                    roy "\"Here's a fun hypothetical; if you get a robot gf, would you get one?\""
                    dik "\"*Sigh* This again...\""
                    menu:
                        "\"No\"":
                            sze "\"No, not everyone has a robot fetish\""
                            sze "\"Just hire a person to give you hugs ;) ;)...\""
                            roy "\"That's stupid, you'd have to pay money for prostitution services\""
                            drk "\"Lol does Sze want to pay money for touches??\""
                            if sze.intellect >=3:
                                sze "\"No, Roy here wants to build robot fucktoys cos he says you need to pay money for human touches\""
                                drk "\"But don't you need money for robot parts then?\""
                                dik "\"Wot, Roy, why would you want a robot GF\""
                                roy "\"I don't want one, just, if you had too, wouldn't you get one\""
                                sze "\"But I won't need one cos I'd probably be able to get one\""
                                "You have impressed everyone with your confidence in your ability to slay (eventually)"
                                $ sze.charm += 1
                                roy "\"You people don't get it. This is because you are held back by your human limitations\""
                                "You tune out"
                                "Recess is over, time for next class"
                                jump english1
                            else:
                                sze "\"N-no...\""
                                drk "\"If you think about it, it's probably the only way you'll ever get anyone\""
                                kok "\"Lel actually true, I at least have Serena\""
                                sze "\"Just watch me\""
                                sze "\"I will win her over\""
                                sze "Let me reminisce of the sakura in full bloom in the Valley, as I first met her"
                                show bg dreamtree
                                with fade
                                sze "For your raven hair"
                                sze "My purpose has been twice bound"
                                sze "For your love, my life"
                                "You try poking yourself with a moderately sharp stick"
                                "You faintly hear Richard shouting"
                                dik "\"Oi, you fucking idiots, don't just stand there, stop him!\""
                                "You barely have enough strength to register what is happening"
                                sze "\"Ow, it wasn't meant to be like this\""
                                sze "\"Oh, there's the descending aorta\""
                                jump dead
                        "\"Vices\"":
                                sze "\"If I had no gf, I would rather play with vices\""
                                roy "\"Ok...\""
                                roy "\"You have successfully out-weirded me\""
                                "Recess is over, time for next class"
                                jump english1

# make variable for royfriendship --> its roy.friendship
                        "\"Yes\"":
                            sze "\"Yes\""
                            sze "\"I'd totes stick ma dick in the exhaust pipe of a car transformer\""
                            roy "\"That's not what I meant\""
                            sze "\"And then as they go vrrm vrrm, I go vrrm vrrm\""
                            $ sze.thirst += 1
                            dik "\"...\""
                            dik "\"What the shit did I just hear?\""
                            sze "\"Don't worry about it, recess is over, time for English\""
                            jump english1




        else:
            "You go to Rowe Corner"
            sze "I sze Serena... I should talk"
            menu:
                "Talk":
                   "You move like a panther, with slick moves and predatory focus"
                   "The coast is clear; she is not with anyone and you are in optimal position to engage"
                   $ playsfx("vpunch.ogg")
                   "..." with vpunch
                   "Until you bump into Richard and Derek"
                   drk "\"Watch where you going, fgt\""
                   dik "\"Actually it's pronounced \"faggot\"\""
                   drk "\"Whatevs\""
                   sze "\"Wow soz...geez\""
                   sze "Derek is {s}a Machiavellian bastard{/s} an intelligent guy {s}whose morals are as fluid as his loyalties{/s}"
                   $ game.metDerek = True
                   "You turn your attention back to Serena, only to see her chatting with Willis"
                   "Your hunt has failed, leaving you greatly unsatiated"
                   $ sze.thirst += 1
                   menu:
                        "\"Try to get her attention\"":
                            sze "\"S-s-s-senpai\""
                            "\"...\""
                            sze "\"Senpai, n-notice meeee...\""
                            "\"...\""
                            sze "She still has not noticed me"
                            sze "I know what will get her attention"
                            sze "Let me reminisce of the sakura in full bloom in the Valley, as I first met her"
                            show bg dreamtree
                            with fade
                            sze "For your raven hair"
                            sze "My purpose has been twice bound"
                            sze "For your love, my life"
                            "You try poking yourself with a moderately sharp stick"
                            sze "\"Ow, it wasn't meant to be like this\""
                            sze "\"Oh, there's the descending aorta\""
                            jump dead

                        "\"Give up\"":
                            sze "I must temper my heart with reason"
                            sze "I don't need to be so thirsty"
                            $ sze.thirst -= 1
                            sze "maybe I should do something else"
                            jump recess1a

                "Ceebs":
                    "you decide to give up on your pursuit"
                    "Instead you choose to turn your attention towards other people"
                    $ sze.thirst += 1
                    menu:
                        "Talk to Richard":
                            "You notice Richard is busy in conversation about something with some other people"
                            if sze.charm >=5:
                                sze "\"Hi!\""
                                dik "\"Hi Arthur!\""
                                dik "\"I see you've broken the game; you aren't meant to be able to have the stats to see this\""
                                sze "\"lol\""
                                jump actualded
                            else:
                                sze "ceebs talking to Richard"
                                wil "\"Oh it's Arthur\""
                                sze "\"Hi Will\""
                                wil "\"Have you heard of this strange legend surrounding Anthony Le?\""
                                drk "\"There's a legend about Anthony Le? I must hear of this\""
                                sze "Derek is {s}a Machiavellian bastard{/s} an intelligent guy {s}whose morals are as fluid as his loyalties{/s}"
                                $ game.metDerek = True
                                sze "\"?\""
                                wil "\"In ages past, when I was but a young student in accelerated maths\""
                                sze "\"But he's in the same class as you were{nw}\""
                                wil "\"Shut up, you're ruining the story\""
                                wil "\"As I was saying\""
                                scene bg dream
                                with fade
                                $ stopmusic()
                                $ playmusic("TheRoomOSTMainTheme.ogg", loop=True)
                                wil "\"{i}In ages past, when I was but a young student in the Woodhouse School of Accelerated Maths{/i}\""
                                wil "\"{i}one of my most skilled peers was one Anthony Le {/i}\""
                                wil "\"{i}One among our number noted his intellectual prowess, noted how fast he blazed through the course content{/i}\""
                                wil "\"{i}And he let jealousy into his heart.{/i}\""
                                wil "\"{i}The one who was jealous of the Le was cunning in his own right. He knew many forgotten sciences{/i}\""
                                wil "\"{i}and had access to many arcane device{/i}\""
                                wil "\"{i}And it was he who noticed the Cherenkov radiation emitted by Anthony due to his speed{/i}\""
                                wil "\"{i}So in an epiphany, he wondered what would happen if he could capture some of Anthony's radiant brilliance{/i}\""
                                wil "\"{i}His afterimage{/i}\""
                                wil "\"{i}To that end, he borrowed Anthony's calculator{/i}\""
                                wil "\"{i}Tinkered with it, imbuing it with secret and ancient technologies and runes{/i}\""
                                wil "\"{i}He returned it, with the machine looking innocent enough{/i}\""
                                wil "\"{i}Yet, as soon as Anthony touched it, he had unknowingly channeled the entirety of his afterimage into the calculator{/i}\""
                                wil "\"{i}Thus, the usurper found the secret too Anthony's brilliance{/i}\""
                                wil "\"...\""
                                wil "\"Are you still awake?\""
                                menu:
                                    "\"Yes\"":
                                        sze "\"Yeah, but aren't you better than Anthony Le now?\""
                                        wil "\"Perhaps...one day you shall learn the rest of the story\""
                                        wil "\"For now, I do believe we have English\""
                                        jump english1
                                    "\"No\"":
                                        sze "\"Uh, totes, yeah, I liked the bit where you bashed him and then{nw}"
                                        wil "\"...so you weren't listening\""
                                        sze "\"No I wasn't...\""
                                        sze "\"I was absorbing\""
                                        $ wil.friendship -= 1
                                        wil "\"Whatever, let's just go English\""
                                        jump english1
                        "Talk to yourself":
                            sze "\"Hey man\""
                            sze "\"Hey, how's it goin'?\""
# include variable for introduction of Roy
                            roy "\"Hey, are you talking to yourself?\""
                            sze "It's Roy. He's sorta the school clowm, a bit autistic, literally. He likes nerf guns, rants and loves humanoid robots {s}to an unhealthy extent{/s}}\""
                            roy "\"Did I offend you? Why are you so quiet?\""
                            sze "\"I'm thinking, Roy\""
                            roy "\"What about? Let's talk about robots\""
                            roy "\"If you couldn't get a girlfriend, would you build a robot gf?\""
                            sze "\"Wot\""
                            menu:
                                "\"No\"":
                                    sze "\"No, not everyone has a robot fetish\""
                                    sze "\"Just hire a person to give you hugs ;) ;)...\""
                                    roy "\"That's stupid, you'd have to pay money for prostitution services\""
                                    drk "\"Lol does Sze want to pay money for touches??\""
                                    sze "Derek is {s}a Machiavellian bastard{/s} an intelligent guy {s}whose morals are as fluid as his loyalties{/s}"
                                    $ game.metDerek = True
                                    if sze.intellect >=3:
                                        sze "\"No, Roy here wants to build robot fucktoys cos he says you need to pay money for human touches\""
                                        drk "\"But don't you need money for robot parts then?\""
                                        dik "\"Wot, Roy, why would you want a robot GF\""
                                        roy "\"I don't want one, just, if you had too, wouldn't you get one\""
                                        sze "\"But I won't need one cos I'd probably be able to get one\""
                                        "You have impressed everyone with your confidence in your ability to slay (eventually)"
                                        $ sze.charm += 1
                                        roy "\"You people don't get it. This is because you are held back by your human limitations\""
                                        "You tune out"
                                        "Recess is over, time for next class"
                                        jump english1
                                    else:
                                        sze "\"N-no...\""
                                        drk "\"If you think about it, it's probably the only way you'll ever get anyone\""
                                        kok "\"Lel actually true, I at least have Serena\""
                                        sze "\"Just watch me\""
                                        sze "\"I will win her over\""
                                        sze "Let me reminisce of the sakura in full bloom in the Valley, as I first met her"
                                        show bg dreamtree
                                        with fade
                                        sze "For your raven hair"
                                        sze "My purpose has been twice bound"
                                        sze "For your love, my life"
                                        "You try poking yourself with a moderately sharp stick"
                                        "You faintly hear Richard shouting"
                                        dik "\"Oi, you fucking idiots, don't just stand there, stop him!\""
                                        "You barely have enough strength to register what is happening"
                                        sze "\"Ow, it wasn't meant to be like this\""
                                        sze "\"Oh, there's the descending aorta\""
                                        jump dead
                                "\"Vices\"":
                                    sze "\"If I had no gf, I would rather play with vices\""
                                    roy "\"Ok...\""
                                    roy "\"You have successfully out-weirded me\""
                                    "Recess is over, time for next class"
                                    jump english1
# make variable for royfriendship
                                "\"Yes\"":
                                    sze "\"Yes\""
                                    sze "\"I'd totes stick ma dick in the exhaust pipe of a car transformer\""
                                    roy "\"That's not what I meant\""
                                    sze "\"And then as they go vrrm vrrm, I go vrrm vrrm\""
                                    $ sze.thirst += 1
                                    dik "\"...\""
                                    dik "\"What the shit did I just hear?\""
                                    sze "\"Don't worry about it, recess is over, time for English\""
                                    jump english1
    elif _return == 2:
        "Kilgour"
        "You ceebs walk that far though"
        jump recess1a

    elif _return == 3:
        "R Quad"
        "You ceebs walk that far though"
        jump recess1a

    elif _return == 4:
        "Library"
        "You ceebs walk that far though"
        jump recess1a

    elif _return == 5:
        "Gym"
        "You ceebs walk that far though"
        jump recess1a

    elif _return == 6:
        "Canteen"
        "You ceebs walk that far though"
        jump recess1a

    elif _return == 7:
        scene bg dreamtree
        $ playmusic("p4Traumerei.ogg")
        "Valley"
        $ playsfx("wind.ogg", loop=True)
        "As you begin walking you can feel the breeze blowing up against your butthole"
        "While you enjoy yourself for a moment you bump into someone"
        $ playsfx("vpunch.ogg")
        "..." with vpunch
        "There you meet her, the one and only"
        "..."
        $ playsfx("mlady.ogg")
        "John Cena" 
        "..."
        "Not really its actually her"
        "Using your powers you are able to manipulate the fabric of reality"
        $ easterEggValley(rin)
        if rin.friendship >= 100:
            sze "I think I can now finally die happy"
            "..."
            call screen kms
        else:
            $ stopmusic()
            sze "Well I suck shit"
            "Even with the power of god within his physical body he still cannot slay Serena"
            "Your friendship with her is currently at [rin.friendship]"
            "Since you have now realised that you are a failure, you decide to go return back to the hall"
            jump recess1a

    elif _return == 8:
        "Oval"
        "You ceebs walk that far though"
        jump recess1a

    elif _return == 9:
        "Curry courts"
        "You ceebs walk that far though"
        jump recess1a

    elif _return == 10:
        "Basketball Courts"
        "You ceebs walk that far though"
        jump recess1a

    elif _return == 11:
        "Carpark"
        "You ceebs walk that far though"
        jump recess1a

    elif _return == 12:
        "Fort Street"
        "You ceebs walk that far though"
        jump recess1a

    elif _return == 13:
        "Bridge"
        "You ceebs walk that far though"
        jump recess1a

    elif _return == 14:
        "A random blob of green, popular with \romantic\" twinkies and other unimportant people"
        "You loiter there pointlessly"
        "Recess is over, time for next class"
        jump english1

    elif _return == 15:
        "Wilkins"
        "You ceebs walk that far though"
        "Even though that is right next to the Hall, sorta"
        jump recess1a

    elif _return == 16:
        "Fountain Quad"
        "You wait in fountain quad, long after the asszembly is ended, noting the mutilated Meleager..."
# nek minute new quest to look for the statue's... y'know, gigglestick and mothballs
        "Recess is over, time for next class"
        jump english1

    elif _return == 17:
        "Cohen"
        "You ceebs walk that far though"
        jump recess1a

    elif _return == 18:
        "Hall"
        "Why are you even staying here? Asszembly has ended"
        jump recess1a

    elif _return == 19:
        "Lower Kilgour Quad"
        "You ceebs walk that far though"
        jump recess1a

    elif _return == 20:
        "Lower Kilgour"
        "You ceebs walk that far though"
        jump recess1a

    elif _return == 21:
        "Upper Kilgour Quad"
        "You ceebs walk that far though"
        jump recess1a
