label garyreeducation:
    jit "\"Welcome to my reeducation program my young Arthur!\""
    $ quests.unlock_quest("garythirst1")
    "You have unlocked Gary's reeducation program"
    "Check your achievements to start Gary's reeducation quests"
    jump garyreeducation_finish

label garyreeducation1:
    jit "\"Touching the peepee makes white stuff come out\""
    $ sze.thirst += 1
    $ quests.complete_quest("garythirst1")
    "You take a moment to comprehend this new found knowledge"
    "..."
    jump garyreeducation_finish

label garyreeducation2:
    jit "\"Through the power of the internet one can access websites showcasing images of naked women\""
    $ sze.thirst += 2
    $ quests.complete_quest("garythirst2")
    "Your phone vibrates, and you salivate at all the possibilities that have opened up"
    jump garyreeducation_finish 

label garyreeducation3:
    jit "\"The penis can be inserted into the vagina achieve a pleasurable sensation\""
    $ sze.thirst += 3
    $ quests.complete_quest("garythirst3")
    "You think about what you can do to Serena"
    jump garyreeducation_finish

label garyreeducation4:
    jit "\"In certain areas known as Brothels, one may exchange currency for sex\""
    $ sze.thirst += 4
    $ quests.complete_quest("garythirst4")
    "You decide to save up some money to fuck a whore"
    jump garyreeducation_finish

label garyreeducation5:
    jit "\"When one grows tired of watching porn, they graduate to viewing 2-dimensional substitutes. This art form is known as Hentai.\""
    $ sze.thirst += 5
    $ quests.complete_quest("garythirst5") 
    "You never look at Gary's laptop the same way again"
    jump garyreeducation_finish

label garyreeducation6:
    jit "\"Contrary to popular belief Traps are not gay\""
    $ sze.thirst += 6
    $ quests.complete_quest("garythirst6")
    "You think about Serena, but with a penis"
    "Your imagination blossoms and your penis starts to erect itself"
    jit "Dude wtf do that elsewhere"
    sze "{i}blushes{/i}"
    jump garyreeducation_finish

label garyreeducation7:
    jit "\"It is said that upon remaining a virgin for 30 years, one will gain wizardly powers.\""
    $ sze.thirst += 7
    $ quests.complete_quest("garythirst7")
    sze "{i}Maybe Serena isnt that important anymore{/i}"
    jump garyreeducation_finish

label garyreeducation8:
    jit "\"Autofellatio is a sacred technique, known to only the most skilled perverts.\""
    $ sze.thirst += 8
    $ quests.complete_quest("garythirst8")
    "You begin to twist the pencil into your butthole violently"
    "The exotic blend between pain and pleasure makes you lose control of your body"
    sze "{i}urrgpgkgpghhh...{/i}"
    jit "What the fuck Arthur"
    $ achievements.unlock_achievement("garyreeducation")
    jump garyreeducation_finish

label garyreeducation_finish:
    "Recess has passed and you have English next"
    jump english1