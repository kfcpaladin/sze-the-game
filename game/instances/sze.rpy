# Customising sze through the MainCharacter class
init python:
    # Reads dictionary of attribute values
    sze.setAttributes({
        "charm": 0,
        "fort": 0,
        "intellect": 0,
        "strength": 0,
        "thirst": 0,
    })
    # Set the messages you get when the tutorial is enable - Activated when your attribute changes for the first time
    sze.setTutorials({
        "charm": {
            "show": True, 
            "brief": "Charm is a measure of how well you slay",
            "msgGain": "Currently you are a faggot, however this may be changed through slaying not being retarded in day to day life.",
            "msgLoss": "Currently you are a faggot, however this may be changed through slaying not being retarded in day to day life.",
        },
        "fort": {
            "show": True, 
            "brief": "Fortianness is how Fortian you are and can be improved by being more Michael Kirby",
            "msgGain": "Currently, you aren't very Fortian.",
            "msgLoss": "Currently, you aren't very Fortian.",  
        },
        "intellect": {
            "show": True, 
            "brief": "Intelligence is a measure of how smart you are",
            "msgGain": "Currently you are a retard, however this may be changed through diligent studying and participating in class.",
            "msgLoss": "Currently you are a retard, however this may be changed through diligent studying and participating in class.",
        },
        "strength": {
            "show": True, 
            "brief": "Strength is a measure of how strong you are",
            "msgGain": "It can be improved by getting good. Currently you aren't very good.",
            "msgLoss": "It can be improved by getting good. Currently, you make 6 year olds look like professional MMA fighters.", 
        },
        "thirst": {
            "show": True, 
            "brief": "Thirst is a measure of desperately you want to drink water",
            "msgGain": "You become one step closer to Tiddalik.",
            "msgLoss": "At this rate your body will dehydrate into a shrivelled penis.",
        },
    })
    # Whenever your attribute changes, a message will be provided depending on whether it increased or decreased
    sze.setAttributeIntroMessages({
        "charm": {
            "msgGain": "Your charm increased",
            "msgLoss": "Your charm just decreased",
        },
        "fort": {
            "msgGain": "You became more Michael Kirby  , as your Fortianness is at [sze.fort]",
            "msgLoss": "You fortianness dropped.",
        },
        "intellect": {
            "msgGain": "Congratulations",
            "msgLoss": "You become a bit dumber",
        },
        "strength": {
            "msgGain": "Your combat propensity has increased",
            "msgLoss": "Your combat propensity has decreased",
        }, 
        "thirst": {
            "msgGain": "You became more thirsty",
            "msgLoss": "You start zipping your pants back up",
        },
    })
    # This will determine what message you will get depending on the attribute value
    sze.setAttributeMessages({
        "charm": [
            {"min": 100, "msg": "With a charm of [sze.charm], you slay just by looking. Gaze upon the world, your dominion."},
            {"min": 75,  "msg": "With a charm of [sze.charm], you have probably slayed every LG in Sydney by now"},
            {"min": 50,  "msg": "You have surpassed even Chao in slaying ability with a charm of [sze.charm]"},
            {"min": 25,  "msg": "You are just very slightly charming, at [sze.charm]"},
            {"min": 0,   "msg": "With exceptionally average charm of [sze.charm], its going to take a very long time for Serena to notice you."},
            {"min":-25,  "msg": "With charm of [sze.charm], there seems to be an invisible forcefield repelling LGs from you"},
            {"min":-50,  "msg": "With charm at [sze.charm], you are often mistaken as a modern art piece."},
            {"min":-75,  "msg": "The average gayness of every room you enter is increased by 100%, due to your charm of [sze.charm]"},
            {"min":-100, "msg": "You once tried to masturbate, your hand rejected you."},
            {"min":-125, "msg": "Even bacteria tries to avoid you."},
        ],
        "fort": [
            {"min": 100, "msg": "You are the epitome of the fort, with a fortianness of [sze.fort]\nYou are a proper protester, you call the police \"pig dogs\" and you are part of an artist collective"},
            {"min": 75,  "msg": "Michael Kirby looks up to you and your fortianness of [sze.fort]"},
            {"min": 50,  "msg": "With a fortianness of [sze.fort], you are often called in to speak at Speech Day"},
            {"min": 25,  "msg": "With a fortianness of [sze.fort], you probably made it into the SRC"},
            {"min": 0,   "msg": "At [sze.fort] fortianness, you are merely a generic student"},
            {"min":-25 , "msg": "Your poor fortianness of [sze.fort] suggests you might secretly be a James Ruse spy"},
            {"min":-50,  "msg": "At [sze.fort] fortianness, Moxham is willing to engage in the capitalist process of putting a bounty on your head to kill you"},
            {"min":-75,  "msg": "With [sze.fort] fortianness, you are probably a dirty, capitalist, bourgeois pig who might have underlying religious affiliations"},
            {"min":-100, "msg": "Your racist, sexist and classist behaviour is an affront to the school"},
        ],
        "intellect": [
            {"min": 100, "msg": "With intelligence of [sze.intellect], maybe its for the better. Your thoughts were too complex for even Stephen Hawking."},
            {"min": 75,  "msg": "But your predicted ATAR is still a safe 99.95, and your intelligence of [sze.intellect]"},
            {"min": 50,  "msg": "You are quite smart already, maybe not band-6 yet, but getting there. A bit more hard work and you will truly ACE TRIALS. Your current intelligence is [sze.intellect]"},
            {"min": 25,  "msg": "Your intelligence is at [sze.intellect], not particularly amazing."},
            {"min": 0,   "msg": "With your remarkably average intelligence of [sze.intellect], Serena will probably not be impressed."},
            {"min":-25 , "msg": "You are a bit slow, with intelligence of [sze.intellect]"},
            {"min":-50,  "msg": "You are probably doing worse than Chao in your tests currently, with intelligence of [sze.intellect]"},
            {"min":-75,  "msg": "It's astonishing how someone with an intelligence of [sze.intellect] even made it to Fort Street. How many dicks did you have to suck to get here?"},
            {"min":-100, "msg": "With intelligence of [sze.intellect], you are not even a functioning member of society."},
            {"min":-125, "msg": "You are somehow dumber than a rock, like literally. I dont know how that is even possible."},
        ],
        "strength": [
            {"min": 100, "msg": "Your combat propensity is at [sze.strength], making you Level S-Class 11th-dan Golden Jade Dragon Jedi Master Ninja Samurai Knight Marshal Admiral, surpassing Saitama in skill."},
            {"min": 75,  "msg": "With combat propensity at [sze.strength], you probably ended 300 spartans with a single one-inch punch."},
            {"min": 50,  "msg": "Your combat propensity of [sze.strength] would allow you to beat black-belt Aradhya and Jew-jitsu Steven with ease."},
            {"min": 25,  "msg": "At combat propensity levels of [sze.strength], you can probs beat the average student."},
            {"min": 0,   "msg": "At [sze.strength], your combat propensity, it is advised that you tactically retreat from your \"fights\"."},
            {"min":-25 , "msg": "Your below average combat propensity of [sze.strength] suggests that you have a thing for being dominated."},
            {"min":-50,  "msg": "At [sze.strength] combat propensity, the only slaying you know is in Dungeons & Dragons..."},
            {"min":-75,  "msg": "With [sze.strength] combat propensity pussies slays you."},
            {"min":-100, "msg": "When you have [sze.strength] combat \"propensity\", you will get rekt so hard, you will be reincarnated as an abortion."},
            {"min":-125, "msg": "Your combat \"propensity\" or lack thereof will lead to much assrippings in the future"},
        ],
        "thirst": [
            {"min": 100, "msg": "At a thirst of [sze.thirst], you rival Tiddalik"},
            {"min": 75,  "msg": "With a thirst of [sze.thirst], sometimes moxham appears in your {s}dreams{/s} hallucinations"},
            {"min": 50,  "msg": "With a thirst of [sze.thirst], like Roy, you are willing to partake in sexual activities with robots for water"},
            {"min": 25,  "msg": "Even a can of SOLO cannot crush your thirst of [sze.thirst]"},
            {"min": 0,   "msg": "At [sze.thirst] thirstiness , you have the standard healthy desires of a teenage boy of your age."},
            {"min":-25 , "msg": "With a thirstiness of [sze.thirst], you have been oft compared to LiXu"},
            {"min":-50,  "msg": "At a thirst of [sze.thirst], it is no surprise you have already taken a vow of celibacy."},
            {"min":-75,  "msg": "With [sze.thirst] thirstiness, you elected to have a penectomy."},
            {"min":-100, "msg": "You are disgusted by the concept of sexual relations, even with Serena."},
        ],
    })
    # set stat messages
    sze.setStatMessages({
        "charm": [
            {"min": 100, "msg": "You slay just by looking. Gaze upon the world, your dominion"},
            {"min": 75,  "msg": "With that level of charm, you have probably slayed every LG in Sydney by now"},
            {"min": 50,  "msg": "You have surpassed even Chao in slaying ability; the teacher becomes the student"},
            {"min": 25,  "msg": "You are just very slightly charming"},
            {"min": 0,   "msg": "With such exceptionally average charm, its going to take a very long time for senpai to notice you."},
            {"min":-25,  "msg": "With your charm, or lack thereof, there seems to be an invisible forcefield repelling girls from you"},
            {"min":-50,  "msg": "With that much charm, you are often mistaken for a modern art piece"},
            {"min":-75,  "msg": "The average gayness of every room you enter is increased by 100%, due to your charm"},
            {"min":-100, "msg": "You once tried to masturbate, your hand rejected you"},
        ],
        "fort": [
            {"min": 100, "msg": "You are a proper protester, you call the police 'pig dogs' and you are part of an anarcho-Maoist-libertarian artist collective"},
            {"min": 75,  "msg": "Michael Kirby looks up to you and your fortianness"},
            {"min": 50,  "msg": "With that much Fortianness, you would be called in to give talks about social justice, but you don't have any white priviledge to acknowledge and you are still straight (you think), cis-gendered scum"},
            {"min": 25,  "msg": "With that much Fortianness, you probably can make it into the SRC if you were bothered"},
            {"min": 0,   "msg": "At [sze.fort] Fortianness, you are merely a generic student"},
            {"min":-25,  "msg": "Your poor fortianness of [sze.fort] suggests you might secretly be a James Ruse spy"},
            {"min":-50,  "msg": "At [sze.fort] fortianness, Moxham is willing to engage in the capitalist process of putting a bounty on your head to kill you"},
            {"min":-75,  "msg": "With so little fortianness, you're probs a dirty, capitalist, bourgeois pig who might have underlying religious affiliations"},
            {"min":-100, "msg": "With so little fortian- how are you not just expelled at this point?"},
        ],
        "intellect": [
            {"min": 100, "msg": "You have surpassed even Justin Wu, dux of James Ruse"},
            {"min": 75,  "msg": "Maybe you'll be able to impress Serena with your 99.95 ATAR"},
            {"min": 50,  "msg": "A bit more hard work and you will truly ACE TRIALS"},
            {"min": 25,  "msg": "At marginally above average intellect you really shouldnt be celebrating yet"},
            {"min": 0,   "msg": "With your remarkably average intellect, your waifu will probably not be impressed"},
            {"min":-25,  "msg": "You are a bit slow, should you even be in a selective school?"},
            {"min":-50,  "msg": "Your test results are probably worse than Chao's tests for STDs"},
            {"min":-75,  "msg": "It's astonishing how you made it to Fort Street. How many dicks did you have to suck to get here?"},
            {"min":-100, "msg": "With almost no brain activity, the fact that your nervous system still works is a scientific anomaly."},
        ],
        "strength": [
            {"min": 100, "msg": "You are Level S-Class 11th-dan Golden Jade Dragon Jedi Master Ninja Samurai Viking Knight Marshal Admiral"},
            {"min": 75,  "msg": "With your combat propensity, you probably ended 300 spartans with a single one-inch punch."},
            {"min": 50,  "msg": "Your skill in a fight would allow you to beat black-belt Aradhya and Jew-jitsu Steven."},
            {"min": 25,  "msg": "With such strength, you can probs beat the average student."},
            {"min": 0,   "msg": "At your level it is advised that you tactically retreat from your fights."},
            {"min":-25,  "msg": "Your below average combat propensity suggests that you have a thing for being dominated."},
            {"min":-50,  "msg": "At [sze.strength] combat propensity, the only slaying you know is in Dungeons & Dragons..."},
            {"min":-75,  "msg": "With that combat 'proficiency' pussies slays you."},
            {"min":-100, "msg": "Don't fight; you will get rekt so hard, you will be reincarnated as an abortion."},
        ],
        "thirst": [
            {"min": 100, "msg": "At a thirst of [sze.thirst], you rival Tiddalik"},
            {"min": 75,  "msg": "You're so thirsty, sometimes moxham appears in your {s}dreams{/s} hallucinations"},
            {"min": 50,  "msg": "With that much thirst, like Roy, you are willing to partake in sexual activities with robots for water"},
            {"min": 25,  "msg": "Even a can of SOLO cannot crush your thirst of [sze.thirst]"},
            {"min": 0,   "msg": "With this much thirstiness, you have the standard healthy desires of a teenage boy of your age."},
            {"min":-25,  "msg": "You have been oft compared to LiXu due to your lack of thirst"},
            {"min":-50,  "msg": "The only thing you drink is mountain dew when playing WoW"},
            {"min":-75,  "msg": "With your lack of desire for water, it is no surprise you have already taken a vow of celibacy."},
            {"min":-100, "msg": "You elected to have a penectomy, your bladder being sufficient for your needs."},
        ]
    })



