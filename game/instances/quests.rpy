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
        "test1": {
            "title": "I am not a person 1",
            "brief": "I enjoy touching kids",
            "description": "Every since I was a young lad, I had always dreamt about touching the undersides of children. But then I got Harvey Weinstein'd",
            "dependencies": None,
        },
        "test2": {
            "title": "I am not a person 2",
            "brief": "I enjoy touching kids",
            "description": "Every since I was a young lad, I had always dreamt about touching the undersides of children. But then I got Harvey Weinstein'd",
            "dependencies": None,
        },
        "test3": {
            "title": "I am not a person 3",
            "brief": "I enjoy touching kids",
            "description": "Every since I was a young lad, I had always dreamt about touching the undersides of children. But then I got Harvey Weinstein'd",
            "dependencies": ["test1", "test2"],
        },
        "emptyQuest": {
            "title": None,
            "brief": None,
            "description": None,
            "dependencies": ["radniw", "dwaidnawn"],
        },
    })
