init -1 python:
    achievements = Achievements(["title", "brief", "description", "dependencies"])
    # add achievements

init python:
    # thirst 
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
        "rina1": {
            "title": "Slay Serena",
            "brief": "Date Serena",
            "description": "Your goal as a barnacle is complete",
            "dependencies": None,
            "conditions": {
                "function": lambda: rin.friendship >= 100,
                "msg": "You have slain the beast",
            },
        },
    })
