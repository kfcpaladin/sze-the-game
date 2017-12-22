init -1 python:
    itemList = {
        "ball": Item(**{
            "name": "ball", 
            "desc": "bouncy thing", 
            "stat": {
                "strength": 1,
                "intellect": -1,
                "charm": -1,
            }, 
            "icon": "images/ball.png",
        }),
        "axe": Item(**{
            "name": "axe", 
            "desc": "weaponz", 
            "stat": {
                "strength": 10,
                "intellect": -10,
                "charm": 2,
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
                "strength": 15,
                "intellect": -20,
                "charm": 5,
            }, 
            "icon": "images/axe.png",
        }),
        "calc": Item(**{
            "name": "calculator", 
            "desc": "smarts + 1", 
            "stat": {
                "intellect": 20,
                "strength": -10,
                "charm": -10,
            }, 
            "icon": "images/calc1.png",
        }),
    }