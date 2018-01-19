init -1 python:
    achievements = Achievements(["title", "brief", "description", "dependencies"])
    # add achievements

init python:
    # attribute achievements 
    achievements.addAchievements({
        "thirst1": {
            "title": "Become thirsty",
            "brief": "Get more than 25 thirst",
            "description": "One step closer to adulthood",
            "dependencies": None,
            "conditions": {
                "function": lambda: sze.thirst > 25,
                "msg": None,
            },
        },
        "thirst2": {
            "title": "Become thirstier",
            "brief": "Get more than 50 thirst",
            "description": "The joys of adulthood become more apparent",
            "dependencies": "thirst1",
            "conditions": {
                "function": lambda: sze.thirst > 50,
                "msg": None,
            },
        },
    })

    achievements.addAchievements({
        "poweredUp": {
            "title": "Become a better person",
            "brief": "All your stats are positive",
            "description": "Since the days when you were thirsting over Serena, you have evolved into a better person",
            "hidden": True,
            "conditions": [
                {
                    "function": lambda: sze.thirst > 0,
                    "msg": None,
                },
                {
                    "function": lambda: sze.intellect > 0,
                    "msg": None,
                },
                {
                    "function": lambda: sze.charm > 0,
                    "msg": None,
                },
                {
                    "function": lambda: sze.fort > 0,
                    "msg": None,
                },
                {
                    "function": lambda: sze.strength > 0,
                    "msg": None,
                },
            ],
        },
        "autistic": {
            "title": "You are a horrible person",
            "brief": "All your stats are negative",
            "description": "Your obsession with Serena has led you down a dark and terrible path, one that you may never recover from",
            "hidden": True,
            "conditions": [
                {
                    "function": lambda: sze.thirst < 0,
                    "msg": None,
                },
                {
                    "function": lambda: sze.intellect < 0,
                    "msg": None,
                },
                {
                    "function": lambda: sze.charm < 0,
                    "msg": None,
                },
                {
                    "function": lambda: sze.fort < 0,
                    "msg": None,
                },
                {
                    "function": lambda: sze.strength < 0,
                    "msg": None,
                },
            ],
        },
    })

    # quest achievements
    achievements.addAchievements({
        "garyreeducation": {
            "title": "Complete reeducation",
            "brief": "Gary has taught you well",
            "description": "As a fully fledged graduate of the Gary reeducation clinic, your thirst for Serena has become boundless",
            "icon": loadImage("achievement_garyreeducation.png"),
            "hidden": True,
        }
    })

    # friendship achievements
    achievements.addAchievements({
        "rina1": {
            "title": "Slay Serena",
            "brief": "Date Serena",
            "description": "Your goal as a barnacle is complete",
            "icon": loadImage("achievement_rina1.png"),
            "dependencies": None,
            "conditions": {
                "function": lambda: rin.friendship >= 100,
                "msg": "You have slain the beast",
            },
        },
    })

    # suicide achievements
    achievements.addAchievements({
        "suicide": {
            "title": "Become suicidal",
            "brief": "Kill yourself at least 5 times",
            "description": "You are as suicidal as ISIS",
            "hidden": True,
            "conditions":{
                "function": lambda: game.suicideCount >= 5,
                "msg": "Stop killing yourself",
            },
        },
    })
