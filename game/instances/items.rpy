init -1 python:
    itemList = {
        "ball": Item(**{
            "name": "ball", 
            "desc": "bouncy thing", 
            "stat": {
                "charm": -1,
                "intellect": -1,
                "strength": 1,
            }, 
            "icon": "images/ball.png",
        }),
        "axe": Item(**{
            "name": "axe", 
            "desc": "weaponz", 
            "stat": {
                "charm": 2,
                "intellect": -10,
                "strength": 10,
            }, 
            "icon": "images/axe.png",
        }),
        "money": Item(**{
            "name": "monies", 
            "desc": "cash monies wads", 
            "stat": {
                "charm": 10,
                "intellect": 4,
                "strength": -3,
            }, 
            "icon": "images/bag.png",
        }),
        "fireaxe": Item(**{
            "name": "fireaxe", 
            "desc": "weaponz", 
            "stat": {
                "charm": 5,
                "intellect": -20,
                "strength": 15,
            }, 
            "icon": "images/axe.png",
        }),
        "calc": Item(**{
            "name": "calculator", 
            "desc": "smarts + 1", 
            "stat": {
                "charm": -10,
                "intellect": 20,
                "strength": -10,
            }, 
            "icon": "images/calc1.png",
        }),
    }

    unlockableItems = {
        "god": Item(**{
            "name": "The god particle",
            "desc": "Turns you into michael kirby",
            "stat": {
                "charm": 1000,
                "fort": 1000,
                "intellect": 1000,
                "strength": 1000,
                "thirst": -1000,
            },
            "icon": "images/kirby.png",
        }),
        "neo armstrong": Item(**{
            "name": "neo armstrong cyclone jet armstrong cannon",
            "desc": "The most powerful weapon used by an alien civilization, able to destroy wipe out entire species (sunrise don;t sue us)",
            "stat": {
                "charm": 1000,
                "fort": -100,
                "intellect": -1000,
                "strength": 1000,
                "thirst": 1000,
            },
            "icon": "images/cannon.png",
        })
    }
