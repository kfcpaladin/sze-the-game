define game = Game({
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
    "kahootStarted": False, # Keep track of intialisation for kahoot game
    "kahootScore": {        # Keep track of the score
        "points": 0, 
        "time_remain": 0, 
        "choice": None
    },    
    "metDerek": False,
    "norton": False,
    "stealWillisGirl": False,
    "yangRant": False,
    # Iterables
    "moxCounter": 0,
    "timeTravelCounter": 0,
})