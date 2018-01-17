init python:
    quests = Quests(["title", "brief", "description", "dependencies", "label"])
    # Test quests
    quests.addQuests({
        "serenaSlay": {
            "title": "Slay Serena and go to heaven",
            "brief": "Arthur is planning on slaying Serena",
            "description": "Once in heaven, Arthur will be able to slay several virgins, thereby satisfying his life goal of being a donkey",
            "icon": loadImage("quest_serenaSlay.png"),
            "dependencies": None,
            "conditions": [
                {
                    "function": lambda: sze.strength > 100,
                    "msg": "You need at least 100 strength to impress [rin.name]",
                },
                {
                    "function": lambda: sze.thirst > 100,
                    "msg": "You have insufficient thirst to slay [rin.name]",
                },
                {
                    "function": lambda: game.timeTravelCounter >= 4,
                    "msg": "To slay [rin.name] you must time travel at least 4 times"
                },
                {
                    "function": lambda: rin.friendship >= 50,
                    "msg": "Without being friends with [rin.name] you cannot slay her",
                },
                {
                    "function": lambda: game.moxCounter <= 0,
                    "msg": "[rin.name] does not appreciate rebels as a companion",
                },
            ]
        },
        "sexuality": {
            "title": "Arthur's gay journey",
            "brief": "Arthur is going on an adventure",
            "description": "In order to acquire all 9 pokeballs, he must conquer Kevin Spacey",
            "dependencies": None,
            "conditions": {
                "function": lambda: sze.thirst > 100,
                "msg": "You need at least 100 thirst",
            },
        },
    })

    # Gary reeducation quests
    quests.addQuests({
        "garythirst1": {
            "title": "Gary's reeducation program",
            "brief": "Gary will help Arthur slay Serena",
            "description": "Not only are his expertise in slaying unparalleled, he also offers free condoms",
            "dependencies": "locked",
            "label": "garyreeducation1",
            "conditions": {
                "function": lambda: game.checkTime("recess"),
                "msg": "You can only go to Gary for reeducation during recess", 
            },
        },
        "garythirst2": {
            "title": "Gary's reeducation program",
            "brief": "Gary will help Arthur slay Serena",
            "description": "Not only are his expertise in slaying unparalleled, he also offers free condoms",
            "dependencies": "garythirst1",
            "label": "garyreeducation2",
            "conditions": {
                "function": lambda: game.checkTime("recess"),
                "msg": "You can only go to Gary for reeducation during recess", 
            },
        },
        "garythirst3": {
            "title": "Gary's reeducation program",
            "brief": "Gary will help Arthur slay Serena",
            "description": "Not only are his expertise in slaying unparalleled, he also offers free condoms",
            "dependencies": "garythirst2",
            "label": "garyreeducation3",
            "conditions": {
                "function": lambda: game.checkTime("recess"),
                "msg": "You can only go to Gary for reeducation during recess", 
            },
        },
        "garythirst4": {
            "title": "Gary's reeducation program",
            "brief": "Gary will help Arthur slay Serena",
            "description": "Not only are his expertise in slaying unparalleled, he also offers free condoms",
            "dependencies": "garythirst3",
            "label": "garyreeducation4",
            "conditions": {
                "function": lambda: game.checkTime("recess"),
                "msg": "You can only go to Gary for reeducation during recess", 
            },
        },
        "garythirst5": {
            "title": "Gary's reeducation program",
            "brief": "Gary will help Arthur slay Serena",
            "description": "Not only are his expertise in slaying unparalleled, he also offers free condoms",
            "dependencies": "garythirst4",
            "label": "garyreeducation5",
            "conditions": {
                "function": lambda: game.checkTime("recess"),
                "msg": "You can only go to Gary for reeducation during recess", 
            },
        },
        "garythirst6": {
            "title": "Gary's reeducation program",
            "brief": "Gary will help Arthur slay Serena",
            "description": "Not only are his expertise in slaying unparalleled, he also offers free condoms",
            "dependencies": "garythirst5",
            "label": "garyreeducation6",
            "conditions": {
                "function": lambda: game.checkTime("recess"),
                "msg": "You can only go to Gary for reeducation during recess", 
            },
        },
        "garythirst7": {
            "title": "Gary's reeducation program",
            "brief": "Gary will help Arthur slay Serena",
            "description": "Not only are his expertise in slaying unparalleled, he also offers free condoms",
            "dependencies": "garythirst6",
            "label": "garyreeducation7",
            "conditions": {
                "function": lambda: game.checkTime("recess"),
                "msg": "You can only go to Gary for reeducation during recess", 
            },
        },
        "garythirst8": {
            "title": "The final problem",
            "brief": "Become a slaying god",
            "description": "If you complete this, you will become the most sexy man alive",
            "dependencies": "garythirst7",
            "label": "garyreeducation8",
            "conditions": {
                "function": lambda: game.checkTime("recess"),
                "msg": "You can only go to Gary for reeducation during recess", 
            },
        }
    })
