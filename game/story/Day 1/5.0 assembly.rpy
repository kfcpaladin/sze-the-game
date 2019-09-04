label asszembly1:
    $ autosave()
    $ stopmusic()
    $ playmusic("p4YouthfulLunch.ogg", loop=True)
    scene bg rowecorridor
    with fade
    sze "\"Time for my first assembly of the year\""
    wil "\"Indeed, I wonder whether Moxham will be here?\""
    pra "\"I'm finally free from the Engineering room...\""
    sze "\"Why not drop it?\""
    pra "\"Not just yet... I need to enact my revenge\""
    if game.yangRant is True:
        wil "\"That reminds me, Pragash, I have a proposal of sorts\""
        pra "\"What kind?\""
        wil "\"One that might facilitate for such an enactment of revenge, in return for a minor favour\""
        sze "\"Aaah, yes, indeed\""
        "Yang appreciates the backup, allowing Pragash to hear the proposal for his re-election into the SRC"
        $ wil.friendship += 1
        pra "\"Unfortunately, the SRC&PNC hate me, I will need something really hero from a PR team to pull this off\""
        pra "\"Otherwise, I would love to help\""
        wil "\"Hmmm... Arthur, I don't suppose you could be a good friend and help out here...\""
        menu:
            "\"Ok\"":
                sze "\"Ok\""
                pra "\"There's the Fortian spirit\""
                $ sze.fort += 1
                wil "\"My plan will come into fruition then\""
                pra "\"I owe much to the two of you then\""
                $ pra.friendship += 1
                sze "\"np\""
                $ game.electionPromise = True
                jump asszembly1p1
            "\"I'll pass\"":
                sze "\"I'll pass\""
                pra "\"Wow, what a little shit\""
                $ pra.friendship -= 1
                wil "\"Indeed\""
                $ wil.friendship -= 1
                sze "\"Calm down, fine\""
                $ game.electionPromise = True
                jump asszembly1p1
            "\"Play with vices\"":
                sze "\"I wanna play with vices\""
                wil "\"The fuck you talking about?\""
                sze "\"Nevermind\""
                $ sze.intellect -= 1
                pra "\"Just do it\""
                sze "\"...\""
                sze "\"fine\""
                $ game.electionPromise = True
                jump asszembly1p1
    else:
        wil "\"Why would you want to enact revenge upon engineering\""
        wil "\"It is the greatest subject to have ever existed\""
        pra "\"...You will never understand\""
        jump asszembly1p1

label asszembly1p1:
    dea "\"Hey guys, looking forward to assembly?\""
    wil "\"It would be un-Fortian to skip it\""
    pra "\"I hear Gary might be...\""
    "The conversation gets you thinking about your options..."
    #wil fuck you derek lol totes
    #wow calm down wil, plus I wrote it not derk ;)
    menu:
        "\"I need to put some stuff in my locker\"":
            jump asszembly1jigolo
        "\"Lol, actually ceebs skipping asszembly though\"":
            jump asszembly1_2

label asszembly1_2:
    scene bg hallentrance
    with fade
    sze "\"Lol, actually ceebs skipping asszembly though\""
    $ sze.fort += 1
    wil "\"You are true Fortian, Moxham would be proud of you\""
    sze "\"Really?\""
    wil "\"No, I don't think she cares\""
    show willis normal
    with dissolve
    kok "\"Arthur, my man!\""
    kok "\"Nice to see you all faggots\""
    kok "\"and Arthur, my friend, my rock, the Chosen One...\""
    sze "\"Eh?\""
    kok "\"you are the Uberfaggot\""
    sze "\"...\""
    sze "\"...Willis\""
    pra "\"Willis, I thought we were friends, how could you forget me?\""
    kok "\"I haven't, I just don't care\""
    hide willis normal
    with dissolve
    dik "\"Greetings and salutations to all and Willy la Willy\""
    kok "\"Fuck you\""
    dik "\"No thank you, I don't swing that way\""
    kok "\"Fuc- never mind\""
    pra "\"Tell you what fucks with the mind? Simple harmonic motio{nw}\""
    wil "\"I'm just revising simple harmonic motion and permutations and combinations\""
    wil "\"Don't worry, they're easy topics, ez 100 in tests\""
    pra "\"Teach me William, show me the way to your greatness...\""
    wil "\"Relax, just do 20,000 tests.\""
    kok "\"Tests? I think Chao should get one of his LGs to do one, make sure- {nw}\""
    $ playsfx("vpunch.ogg")
    cha "\"Fee\"" with vpunch
    $ playsfx("hpunch.ogg")
    cha "\"Fi\"" with hpunch
    $ playsfx("vpunch.ogg")
    cha "\"Fo\"" with vpunch
    $ playsfx("hpunch.ogg")
    cha "\"Fum\"" with hpunch
    show chao normal
    cha "\"Imma fuck you up the bum\""
    if game.chaoPissed is True:
        "Chao is blocking me"
        $ playsfx("vpunch.ogg")
        cha "\"I promised I would have my revenge...\"" with vpunch
        sze "\"Shit\""
        "You try to run but the crowd blocks you and Chao grabs you"
        sze "\"Aarrgh, fuck off, don't touch me\""
        $ playsfx("hpunch.ogg")
        cha "\"Huehue\"" with hpunch
        sze "\"Ow, fuck, my head...\""
        $ sze.intellect -= 1
        $ playsfx("hpunch.ogg")
        cha "\"Fuck your head? Ok\"" with hpunch
        sze "\"Nooo, raep, raep\""
        if dik.friendship > 0:
            $ stopmusic()
            $ playmusic("RaxlenSliceBG8bit.ogg")
            dik "\"Oi, fat ass, pick on people your own size, like Gabe Newell\""
            cha "\"Lemme think...\""
            cha "\"Nah...\""
            dik "\"My apologies, then\""
            cha "\"?\""
            $ playsfx("hpunch.ogg")
            dik "\"For {b}this{/b}\"" with hpunch
            cha "\"FUUUUUUCCCCKKKKK, what the shit was that?!?!?!\""
            dik "\"Steel cap work boots, bitch\""
            cha "\"Arrgh, don't make me angry\""
            dik "\"Don't make me make Chao Mein\""
            cha "\"...\""
            cha "\"Fuck off\""
            $ stopmusic()
            $ playmusic("p4YouthfulLunch.ogg", loop=True)
            hide chao normal
            "You observed how to some combat technique"
            $ sze.strength += 1
            jump asszembly1_3
        elif dik.friendship < 1:
            $ playsfx("vpunch.ogg")
            cha "\"I go full frontal\"" with vpunch
            $ sze.intellect -= 1
            sze "\"Aaah, plz stop\""
            cha "\"Why should I? Beg slave, you know you like it\""
            $ sze.intellect -= 1
            sze "\"No... No means no\""
            "Chao slams you down onto the ground"
            $ playsfx("vpunch.ogg")
            cha "\"I will ravage you to Chaoder\"" with vpunch
            $ sze.intellect -= 1
            $ sze.intellect -= 1
            $ sze.intellect -= 1
            sze "\"Raep, raep\""
            sze "\"I positively assert that no means no\""
            $ sze.strength -= 1
            "You faintly hear people shouting at Chao and through your blurred vision you can make out a crowd of people swarming Chao..."
            "The whities have heard you positively asserting yourself against Chao's desecration of your physical form, one is helping you up"
            "They praise the Fortianness of your actions"
            hide chao normal
            with dissolve
            $ sze.fort += 1
            "You proceed to weakly move your battered and bruised assemblage into asszembly"
            jump asszembly1_3
    else:
        cha "\"Hi\""
        rus "\"Oi, don't roast me\""
        cha "\"Chill, I'm just here to raep Pragga\""
        pra "\"No, fuck off...\""
        $ playsfx("hpunch.ogg")
        "You feel it best not to intervene" with hpunch
        "Despite Pragash's attempts to positively assert himself, the whites call him out for not accepting non-heterosexual practices"
        sze "They must've really hated him being on the Student Representative Council..."
        cha "\"Let's go in\""
        pra "\"...Nooo...not again\""
        cha "\"I meant the hall...\""
        hide chao normal
        jump asszembly1_3
label asszembly1_3:
    scene bg hall
    with fade
    $ stopmusic()
    $ playmusic("EscortsGaudeamusDooWop.ogg")
    "Gaudeamus igitur...something something...venit mors velociter, rapit nos atrociter..."
    mox "\"I would like to acknowledge the traditional owners of the land...\""
    sze "Wow, this is boring"
    menu:
        "Sleep":
            sze "\"I sleep\""
            sze "\"{i}I dream {/i}\""
            scene bg schoolfront
            $ playsfx("hpunch.ogg")
            $ _string = "{size=90}{b}{i}{rainbow}C.O.L.O.U.R.F.U.L.{/rainbow}{/i}{/b}{/size}"
            sze "[_string]" with hpunch
            $ playmusic("p4Traumerei.ogg")
            sze "I still remember the day I first met her"
            sze "It was the first school day of 2011, and I had just entered my dream high school, Fort Street High School"
            sze "\"I can't wait for a diligent 6 years of study, and to hopefully get an high ATAR and become a lawyer/doctor in USYD\""
            sze "\"How would I world peace and high distinction average simultaneously.\""
            sze "This thought confounds me, and compelled to Valley to commune with the spirits of Fortians past\""
            scene bg field
            with fade
            "\"{i}It is the duty of Fortians to protect indigenous rights {/i}\""
            "\"{i}Transgender rights are the key to a prosperous society {/i}\""
            "\"{i}Refugees will help propel Australia to a 0th World Country {/i}\""
            sze "\"I thank you for your sage wisdom, treasured spirits of Fortians Past\""
            sze "\"I decide to linger in this serene enviroment a little longer to rest my weary soul\""
            sze "And then I saw her"
            scene bg dreamtree
            $ playsfx("wind.ogg")
            sze "As she turned, the wind blew and her hair flowed around her"
            sze "The falling cherry blossom petals danced around her figure"
            sze "The twinkle in her eyes was as bright as Michael Kirby's ideals"
            sze "I knew then her name was Serena"
            $ stopsfx()
            scene bg hall
            sze "I had a dream, and it had water"
            sze "My pants are wet"
            $ sze.thirst += 1
            mox "\"How dare you wet your pants, when transgendered women in Siberia lack access to basic water facilities?\""
            $ game.moxCounter += 1
            $ sze.fort -= 1
            mox "\"Maybe a stint in detention will help you regain you Fortian Pride\""
            $ stopmusic()
            $ playmusic("EscortsGaudeamusDooWop.ogg", loop=True)
            mox "\"Continuing on from that distraction, let us think back to when Year of 1935 topped the HSC. I believe our current year has the potential to top James Ruse in both exit profile and academics\""
            "You hear Richard cough loudly"
            jump asszembly1_4
        "Talk":
            if game.electionPromise is True:
                call quest1electionpromise1_a
                jump asszembly1_4
            else:
                "But the silhouette of Serena, seated four rows ahead, catches your eye"
                "You watch as she gossips with Willis"
                $ sze.thirst += 1
                drk "\"wtf, are u drooling Arthur?\""
                "You notice Derek for the first time this year"
                sze "Derek is {s}a Machiavellian bastard{/s} an intelligent fellow {s}whose morals are as fluid as his loyalties{/s}"
                sze "shit, I need to make a convincing lie or something"
                $ game.metDerek = True
                menu:
                    "Stand up":
                        if sze.intellect >=4:
                            sze "Shit, better say something..."
                            sze "\" That's Bullshit!!!\""
                            "Everyone turns and looks at you"
                            sze "\"The academic inequality between Indigenous peoples and the rest of Australia is inherently related to the unequal global distribution of food\""
                            "You hear a wave of agreement and admiration wash over the entire hall"
                            show moxham happy
                            mox "\"Yes, yes indeed\""
                            mox "\"This is extremely relevant to the efforts to donate canned food to the families of the Charlie Hebdo shooting victims\""
                            mox "\"This man is epitome of Fortian\""
                            hide moxham happy
                            $ sze.charm += 1
                            $ sze.fort += 1
                            "You sit back down, basking in the glory of your social justice-ness"
                            dik "\"Wow, you commie hippy bastard\""
                            dik "\"I kid, that was some impressive bullshittery\""
                            sze "\"what do you mean \"bullshittery\"?\""
                            dik "\"{cps=*0.2}...{/cps}\""
                            $ dik.friendship -= 1
                            drk "\"Lol calm down, nice one Sze, so u were just drooling out of social justice\""
                            "You dodged a bullet there"
                            jump asszembly1_4
                        elif sze.intellect >=2:
                            sze "\"...\""
                            "People around you look expectantly at you"
                            sze "Shit forgot what I was going to say"
                            "You spend a few awkward seconds sweating like some craven pig in the middle of summer"
                            $ sze.charm -= 1
                            sze "\"urm...mumble need...toilet\""
                            drk "\"lolwut? why u drool even more?\""
                            sze "\"I need to go to toilet, wash hands\""
                            sze "Fuck that was awkward"
                            "you disappear into toilet for 20 minutes"
                            jump asszembly1_4
                        else:
                            $ playmusic("VarienThroneOfRavens.ogg")
                            $ playsfx("vpunch.ogg")
                            "You stand rooted to the spot, even as Moxham noticed you and stopped speaking" with vpunch
                            $ playsfx("vpunch.ogg")
                            "Your heartbeat starts irregularly racing" with vpunch
                            $ playsfx("vpunch.ogg")
                            sze "shit shit {nw}" with vpunch
                            $ playsfx("vpunch.ogg")
                            sze "shit shit {nw}" with vpunch
                            $ playsfx("vpunch.ogg")
                            sze "shit shit {nw}" with vpunch
                            "Your heart finally gives up as you die of embarrassment"
                            jump dead
                    "Deny all charges":
                        if sze.intellect >=2:
                            sze "\"I am merely salivating in anticipation of my recess which consists of leftover butter chicken\""
                            pra "\"Butter chicken is good but rogan josh is better\""
                            sze "\"That was ordered from the restaurant two days ago\""
                            drk "\"Wait why u even order from Indian restaurant?\""
                            sze "\"It was more Hong Kong/Indian/Italian/American fusion\""
                            pra "\"wtf\""
                            sze "\"I am accepting to new ideas because of my Fortianness\""
                            $ sze.fort += 1
                            pra "\"That almost makes annoys me as much as Desney being on SRC\""
                            "You see that this has caught the attention of Will Yang\""
                            wil "\"Perhaps you might be persuaded to run?\""
                            pra "\"But they hate me on the SRC\""
                            wil "\"I hear Wesley is planning on running\""
                            wil "\"If not you then Wesley...\""
                            pra "\"Then I need assistance\""
                            "They disrupt your gazing at Serena by asking if you would render aid"
                            menu:
                                "\"Szeebs\"":
                                    sze "\"Szeebs tho\""
                                    $ pra.friendship -= 1
                                    wil "\"I had higher expectations for you, you are disappointment\""
                                    $ wil.friendship -= 1
                                    jump asszembly1_4
                                "\"K\"":
                                    sze "\"K\""
                                    "You talk more with them to discuss plans before Yang turns away"
                                    sze "I have idea...maybe Derek and Rick have better idea for this"
                                    $ game.electionPromise = True
                                    call quest1electionpromise1_a
                                    jump asszembly1_4
                        else:
                            sze "\"I wasn't drooling tho\""
                            drk "\"You definitely were drooling\""
                            sze "\"But I wasn't\""
                            drk "\"you were\""
                            dik "\"You definitely were\""
                            pra "\"You were\""
                            drk "\"If you think about it, you were\""
                            sze "\"Nooo...why you be like this?\""
                            $ sze.charm -= 1
                            "You spend the next few minutes insisting that you weren't drooling"
                            jump asszembly1_4

        "Pay attention":
            "30 minutes later"
            mox "\"Michael Kirby is great, let us worship Michael Kirby\""
            "You worship Michael Kirby, allowing yourself to absorb the power of social justice"
            $ sze.fort += 1
            "40 minutes later"
            jump asszembly1_4

label quest1electionpromise1_a:
                "You turn to talk to Derek and Richard"
                pra "\"urgh...\""
                "You are reminded of your quest"
                sze "\"I wonder what it would be like for Pragash to be on the SRC...\""
                dik "\"Wow, that is an interesting idea\""
                dik "\"And retarded at the same time\""
                pra "\"Hey, I heard that\""
                drk "\"Well actually, we could probably make this work. First, identify likely opponents.\""
                if game.metDerek is True:
                    return
                else:
                    sze "{cps=*1.5}Derkie Derk has high pitch wail like Willy and Chao{/cps}{nw}"
                    sze "Derek is {s}a Machiavellian bastard{/s} an intelligent fellow {s}whose morals are as fluid as his loyalties{/s}"
                    $ game.metDerek = True
                    return
                drk "\"There are many but we focus on getting him a nemesis and then lock on\""
                dik "\"Then spin policy which will get him elected\""
                drk "\"Sigh... you conservatives... Character attacks are the only ways to guarantee election\""
                dik "\"But surely he needs to be able to back up his attacks with something of substance\""
                "You have an epiphany"
                $ sze.intellect += 1
                sze "\"Maybe, we can get together a campaign team...\""
                pra "\"Is that even necessa{nw}\""
                drk "\"Good idea\""
                sze "\"How about I get a bunch of guys to work with Pragash to figure out policy, so that he can debate\""
                dik "\"First he needs to figure out how to debate...\""
                pra "\"Like a Rap battle\""
                drk "\"Indeed, something which the populace can relate and rally to\""
                dik "\"What will we do?\""
                sze "\"Both of you lead the attack with PR\""
                dik "\"Make Pragash the Vox Populi\""
                dik "\"Yes... and then we cross the Rubicon {nw}\""
                dik "\"erm, the bridge from Kilgour to Wilkins building- and force them to flee...\""
                drk "\"Figuratively, of course, yes?\""
                dik "\"errr.....\""
                pra "\"Thanks all of you\""
                $ pra.friendship += 1
                pra "\"By the way, have you heard that Chelsea destroyed ManU last night\""
                dik "\"I was just watching news about that. The cricket match was most intense\""
                pra "\"OMFG\""
                dik "\"I jest\""
                dik "\"or do I?\""
                "You should relay this news to William Yang - he is currently engaged in conversation with his hand"
                "You engage in mindless conversation with Richard, Derek and Pragash"
                return

label asszembly1_4:
    mox "\"It's ok if half the previous year's Year 12 got band 3, Fortians are the epitome of social justice and exit profile\""
    mox "\"Quoting some Latin 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Pedicabo ego vos et irrumabo.' There is more to high school than ATAR\""
    "20 minutes later"
    sze "\"Well that was fucking useless\""
    $ sze.fort += 1
    wil "\"Pah, all this talk of helping the community; only I know of what must be done for the greater good\""
    jump recess1
