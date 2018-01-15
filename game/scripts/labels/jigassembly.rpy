init python:

    # 5.1 jig assembly
    labels.extend([
        {
            "name": "asszembly1jigolo",
            "jump": ["asszembly1_2", "asszemblyjigolo1_2"],
            "pos": (9.5, 0),
            "colour": "#b6b3b3",
        },
        {
            "name": "asszemblyjigolo1_2",
            "jump": ["asszemblyjigolo1_3"],
            "pos": (9.5, 1),
            "colour": "#b6b3b3",
            
        },
        {
            "name": "asszemblyjigolo1_3",
            "jump": ["asszembly1shitstorm", "fugitivesfromasszembly1"],
            "pos": (9.5, 2),
            "colour": "#b6b3b3",
        },
        {
            "name": "fugitivesfromasszembly1",
            "jump": [
                "asszemblyjigolo1encounter", 
                "asszemblyjigolokindagaytoilet",
                "asszemblyjigolodiscoverthefood",
                "asszemblyjigoloviceland",
            ],
            "call": ["asszemblyjigolo1encounter"],
            "pos": (9.5, 3),
            "colour": "#b6b3b3",
        },
        {
            "name": "asszemblyjigolo1encounter",
            "jump": ["asszembly1shitstorm"],
            "pos": (9.5, 4),
            "colour": "#b6b3b3",
        },
    ])

    # 5.2 jig toilet
    labels.extend([
        {
            "name": "asszemblyjigolokindagaytoilet",
            "jump": ["szemeettheleatgaytoilet", "toiletstudies1"],
            "pos": (10, 0.5),
            "colour": "#5e33ff",
        },
        {
            "name": "toiletstudies1",
            "jump": "recess1a",
            "pos": (10, 1.5),
            "colour": "#5e33ff",
        },
        {
            "name": "szemeettheleatgaytoilet",
            "jump": "recess1a",
            "pos": (10, 2.5),
            "colour": "#5e33ff",
        },
    ])

    # 5.3 jig food
    labels.extend([
        {
            "name": "asszemblyjigolodiscoverthefood",
            "jump": "recess1a",
            "pos": (10, 3.5),
            "colour": "#ff3633",
        },
    ])

    # 5.4 jig vices
    labels.extend([
        {
            "name": "asszemblyjigoloviceland",
            "jump": "recess1",
            "call": "garyreeducation",
            "pos": (10.5, 0),
            "colour": "#333cff",
        },
        {
            "name": "garyreeducation",
            "jump": None,
            "pos": (10.5, 1),
            "colour": "#333cff",
        },
    ])

    # 5.5 assembly shitstorm
    labels.extend([
        {
            "name": "asszembly1shitstorm",
            "jump": "dead",
            "pos": (10.5, 2),
            "colour": "#ff5733",
        },
    ])