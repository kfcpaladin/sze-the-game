init -1 python:
    from models.achievements import Achievement, AchievementManager
    from util.conditions import * 

    def load_achievements(popups):
        

        manager = AchievementManager(popups)

        manager.add_achievement(Achievement(
            _id="thirst1",
            title="Become thirsty",
            brief="Get more than 25 thirst",
            description="One step closer to adulthood"
        ))

        manager.get_achievement("thirst1").set_unlock_condition(GreaterEqual(sze.thirst_prop, 25))

        manager.add_achievement(Achievement(
            _id="thirst2",
            title="Become thirstier",
            brief="Get more than 50 thirst",
            description="The joys of adulthood become more apparent",
            hidden=True
        ))

        manager.get_achievement("thirst2").set_reveal_condition(EqualTo(manager.get_achievement("thirst1").is_complete_prop, True))
        manager.get_achievement("thirst2").set_unlock_condition(GreaterEqual(sze.thirst_prop, 50))

        manager.add_achievement(Achievement(
            _id="poweredUp",
            title="Become a better person",
            brief="All your stats are positive",
            description="Since the days when you were thirsting over Serena, you have evolved into a better person",
            hidden=True
        ))

        manager.get_achievement("poweredUp").set_unlock_condition(And(
            GreaterThan(sze.thirst_prop, 0),
            GreaterThan(sze.intellect_prop, 0),
            GreaterThan(sze.charm_prop, 0),
            GreaterThan(sze.fort_prop, 0),
            GreaterThan(sze.strength_prop, 0),
        ))

        manager.add_achievement(Achievement(
            _id="autistic",
            title="You are a horrible person",
            brief="All your stats are negative",
            description="Your obsession with Serena has led you down a dark and terrible path, one that you may never recover from",
            hidden=True
        ))
        
        manager.get_achievement("autistic").set_unlock_condition(And(
            LessThan(sze.thirst_prop, 0),
            LessThan(sze.intellect_prop, 0),
            LessThan(sze.charm_prop, 0),
            LessThan(sze.fort_prop, 0),
            LessThan(sze.strength_prop, 0),
        ))

        # quest achievements
        manager.add_achievement(Achievement(
            _id="garyreeducation",
            title="Complete reeducation",
            brief="Gary has taught you well",
            description="As a fully fledged graduate of the Gary reeducation clinic, your thirst for Serena has become boundless",
            icon=loadImage("achievement_garyreeducation.png"),
            hidden=True
        ))

        manager.add_achievement(Achievement(
            _id="toddkarate",
            title="Start learning karate",
            brief="You meet Todd for the first time",
            description="Todd possesses alien karate skills, which he is willing to share with you",
            icon=loadImage("achievement_toddkarate.png"),
            hidden=True
        ))

        # friendship achievements
        manager.add_achievement(Achievement(
            _id="rina1",
            title="Slay Serena",
            brief="Date Serena",
            description="Your goal as a barnacle is complete",
            icon=loadImage("achievement_rina1.png")
        ))

        manager.get_achievement("rina1").set_unlock_condition(GreaterEqual(rin.friendship_prop, 100))

        # suicide achievements
        manager.add_achievement(Achievement(
            _id="suicide",
            title="Become suicidal",
            brief="Kill yourself at least 5 times",
            description="You are as suicidal as ISIS",
            hidden=True
        ))

        manager.get_achievement("suicide").set_unlock_condition(GreaterEqual(game.get_prop("suicideCount"), 5))

        # diary achievements
        manager.add_achievement(Achievement(
            _id="unlockSuicide",
            title="Learn about suicide",
            brief="Unlock the suicide button",
            description="The school seems to think that suicide is a nice choice...",
            icon=loadImage("achievement_unlockSuicide.png"),
            hidden=True
        ))

        manager.add_achievement(Achievement(
            _id="unlockDiary",
            title="Unlock the diary",
            brief="Moxham has blessed you",
            description="This diary is closer to a TARDIS than a book. The inventory doesn't seem to end...",
            icon=loadImage("achievement_unlockDiary.png"),
            hidden=True
        ))

        return manager