# first english class testing
label english1:
    $ clock.set_time("lunch")
    $ autosave()
    scene bg english
    "You arrive at {s}base camp{/s} ground floor of Wilkins"
    "You look up at the stairs, into the gaping maws of the infinite abyss"
    sze "Am I even bothered enough for this?"
    menu:
        "Fuck this shit, I'm out":
            $ sze.fort -= 1
            sze "I don't want to risk a heart attack"
            "You start turning around"
            "And stop before the forboding form of Moxham"
            mox "\"Well, well, well\""
            mox "\"You wouldn't happen to be turning away from your class, now, would you?\""
            menu:
                "I would":
                    sze "\"Yea, so what?\""
                    mox "\"So I'll extend to you an invitation to visit my {s}secret dungeon{/s} office after school\""
                    sze "\"Oh...\""
                    mox "\"But you were being honest, so if you turn around now, I might forgive you, just this once\""
                    sze "Damn, that was close"
                    jump eng1ascension
                "I wouldn't":
                    sze "\"N-n-no\""
                    mox "\"You lie\""
                    sze "\"ah, I, uh, wuz just, ah, going to go t-to the t-toilet... yeah, that's what I was doing\""
                    mox "\"Well, you do like you are about to piss yourself\""
                    $ sze.strength -= 1
                    mox "\"I expect you to be back here in 5 minutes, otherwise there will be consequences\""
                    sze "\"erm...'kay\""
                    "You have no choice but to comply"
                    jump eng1ascension
        "I actually need to pass":
            "You take a deep breath and {s}gather your qi{/s} mentally prepare yourself for the brutal climb"
            sze "I need to be {b}smart{/b} about this and {b}strong{/b} enough to make it successfully"
            jump eng1ascension

label eng1ascension:
            sze "Can't be too hard, just put one foot in front of the other"
            "..."
            sze "\"Just keep swimmin'\""
            "You notice Dean walk past you"
            dea "\"man, these steps are pretty stupid. We should just use rockets\""
            "..."
            sze "\"One flight down, three to go\""
            "..."
            sze "\"I can do this\""
            if sze.intellect > 5:
                "You notice Richard walk past you"
                sze "\"If Pheidippides of Athens could run from Marathon to Greece, I can get up these steps\""
                dik "\"Quite so, my good fellow! Persevere but a few seconds longer, then \"Joy to you, we've won\"!\""
                $ dik.friendship += 1

            else:
                "You notice Richard walk past you"
                sze "\"if that greek guy could do that mara thing, then I can do these stairs too\""
                "You notice Richard shaking his head"
                dik "\"I almost pity thee. Thine incompetence is but a miracle beholden to few\""
                $ dik.friendship -= 1

            "..."
            "The second flight was down, half way"
            "You find yourself at the first floor, and allow yourself one second of respite"
            "Gary/Jitian staggers past"
            jit "\"Phew, good thing I have Strauss for English. This is as high as I need to go; sucks to be everyone else\""
            sze "\"lucky\""
            "..."
            "You pass by Chao, who, despite his girth, appears to be doing rather well"
            if cha.friendship > 1:
                cha "\"Hey Arthur, how's it going?\""
                sze "\"im fking dying\""
                cha "\"Y'know, since you had my back earlier on, I reckon I'll help you out. Aren't I a great guy?\""
                menu:
                    "\"im fking ded, halp me plz\"":
                        cha "\"Alright then, just stay put and I'll get you to the top in no time.\""
                        "Chao suddenly grabs you by the back of your shirt and dangles you over the edge of the building"
                        "He gets into a lopsided shotput pose"
                        $ sze.strength -= 1
                        cha "\"3\""
                        cha "\"2\""
                        cha "\"1\""
                        $ _englishstairs1rngthrow = renpy.random.randint(0, 6)
                        if _englishstairs1rngthrow > 4:
                            sze "\"Wait stop, let me down!!!!!\""
                            "You get launched through the air, rapidly reaching the top floor of the stairs" with vpunch
                            "However, you find yourself shooting past it"
                            "You continue going upwards"
                            "..."
                            "You have already expelled your bowel and bladder contents"
                            "..."
                            "The air is becoming rather thin, making it less easy to constantly scream"
                            "..."
                            "You are unsure if you are starting to drop or still continuing into the infinite blue expanse"
                            "..."
                            "You close your eyes and give up on life"
                            jump dead
                        elif _englishstairs1rngthrow >2:
                            sze "\"Wait stop, let me down!!!!!\""
                            "You get launched through the air, rapidly reaching the top floor of the stairs" with vpunch
                            "Despite the unusual and potentially dangerous method of travel, you do feel quite thankful to Chao."
                            "You lean over the edge and shout a few words to him"
                            sze "\"I don't know if I could've done the rest without a heart attack\""
                            cha "\"Oops I didn't let you down\""
                            sze "\"Thanks Chao, you are truly a great man\""
                            cha "\"Awww thanks Arthur\""
                            sze "\"Your heart is as big as you are\""
                            cha "\"...\""
                            cha "\"k\""
                            $ cha.friendship += 1
                            jump english1top
                        elif _englishstairs1rngthrow <= 2:
                            "You get launched through the air, rapidly reaching the top floor of the stairs{nw}"
                            "But Chao didn't throw hard enough"
                            "Your fingers desperately grasp at, first, the metal railings, then, the concrete wall beneath it, then, anything at all"
                            "But your flailing attempts, like your chances with Serena, slip from your failing hands"
                            sze "\"Fuuuuuuuuuuuuuuucccckkk yooooooouuuuuuuuu chhaaaaaaaaaaaaoooooooo\""
                            cha "\"Fuuuuuuuuuuuuuuucccckkk yooooooouuuuuuuuu toooooooooooooooooooooo\""
                            dik "\"{i}He hit the ground, the sound was \"SPLAT\", his blood went spurting high{/i}\""
                            dik "\"{i}His comrades, they were heard to say \"A HELL OF A WAY TO DIE!\"{/i}\""
                            dik "\"{i}He lay there, rolling 'round in the welter of his gore,{/i}\""
                            dik "\"{i}And he ain't gonna jump no more.{/i}\""
                            jump dead
                    "\"thanks but nah\"":
                        sze "\"thanks for the offer\""
                        sze "\"but nah\""
                        sze "\"I\""
                        sze "\"must\""
                        sze "\"overcome\""
                        $ sze.strength += 1
                        cha "\"gotta respect\""
                        cha "\"strength of body and of character\""
                        cha "\"and strong of body odour too...\""
                        $ sze.charm -= 1
                        cha "\"anyway, cya\""
                        jump english1flight3
            else:
                cha "\"Oh look who it is\""
                sze "\"uhh...hi chao\""
                cha "\"I'm tired\""
                sze "\"...\""
                sze "\"yeh so? aren't we all?\""
                cha "\"So i think i'll ride you\""
                "Before you can reply, he has hurled himself onto your back"
                if sze.strength >= 2:
                    "Somehow you manage to stay upright"
                    cha "\"giddyup horsie\""
                    sze "\"Urghgerroffyoufuglypoofter\""
                    cha "\"Save your energy, don't speak, just climb\""
                    "..."
                    "You get to the top of the third flight and decide to throw Chao off"
                    cha "\"Oi slave, what do you think you're doing?!\""
                    sze "\"You know you aren't cool doing that, right?\""
                    cha "\"Oh, tell me, why not?\""
                    menu:
                        "Exacerbate his insecurities":
                            sze "\"Cos all you're doing is proving that you're a chubby ass mofo\""
                            "You notice Dean and Richard nearby"
                            dea "\"Oh shit, good burn\""
                            dik "\"I doth doff my hat at thee, twas a well placed blow\""
                            $ sze.charm += 1
                            cha "\"...\""
                            cha "\"gotta admit that was a good burn\""
                            cha "\"But perhaps you might be the one to help me make peace with my weight\""
                            cha "\"mebe you truly are The Chosen One\""
#                           include new quest - help chao lose his weight, pt.1 -> making peace with his weight
                            cha "\"Until next time, cya\""
                            $ cha.friendship += 1
                            jump english1flight3
                        "Destroy his dignity":
                            if sze.intellect > 3:
                                sze "\"Clearly, ur desire to make me carry u is due to a desire to dominate\""
                                sze "\"This must be cos you get dominated by other people, but clearly not at school\""
                                cha "\"...\""
                                sze "\"Therefore, it must be in home environment\""
                                sze "\"So either ur gf dominates you or ur family does\""
                                sze "\"well?\""
                                sze "\"r u getting dominated by a LG?\""
                                sze "\"r u getting rekt by ur daddy?\""
                                sze "\"or is mummy expressing her desire for Oedipus complex by whipping ur ass?\""
                                cha "\"stfu, I'll remember this\""
                                sze "\"All of the above?\""
                                $ cha.friendship -= 1
                                "The people around you go quiet"
                                dea "\"That was fucking savage. Dunno, man, but you might've gone too far\""
                                dea "\"Still, those are good burns\""
                                $ sze.charm += 1
                                jump english1flight3
                            elif sze.strength > 2:
                                sze "I would try something witty, but I'm probs not smart enough to do that this quickly"
                                sze "Looks like all I can do is use my fists then"
                                cha "\"Well?\""
                                sze "\"i'll let my fist explain\""
                                "You only have one shot at this"
                                "You feel time slowing down as you pull your elbow back"
                                sze "This is gonna be hard; I'll need to punch Chao for a combat score of 12, to do anything"
                                $ _english1stairspunchchao = renpy.random.randint(0, 6) + int(sze.strength)*2 + int(sze.intellect)
                                "Your fist flies forward, with a combat score of [_english1stairspunchchao]"
                                if _english1stairspunchchao > 11:
                                    "!!!"
                                    $ playsfx("hpunch.ogg")
                                    with hpunch
                                    sze "shit"
                                    "Chao has caught your fist"
                                    sze "\"welp\""
                                    sze "\"Do what you will\""
                                    cha "\"You tried\""
                                    cha "\"Gotta respect\""
                                    "He releases your fist, and extends his hand"
                                    sze "\"Ok\""
                                    $ cha.friendship += 1
                                    jump english1flight3
                                else:
                                    "!!!"
                                    $ playsfx("hpunch.ogg")
                                    with hpunch
                                    "Chao stumbles back, holding his jaw"
                                    cha "\"You...\""
                                    "He jabs you a few times"
                                    cha "\"Omae Wa Mou Shindeiru\""
                                    sze "\"{i}N-Nani{/i}?!\""
                                    "You explode"
                                    jump dead
                            else:
                                sze "shit"
                                sze "so...how am I supposed to destroy his dignity"
                                sze "Would dignity even exist outside of society and social interaction?"
                                sze "Why must we have the inalienable right to be valued and respected?"
                                $ sze.intellect += 1
                                sze "Do we deserve it?"
                                cha "\"Well?\""
                                sze "\"umm\""
                                sze "\"You're a dumbfuck\""
                                cha "\"lol\""
                                cha "\"Nice try\""
                                cha "\"Pretty sure you're more lacking in the mental department\""
                                sze "\"eh?\""
                                cha "\"I think I should put you out of your misery\""
                                sze "\"So you'll make me happy then?\""
                                "He jabs you a few times"
                                cha "\"Omae Wa Mou Shindeiru\""
                                sze "\"what?!\""
                                "You explode"
                                jump dead
                else:
                    "Unfortunately, your knees are weak, palms are sweaty"
                    $ playmusic("VarienThroneOfRavens.ogg")
                    "You are instantly flattened"
                    sze "\"gluuurrg-\""
                    "Your breath is pushed out of you, but Chao's mass prevents you from taking another"
                    "Your ribs are almost certainly shattered, your sternum faring no better"
                    "Even if you could take a breath, both of your lungs have already collapsed due to the multiple punctures"
                    "You feel blood filling your thoracic cavity, with each weakening pulse"
                    "In some distant space, through the fading light, you can hear Chao"
                    cha "\"Hey Arthur, cool prank, you can get up now\""
                    sze "i would if i could you fking fgt"
                    jump dead
label english1flight3:
    sze "3 out of 4"
    sze "75 percent"
    sze "I can do this"
    sze "\"arrggfuqtootired\""
    sze "\"One foot\""
    sze "\"in front\""
    sze "\"of the\""
    sze "\"other\""
    "As you trudge along, you see her"
    "Her radiant form inspires and stimulates you"
    $ sze.thirst += 1
    "And gives you strength"
    $ sze.strength += 1
    "Your heart is pumping, freshly oxygenated blood coursing through your body"
    if sze.thirst > 3:
        "You surge forward, with surefooted and steady steps, despite your nausea"
        "Your heart is racing"
        "You reach out, hoping to say something, anything to her. You have a pressure in your chest that you just need to get rid of."
        "The sound of your blood rapidly throbbing in your ears is all you hear"
        "You know, in this moment, you are no longer paralyzed by fear. You can talk to her, tell her how you feel {nw}"
        "Your heart rate, so fast, it simply quivers"
        sze "\"gaaa-\""
        "Your heart stops"
        if wil.friendship > 40:
            wil "\"lol, you idiot, you've overexerted yourself\""
            wil "\"I still need you around, so I can't let you die of a heart attack\""
            "Your consciousness is fading"
            "You hear Will say something vaguely"
            "There appears to be something going on in the background"
            wil "\"Well, here goes\""
            wil "\"Clear\""
            $ playsfx("vpunch.ogg")
            with vpunch
            sze "\"-aargh\""
            wil "\"Surprised that worked\""
            "Your blurry vision makes out a few battery shaped objects, connected to a big spring shaped thing"
            "Wires join the otherwise disconnected bits and pieces, with two leading to two accupuncture needles sticking near your right shoulder and left armpit"
#           can include random advanced quiz question
            wil "\"Well, you should be good to go\""
            wil "\"cya around\""
            jump english1top
        elif pra.friendship > 1:
            pra "\"Whoa, Arthur are you dead?\""
            sze "\"-aargh\""
            pra "\"Is that a yes or a no?\""
            sze "\"Huurgh\""
            pra "\"I think that's a yes\""
            "You aren't too sure what's going on, but you think you see Pragash deliberately prick his own finger"
            pra "\"Ouch\""
            pra "\"{i}Kuchiyose: Karegyangu{/i}\""
            sze "I must be dreaming"
            "{s}Curries{/s} People clearly of sub-continental descent appear around Pragash"
            pra "\"Thanks for appearing on such short notice, my dudes\""
            "Your consciousness fades"
            "..."
            sze "I'm taking a long time to die"
            sze "But is this dying?"
            sze "I feel too energetic"
            "..."
            "You can sense a form of life energy flowing into you"
            sze "I blink"
            sze "I sze"
            sze "\"Errm...why is there a bunch of guys putting there hands on me?\""
            pra "\"Brothers, it seems our work here is done\""
            pra "\"{i}kai{/i}\""
            "All the {s}Curries{/s} people of sub-continental descent disappear, as you blink"
            pra "\"I'll explain some other time, for now, I do believe we have English\""
            jump english1top
        else:
            wil "\"Lol, you look kinda funny\""
            sze "\"-rgh\""
            pra "\"Whoa, shit it moved\""
            pra "\"Dead bodies shouldn't move\""
            pra "\"Kill it dead\""
            jump dead
    else:
        "But you control your heart, and decide to approach some other time"
        $ sze.thirst += 1
        "..."
        jump english1top
label english1top:
    "Captain's report, {s}February 4th, 2531{/s} January 28th, 2015"
    "{s}Five year, five long years.{/s} 5 minutes, 5 long minutes. That's how long it took to get {s}Harvest back{/s} to the top."
    "At first it was going well...{s}then setback after setback, loss after loss...{/s} step after step, sweat after sweat..."
    "Made what was going to be a {s}quick and decisive win{/s} normal journey to class..."
    "Into five minutes of hell..."
    "..."
    sze "I'm here"
    sze "On time"
    sze "Now who are my classmates?"
    "You aren't too familiar with a lot of the people"
    "However there are some who you do recognise"
    sze "Roy is pulling off fancy tricks with his yoyo, occasionally messing up"
    sze "Andrew is talking to someone you remember from a while ago..."
    sze "whatshisname?"
    sze "crap"
    sze "I think he's waving to me?"
    sze "\"Hi...uh...?\""
    menu:
        "Stefan":
            sze "\"Hi Stefan\""
            dng "\"lol, when did you get a lisp?\""
            sze "\"...Ahem\""
            sze "\"I meant Steven\""
            dng "\"lol Arnold, you didn't forget my name did you?\""
            menu:
                "Bitch forgot my name?!":
                    sze "\"Bitch forgot my name?!\""
                    dng "\"Says you\""
                    lee "\"Arguing like an old married couple already\""
                    sze "\"Steven is baka-desu\""
                    dng "\"Nani?! U wanna die mate?!\""
                    $ dng.friendship -= 1
                    lee "\"Lol, both of you are fucking weebs\""
                    sze "\"N-no\""
                    dng "\"N-no\""
# maybe include a weaboo stat?
                    lee "\"I can see it in your eyes\""
                    lee "\"You've both been looking for each other\""
                    sze "\"!!\""
                    dng "\"S-Shut up\""
                    $ sze.thirst += 1
                    lee "\"Be manly like JoJo\""
                    dng "\"dafuq, you were just calling us weebs\""
                    sze "\"Yes! u r fking weeb, Andrew\""
                    lee "\"Oh...I admit, it's true\""
                    jump eng1waitforschlammie
                "Actually it's Arthur":
                    sze "\"You meant Arthur, right?\""
                    dng "\"Ahem, yeah, yeah\""
                    dng "\"Totes remembered your name {s}Arnold{/s} Arthur\""
                    "It seems we have come to a mutual understanding to never bring this traumatic incident up ever again{nw}"
                    lee "\"Lol, it seems both of you bunyips has forgotten the other's names\""
                    dng "\"Actually that's not true, right {s}Arnold{/s} Arthur?\""
                    "You nod your head vigorously"
                    lee "\"Then what were you talking about previously?\""
                    menu:
                        "Roy":
                            sze "\"we were talking about Roy\""
                            lee "\"Then who, in the name of all the krill in the world, is Arnold?\""
                            dng "\"fking idiot sze\""
                            $ sze.intellect -= 1
                            sze "\"Steven is baka-desu\""
                            dng "\"Nani?! U wanna die mate?!\""
                            lee "\"Arguing like an old married couple already\""
                            lee "\"Except you're both a bunch of old married weebs\""
                            sze "\"...\""
                            dng "\"...\""
                            sze "\"We should just murder him\""
                            dng "\"Yup\""
                            dng "\"rofl\""
                            sze "\"wot?\""
                            sze "\"Who even says 'rofl' before a fight?\""
                            lee "\"Who even says 'rofl'?\""
                            dng "\"oi, fk off both of you\""
                            "You are about to engage in a three-way argument\""
                            roy "\"Hey guys, I heard you mention my name\""
                            sze "\"uhhh...did we?\""
                            dng "\"fgt, you were the one who mentioned it two minutes ago\""
                            roy "\"Well, if you wanna talk about me, why not include the most qualified expert on the topic\""
                            roy "\"Namely me\""
                            lee "\"You're no expert on yourself\""
                            roy "\"Really? How so?\""
                            lee "\"I bet you haven't even used your left elbow to touch the back of your right knee while standing on your left leg\""
                            "You all amuse yourselves with watching Roy engage in an exercise in futility"
                            $ lee.friendship += 1
                            $ dng.friendship += 1
                            $ roy.friendship += 1
                            roy "\"Aaaargh!!!\""
                            roy "\"Is this even possible?\""
                            lee "\"I saw Frank Dwyer do it before, maybe you should try this instead...\""
                            jump eng1waitforschlammie
                        "Our families":
                            sze "\"Deng and I were merely discussing our families, and what we did over the holidays\""
                            dng "\"uh....yeah. Yes we were\""
                            sze "\"In fact, you may have heard Steven mention my brother Arnold\""
                            dng "\"Please continue talking about Arnold, before Andrew most rudely interrupted us\""
                            lee "\"My most sincere apologies\""
                            lee "\"My children will serve your children as servants for the rest of their lives\""
                            sze "\"Errr...as I was saying\""
                            sze "\"My brother is an autistic savant\""
                            dng "\"Wait legit? what is he savant at?\""
                            sze "\"He's a financial extraordinaire, which is why he is with my parents on their 8-year business trip overseas\""
                            dng "\"Legit? So you live alone?\""
                            sze "\"Well, I'm staying in my aunt's investment property in Burwood, but yeah, I live alone, pretty much\""
                            lee "\"That makes you, like, every anime and visual novel protagonist that ever existed\""
                            sze "\"huh, never thought about it that way\""
                            "That was a lie, of course. Otherwise, why else would you have someone narrating your life?"
                            sze "Good point, voice-in-the-head"
                            jump eng1waitforschlammie
                        "Vices":
                            sze "\"We were merely talking about vices\""
                            dng "\"dafuq? we were?\""
                            lee "\"Tell me, Deng, what vices were you two talking about?\""
                            dng "\"Ummm, well, errr, hmmm, help me out a bit Arthur? the, uhh, that vice, umm, {nw}\""
                            lee "\"Specifically the Arnold vice\""
                            dng "\"fuck, ahhh, help me explain, plz Arthur?\""
                            sze "\"nah, I thought I did already, you're just a bad listener\""
                            dng "\"Oh wait, I remember now\""
                            sze "\"err...you do?\""
                            dng "\"Yeah, Arthur stand over there\""
                            sze "\"sure\""
                            "Deng walks up behind you"
                            lee "\"well?\""
                            dng "\"The Arnold Vice Grip is a wrestling move\""
                            "You are starting to feel rather uncomfortable, all of a sudden"
                            dng "\"Basically, you grip the opponent's head, like so, between both hands\"" with hpunch
                            dng "\"Then you shout in an Austrian accent \"Hasta la vista\" and push your elbows against their shoulders, and pull their head up\""
                            "You are feeling extremely uncomfortable with the way that this is going"
                            dng "\"Which results in your simultaneously disconnecting their head from their body, and crushing their head, like so\"" with vpunch
                            dng "\"oops\""
                            jump dead
        "Steven":
            sze "\"Hi Steven\""
            dng "\"Hey Arthur\""
            $ dng.friendship += 1
            sze "I have sucessfully navigated the treacherous waters of social conduct"
            sze "Surely I deserve to have an extra charisma point?"
            "Does sze deserve an extra charm point for remembering an acquaintance's name?"
            menu:
                "Yeah, sure":
                    "But he {i}was{/i} an acquaintance to begin with"
                    "So will you reconsider?"
                    menu:
                        "He still deserves it":
                            "Aah, sticking to your guns"
                            "Very well"
                            $ sze.charm += 1
                            "But know this; true Fortians hate guns"
                            $ sze.fort -= 1
                            sze "Can I have my headspace back, mr. narrator, and mr. random-other-observer?"
                            sze "thanks"
                            sze "wait..."
                            sze "I gained charm?"
                            sze "\"YES!\""
                            dng "\"eh?\""
                            sze "\"errr...\""
                            sze "\"I was just pumped for English\""
                            dng "\"lmao\""
                            jump eng1waitforschlammie
                        "Maybe...idk":
                            "Maybe?"
                            "Fuck you, I don't want to pick for you"
                            $ sze.fort -= 1
                            $ sze.charm -= 1
                            $ sze.thirst += 1
                            "Next time be more decisive"
                            "Now continuing on with the Life of Sze"
                            sze "Oh what the hell?"
                            sze "Oi, you what?"
                            sze "please give me my mental space back"
                            sze "before you screw me over even more"
                            sze "\"Anyhow, Steven, what were we talking about again?\""
                            dng "\"err...bruh, we just said hello\""
                            sze "\"oh...\""
                            dng "\"lmao\""
                            jump eng1waitforschlammie
                        "No, he's scum":
                            "I'd say that's a bit harsh, whether or not he ends up that way is dependent on your guidance"
                            "Nonetheless, such adherence to social justice is an aspect of the Fortianness"
                            $ sze.fort += 1
                            "But since you agree to him being penalised"
                            $ sze.charm -= 1
                            $ sze.thirst -= 1
                            sze "Oi, you what?"
                            sze "please give me my mental space back"
                            "Ok"
                            dng "\"Why do you look like you were talking with someone?\""
                            sze "\"errrrrr...\""
                            lee "\"It's fine, I do it all the time\""
                            lee "\"Really brings out the \"mental\" in mental conversation\""
                            sze "\"N-n-no, I was just getting myself psyched up for English\""
                            lee "\"See? Sze really is loopy\""
                            jump eng1waitforschlammie
                "Maybe":
                    "Maybe?"
                    "Fuck you, I don't want to pick for you"
                    $ sze.fort -= 1
                    $ sze.charm -= 1
                    $ sze.thirst += 1
                    "Next time be more decisive"
                    "Now continuing on with the Life of Sze"
                    sze "Oi, you what?"
                    sze "please give me my mental space back"
                    sze "before you screw me over even more"
                    sze "\"Anyhow, Steven, what were we talking about again?\""
                    dng "\"err...bruh, we just said hello\""
                    sze "\"oh...\""
                    dng "\"lmao\""
                    dng "\"Anyways, how were your holidays?\""
                    jump eng1waitforschlammie
                "Honestly, no":
                    "I'm glad that you have picked the Fortian choice"
                    $ sze.fort += 1
                    "But since you're so sure of penalising Arthur"
                    $ sze.charm -= 1
                    sze "Seems fair, but I'd rather charisma over fortianness for now"
                    sze "After all, it looks more useful when trying to win over Serena"
                    "Sounds like someone is thirsty"
                    $ sze.thirst += 1
                    sze "\"fuck\""
                    dng "\"eh?\""
                    dng "\"Did I fuck up your name?\""
                    dng "\"Oh shit, I thought it was Arthur\""
                    dng "\"err..Arnold, was it? Or is it Adam? Aaron? no, that's not it{nw}\""
                    sze "\"Nah, you were right first time\""
                    dng "\"Oh...so why say \"fuck\"?\""
                    dng "\"It's not like I swing that way, I'm straight as a walking cane\""    
                    lee "\"Obviously, he was thinking about how he feels like a puppet on the strings of Fate\""
                    dng "\"Wow, so deep\""
                    dng "\"That's the way I like it\""
                    jump eng1waitforschlammie
        "Esteban":
            sze "\"Hola Esteban\""
            dng "\"lmao when did you get so Spanish?\""
            sze "\"¿que pasa con hablar en espanol, cholo?\""
            dng "\"I don't understand, but you called me gangster\""
            dng "\"Thanks, bruh\""
            $ dng.friendship += 1
            sze "\"no hay problema\""
            dng "\"So...you're a farmer now?\""
            sze "\"eh?\""
            dng "\"what was that about problems with hay?\""
            sze "\"idk, I don't Spanish\""
            dng "\"What? But you were clearly{nw}\""
            lee "\"Clearly, the French language is better than Spanish\""
            sze "\"Errr...do you even speak French?\""
            lee "\"{i}Aide-de-camp in lieu de double entendre{/i}\""
            sze "\"Seems legit\""
            lee "\"{i}Je suis exhausted{/i}\""
            jump eng1waitforschlammie

label eng1waitforschlammie:
    "You find yourself engrossed in idle banter with Andrew Lee and Steven Deng"
    sze "\"huh...is it just me or is our teacher late?\""
    dng "\"nah, you're right, dunno what Schlam is doing\""
    lee "\"Probably listening to a German band dressed as Mongolians singing about Russia\""
    sze "\"ho-ho-ho-ho-ho, hey!\""
    dng "\"Eh?\""
    dng "\"Is it metal?\""
    lee "\"Nah, who even listens to metal?\""
    dng "\"Oi mate wanna go?\""
    "How to prevent this escalation to total war?"
    menu:
        "With calm and reason":
            sze "\"Guys just chill\""
        "By redirecting their anger towards yourself":
            "After being brutally molested as a child, you cannot bear the anger of others"
        "Look for the nearest teacher":
            "You hear the sound of gigantic footsteps reveberate towards you"
        "Blame Roy for everything":
            sze "Hey guys I think {b}Roy{/b} just {color=[PrimaryColours.GREEN]}{b}{i}farted{/i}{/b}{/color}"
    $ playsfx("vpunch.ogg")
    $ _string = "{b}{grow}THUD{/grow}{/b}"
    "[_string]" with vpunch
    $ playsfx("hpunch.ogg")
    $ _string += "{b}{grow}THUD{/grow}{/b}"
    "[_string]" with hpunch
    $ playsfx("vpunch.ogg")
    $ _string += "{b}{grow}THUD{/grow}{/b}"
    "[_string]" with vpunch
    sze "\"Uhhhh\""
    slm "\"Stop blocking the way, moving quickly now\""
    "You are nearly bowled over by a short, anthropomorphic tornado"
    "It moves with such vigour, you can only register a blur"
    "Or maybe that's just your bad eyesight"
    "Should've gone to Specsavers"
    sze "Ahem, narrator? Please get on with it"
    "You are wondering why it's still movin{nw}"
    slm "\"Right, I am excited to see how you lovely kids will-{nw}\""
    $ playsfx("vpunch.ogg")
    slm "\"If\"" with vpunch
    $ playsfx("hpunch.ogg")
    slm "\"This\"" with hpunch
    $ playsfx("vpunch.ogg")
    slm "\"Bloody\"" with vpunch
    $ playsfx("hpunch.ogg")
    slm "\"Door would just open!!\"" with hpunch
    "The short anthropomorphic tornado gave the door a futile kick before spinning off in the direction of the office"
    sze "...k"
    "Another few minutes pass, students engross themselves with idle banter"
    "The short anthropomorphic tornado returns with the exasperated-looking groundsman/cleaner"
    "Bill the Groundsman takes a huge keyring loaded with keys, of all shapes and sizes out of his trench coat"
    "Within a second, he picks out one of the more generic looking keys."
    "With a twist and a click, the door opens."
    bil "\"See? That's your problem. You got the wrong key {s}again{/s}\""
    "The short anthropomorphic tornado stopped spinning"
    "It throws its arms in the air and looks incredulous"
    slm "\"Bahahahahahaha!!\""
    slm "\"Alright, time to get the show back on the road\""
# include scene change and stuff
    slm "\"Ok, get yourselves seated. I see some familiar and unfamiliar faces.\""
    "Schlam appears to be a somewhat aged, short, slightly round, Caucasian woman; a benign, humoured individual."
    slm "\"Good, good...ah...\""
    slm "\"Get used to your seating arrangements, you'll be staying in them for the rest of the year, otherwise I will forget your name\""
    slm "\"Unless you do drama, in which case there's a deus ex machina making me remember your name\""
    roy "\"B-b-b-but what about me???\""
    slm "\"How can I ever forget you, Cheng?\""
    slm "\"Or was it WuZi?\""
    roy "\"...it's Roy\""
    slm "\"I'll remember that Troy\""
    roy "\"ROY\""
    slm "\"Shut it, Boy\""
    "Roll call took forever, as Schlam went around trying to remember everyone's names and the correct way of pronouncing them"
    "You have a niggling feeling that she would forget most people's names by your next lesson"
    slm "\"Basically, in preliminary (Year 11) English, us teachers are going to see if you kids are worthy of doing Extension 1 or 2 English\""
    slm "\"although, most of your cohort will probably only go into Advanced English, by the end of the year, like the unworthy scrubs that you are\""
    slm "\"Anyway, your modules for yr 11 are...\""
    slm "\"Fk...I forgot\""
    slm "\"excuse my french\""
    slm "\"aaah there's my cheat sheet\""
    slm "\"hehehehehe\""    
    slm "\"Alright, first you will be doing the Area of Study, or AoS of \"Belonging\". Basically, what it means to belong.\""
    roy "\"So, miss, like belong in a place, society, in the universe at large? Does it also explore escapism{nw}\""
    slm "\"STFU, SOY\""
    roy "\"...\""
    "You listen as one of the drama students, essentially paraphrase what Roy said"
    slm "\"Excellent point, MacIntosh. Yes, the texts we will explore will...err...explore these topics in depth\""
    roy "\"...\""
    slm "\"You will each be provided an anthology of poems, as prescribed texts...but not yet, cos the library is run by incompetent gophers\""
    slm "\"Actually, no, it's cos the grade above is too busy sniffing glue to return any of their texts for you to use yet\""
    slm "\"This applies for your Shakespeare text of the year, Othello\""
    slm "\"and your text for the study of the American Dream \"Of Mice and Men\", although it is paired with \"American Beauty\"...\""
    slm "\"Actually, all our discs of \"American Beauty\" are missing, something about students over-analysing roses in bedrooms\""
    slm "\"Hmmm....\""
    slm "\"How about you all partner up, and speak your classmates about your experiences in \"Belonging\".\""
    "Around the class, students instantly start moving around, forming pairs with their friends"
    sze "Damn, I need to find a partner soon or I will be left out"
    "You head towards Steven, catching his glance upon the way"
    dng "\"Soz man, already partnered up with Andrew\""
    sze "Fuck, the only remaining classmate I know is Roy"
    "You gaze across jostling students, but it appears that Roy has already partnered with a member of the infamous \"Games Club\""
    "It appears that everyone has already formed into groups."
    "But wait, there appears to be one student sitting alone in the back row engrossed in his mobile, unaware of what is going on around him"
    sze "\"Hey man, Wanna {s}play soccer{/s} partner up?\""
    zhn "\"对不起, 我不会说英文\""
    sze "\"uhh...\""
    menu:
        "\"[The teacher asked us to partner up for some groupwork]\"": 
#someone translate this to chinese pls, actually translate everything in square brackets
            zhn "\"[I see, I only just arrived in Australia, so I cant really help much]\""
            sze "Fricking useless international students, this wasnt meant to be an issue until uni"
            sze "\"[We should pretend to do work so we don't get in trouble]\""
            zhn "\"[That sounds like a good idea, I wasn't planning on doing work anyway]\""
            zhn "\"[By the way, you should play Hearthstone, it's a pretty good mobile game]\""
            #sze proceeds to play hearthstone, and adds some other students as friends on the game. Raises friendships with zhong and other students, maybe loss of intellect tho.
        "\"Ahh nevermind, Ill just pretend to do work\"":
            zhn "\"[I'll just be playing some Hearthstone]\""
            "You sit down in the adjacent seat and upon up your school laptop"
            sze "Maybe Dean has a halo server set up"
            #sze proceeds to play halo with Rick and Dean and potentially Anthony Le (bringing up storyline of Calculetor)
        "\"Fuck off boat person, We're Full\"":
            "It seems your words have triggered the majority left-leaning students in your class"
            "\"Asylums seekers have a right to seek shelter\""
            "\"It's Un-Australian to discriminate\""
            "\"I bet your a {s}TRUMP{/s} Abbott supporter, shame on you\""
            $ sze.fort -= 1
            #sze is isolated for the rest of the lesson
    slm "\"And would you look at that, lesson's over\""
    slm "\"Hopefully next lesson, we will be able to take the glue bottles and texts from the hands of the students in the grade above\""
    jump chemday1
