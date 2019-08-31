default achievements = load_achievements()

init -1 python:
    from refactor.models.achievements import Achievement, AchievementManager

    def load_achievements():
        manager = AchievementManager()

        manager.add_achievement(Achievement(
            _id="thirst1",
            title="Become thirstier",
            brief="Get more than 50 thirst",
            description="The joys of adulthood become more apparent"
        ))

        manager.add_achievement(Achievement(
            _id="thirst2",
            title="Become thirstier",
            brief="Get more than 50 thirst",
            description="The joys of adulthood become more apparent"
        ))

        manager.add_achievement(Achievement(
            _id="poweredUp",
            title="Become a better person",
            brief="All your stats are positive",
            description="Since the days when you were thirsting over Serena, you have evolved into a better person",
            hidden=True
        ))

        manager.add_achievement(Achievement(
            _id="autistic",
            title="You are a horrible person",
            brief="All your stats are negative",
            description="Your obsession with Serena has led you down a dark and terrible path, one that you may never recover from",
            hidden=True
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

        # suicide achievements
        manager.add_achievement(Achievement(
            _id="suicide",
            title="Become suicidal",
            brief="Kill yourself at least 5 times",
            description="You are as suicidal as ISIS",
            hidden=True
        ))

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