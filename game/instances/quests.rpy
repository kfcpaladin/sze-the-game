init python:
    quests = Quests(["title", "brief", "description", "dependencies"])
    quests.addQuests({
        "serenaSlay": {
            "title": "Slay Serena and acquire your pass into heaven",
            "brief": "Arthur is planning on slaying Serena",
            "description": "Once in heaven, Arthur will be able to slay several virgins, thereby satisfying his life goal of being a donkey",
            "dependencies": None,
        },
        "sexuality": {
            "title": "Arthur's gay journey",
            "brief": "Arthur is planning on going on an adventure",
            "description": "In order to acquire all 9 pokeballs, he must conquer Kevin Spacey",
            "dependencies": None,
        },
        "garythirst1": {
            "title": "Gary's reeducation program",
            "brief": "Gary will help Arthur slay Serena",
            "description": "Not only are his expertise in slaying unparalleled, he also offers free condoms",
            "dependencies": "locked",
            "label": "garyreeducation1",
        },
        "garythirst2": {
            "title": "Gary's reeducation program",
            "brief": "Gary will help Arthur slay Serena",
            "description": "Not only are his expertise in slaying unparalleled, he also offers free condoms",
            "dependencies": "garythirst1",
            "label": "garyreeducation2",
        },
    })
