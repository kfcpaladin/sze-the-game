label garyreeducation:
    jit "\"Welcome to my reeducation program my young Arthur!\""
    $ quests.unlockQuest("garythirst1")
    "You have unlocked Gary's reeducation program"
    "Check your achievements to start Gary's reeducation quests"
    jump garyreeducation_finish

label garyreeducation1:
    jit "\"Touching the peepee makes white stuff come out\""
    $ sze.gain("thirst")
    $ quests.completeQuest("garythirst1")
    "You take a moment to comprehend this new found knowledge"
    "..."
    jump garyreeducation_finish

label garyreeducation2:
    jit "\"Through the power of the internet one can access websites showcasing images of naked women\""
    $ sze.gain("thirst", 2)
    $ quests.completeQuest("garythirst2")
    "Your phone vibrates, and you salivate at all the possibilities that have opened up"
    jump garyreeducation_finish 

label garyreeducation3:
    jit "\"The penis can be inserted into the vagina achieve a pleasurable sensation\""
    $ sze.gain("thirst", 3)
    $ quests.completeQuest("garythirst3")
    "You think about what you can do to Serena"
    jump garyreeducation_finish

label garyreeducation4:
    jit "\"In certain areas known as Brothels, one may exchange currency for sex\""
    $ sze.gain("thirst", 4)
    $ quests.completeQuest("garythirst4")
    "You decide to save up some money to fuck a whore"
    jump garyreeducation_finish

label garyreeducation5:
    jit "\"When one grows tired of watching porn, they graduate to viewing 2-dimensional substitutes. This art form is known as Hentai.\""
    $ sze.gain("thirst", 5)
    $ quests.completeQuest("garythirst5") 
    "You never look at Gary's laptop the same way again"
    jump garyreeducation_finish

label garyreeducation6:
    jit "\"Contrary to popular belief Traps are not gay\""
    $ sze.gain("thirst", 6)
    $ quests.completeQuest("garythirst6")
    "You think about Serena, but with a penis"
    "Your imagination blossoms and your penis starts to erect itself"
    jit "Dude wtf do that elsewhere"
    sze "{i}blushes{/i}"
    jump garyreeducation_finish

label garyreeducation7:
    jit "\"It is said that upon remaining a virgin for 30 years, one will gain wizardly powers.\""
    $ sze.gain("thirst", 7)
    $ quests.completeQuest("garythirst7")
    sze "{i}Maybe Serena isnt that important anymore{/i}"
    jump garyreeducation_finish

label garyreeducation8:
    jit "\"Autofellatio is a sacred technique, known to only the most skilled perverts.\""
    $ sze.gain("thirst", 8)
    $ quests.completeQuest("garythirst8")
    "You begin to twist the pencil into your butthole violently"
    "The exotic blend between pain and pleasure makes you lose control of your body"
    sze "{i}urrgpgkgpghhh...{/i}"
    jit "What the fuck Arthur"
    jump garyreeducation_finish

label garyreeducation_finish:
    "Recess has passed and you have English next"
    jump english1