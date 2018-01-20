init -10 python:
    game = Game({
        "allowedAreas": [
            "bcourts", "bridge", "carpark", "cohen", "currycourts", 
            "food", "fortstreet", "gym", "hall", "kilgour", 
            "library", "lkilgour", "lquad", "oval", "place", 
            "quad", "rowe", "rquad", "uquad", "valley", "wilkins", 
        ],
        # Booleans
        "chaoPissed": False,
        "delivery": False,
        "electionPromise": False,
        "metDerek": False,
        "norton": False,
        "stealWillisGirl": False,
        "yangRant": False,
        # Iterables
        "moxCounter": 0,
        "timeTravelCounter": 0,
        "currentDay": 1,
        "suicideCount": 0,
        "currentDiaryPage": 0,
    })

    game.addTimes({
        "morning": True,
        "recess": False,
        "lunch": False,
        "afternoon": False,
        "night": False,
    })

