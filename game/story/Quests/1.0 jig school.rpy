label jigschool1:
    $ autosave()
    scene bg loadingdock
    # intro
    "You decide to jig school like a dropkick"
    sze "\"{b}Where the fuck I am???{/b}\""
    $ playmusic("TheRoomOSTMainTheme.ogg")
    "\"Who {i}{b}dares{/b}{/i} trespass on my land???\""
    sze "\"Oh shit please don't kill me\""
    "Your bladder feels like it is going to depressurise inside your pants"
    sze "\"{i}Do you know where a bathroom is???{/i}\""
    "\"Come forth {i}young{/i} one. Let me see you...\""
    "You feel a {color=[PrimaryColours.YELLOW]}{i}little drop of urine{/i}{/color} drip out from your bump"
    # choice
    menu:
        "Should you go into the dark alley way ahead of you?"
        "Yes":
            "Against all reasonable thinking, you decide to head into the dark alley way"
            "{b}You hear scraping along the floor, like that of steel against concrete{/b}"
        "No":
            "As you begin to turn around something grabs you by the neck"
            tod "{b}What a coward{/b}"
            sze "{i}Oh shit my pants{/i}"
            "{color=[PrimaryColours.YELLOW]}{i}You urinate inside your pants{/i}{/color}"
    # start fighting
    $ playsfx("vpunch.ogg")
    sze "What the..." with vpunch
    tod "\"What a lame specimen. How disappointing{b}...{/b}\""
    sze "\"Wait what the {b}hell are you doing!!!!{/b}\""
    $ playmusic("ManuelGasGasGas(InitialD).ogg")
    "Suddenly you see a blurry wall of moving muscle and raw power move towards you"
    $ _string = "{grow}!!!!!!!!!!{/grow}"
    sze "{i}{b}{color=[PrimaryColours.RED]}[_string]{/color}{/b}{/i}"
    tod "{b}Fight or die!!!{/b}"
    "{color=[PrimaryColours.RED]}{b}You are greeted with claws slashing away at your flesh, causing blood to gush out of your ragged wounds{/b}{/color}"
    sze "{b}Argggrgegegafwadnaw{/b}"
    $ playsfx("hpunch.ogg")
    sze "Please stop" with hpunch
    $ playsfx("vpunch.ogg")
    "...." with vpunch
    tod "{b}Your lack of courage is most disappointing{/b}"
    "This stranger reveals his alien body, and stands several meters above you"
    # fight back or not
    menu:
        "{b}Throw your strongest punch back{/b}":
            $ _string = "{grow}TAKE THIS YOU FOUL BEAST{/grow}"
            sze "{b}[_string]{/b}"
            $ playsfx("vpunch.ogg")
            "Your fist is propelled at near luminal speeds, colliding against the skull of your enemy" with vpunch
            $ playsfx("hpunch.ogg")
            "{color=[PrimaryColours.RED]}{b}Your fist turns into a soft suspension of blood and shattered bones{/b}{/color}" with hpunch
            tod "{b}What a feeble race these humans are{/b}"
            $ playsfx("vpunch.ogg")
            "In one swell swoop your internal organs part way from your body" with vpunch
            "{color=[PrimaryColours.RED]}{b}{i}Blood rushes out of your chest cavity, and you feel your heart expanding into your thoracic cavity{/i}{/b}{/color}"
            sze "urggg..."
            jump jigschool1_todd_teach
        "{i}Try to run away{/i}":
            jump jigschool1_todd_death
        "{color=[PrimaryColours.YELLOW]}{i}Throw your urine soaked pants at him{/i}{/color}":
            sze "Take this"
            $ playsfx("hpunch.ogg")
            "Your drenched pants slam into your opponent's face" with hpunch
            tod "{color=[PrimaryColours.RED]}{b}Big mistake{/b}{/color}"
            jump jigschool1_todd_death

    
label jigschool1_todd_death:
    sze "{i}whimpers{/i}"
    "As you start to run back you feel something run down your spine"
    sze "{color=[PrimaryColours.RED]}{b}glurrg....{/b}{/color}"
    "You spine has been {b}ripped{/b} out of your body"
    tod "I shall consume this {i}wimp{/i} for nutrition"
    "As the alien approaches you, a sense of overwhelming fear comes over you"
    sze "{i}oh my god{/i}"
    $ playsfx("vpunch.ogg")
    "This alien plunges his hand onto yor chest, and you feel your sternum parting way" with vpunch
    $ playsfx("vpunch.ogg")
    "You body is being drained of all life..." with vpunch
    "You feel yourself turning into a skeleton, as your organs become {color=[PrimaryColours.RED]}{b}liquified{/b}{/color}"
    hide bg loadingdock
    with fade
    show bg ded
    jump dead

label jigschool1_todd_teach:
    # choose to fight back
    $ playsfx("vpunch.ogg")
    "You begin to succumb to your {color=[PrimaryColours.RED]}{b}CATASTROPHIC{/b}{/color} blood loss" with vpunch
    tod "{i}What a pitiful fight{/i}"
    tod "{b}But since you tried to fight back, I can see that you are indeed full of determination and courage{/b}"
    "You sense an aura of respect from your opponent, as he stands above your limp body"
    tod "Young one, are you willing to train and rise above your {i}weakness{/i}?"
    # joke menu
    menu:
        "{b}urggg...{/b}":
            sze "{b}urggg...{/b}"
        "{color=[PrimaryColours.RED]}{b}Cough blood...{/b}{/color}":
            sze "{color=[PrimaryColours.RED]}{b}ackkt...{/b}{/color}"
            "{color=[PrimaryColours.RED]}{b}Blood is sprayed everywhere{/b}{/color}"
        "{color=[PrimaryColours.YELLOW]}{i}Piss yourself{/i}{/color}":
            sze "{i}Ahhh....{/i}"
            "The alien beast takes a step back to avoid stepping in your {color=[PrimaryColours.YELLOW]}{b}urine{/b}{/color}"
    tod "I'll take that as a {color=[PrimaryColours.GREEN]}{b}yes{/b}{/color}"
    "{b}Todd begins to place his palm on your chest{/b}"
    $ playsfx("vpunch.ogg")
    "Suddenly you feel a rush of adrenaline as he pumps his life force into you" with vpunch
    "Your body becomes {color=[PrimaryColours.GREEN]}{b}completely invigorated{/b}{/color} as you recover from your mortal wounds"
    sze "{b}Holy {color=[PrimaryColours.RED]}{i}fuckkk{/i}{/color}{/b}"
    tod "Welcome back my new padawan"
    tod "I [tod.name] will teach you my ways, and one day you may ascend to rival me"
    $ achievements.unlock_achievement("toddkarate")
    sze "{b}Holy shit that felt good{/b}"
    $ sze.strength += 10
    $ tod.friendship += 10
    sze "Teach me your ways master [tod.name]"
    scene bg loadingdocksign
    with fade
    "You spent several hours fighting it out"
    $ playsfx("hpunch.ogg")
    "{b}Blow{/b} after {b}blow{/b} after {b}blow{/b}, your body is eviscerated and rebuilt" with vpunch
    "{color=[PrimaryColours.RED]}{b}Your body is hardened against the might of Todd's blows, and you begin to overcome your inherent weakness{/b}{/color}"
    "You bow to master Todd before you depart, and return to your classes"
    $ quests.complete_quest("jigschool1")
    tod "Farewell my new student"
    "You walk back to school a new man, now gifted life where there was once none"
    jump recess1a

    