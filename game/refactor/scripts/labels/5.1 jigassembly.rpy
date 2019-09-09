init python:

    # 5.1 jig assembly
    labels.extend([
        {
            "name": "asszembly1jigolo",
            "jump": ["asszembly1_2", "asszemblyjigolo1_2"],
            "pos": (9.5, 0),
            "colour": PrimaryColours.GREY,
        },
        {
            "name": "asszemblyjigolo1_2",
            "jump": ["asszemblyjigolo1_3"],
            "pos": (9.5, 1),
            "colour": PrimaryColours.GREY,
            
        },
        {
            "name": "asszemblyjigolo1_3",
            "jump": ["asszembly1shitstorm", "fugitivesfromasszembly1"],
            "pos": (9.5, 2),
            "colour": PrimaryColours.GREY,
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
            "colour": PrimaryColours.GREY,
        },
        {
            "name": "asszemblyjigolo1encounter",
            "jump": ["asszembly1shitstorm"],
            "pos": (9.5, 4),
            "colour": PrimaryColours.GREY,
        },
    ])

    # 5.2 jig toilet
    labels.extend([
        {
            "name": "asszemblyjigolokindagaytoilet",
            "jump": ["szemeettheleatgaytoilet", "toiletstudies1"],
            "pos": (10, 0.5),
            "colour": PrimaryColours.PURPLE,
        },
        {
            "name": "toiletstudies1",
            "jump": "recess1a",
            "pos": (10, 1.5),
            "colour": PrimaryColours.PURPLE,
        },
        {
            "name": "szemeettheleatgaytoilet",
            "jump": "recess1a",
            "pos": (10, 2.5),
            "colour": PrimaryColours.PURPLE,
        },
    ])

    # 5.3 jig food
    labels.extend([
        {
            "name": "asszemblyjigolodiscoverthefood",
            "jump": "recess1a",
            "pos": (10, 3.5),
            "colour": PrimaryColours.RED,
        },
    ])

    # 5.4 jig vices
    labels.extend([
        {
            "name": "asszemblyjigoloviceland",
            "jump": "recess1",
            "call": "garyreeducation",
            "pos": (10.5, 0),
            "colour": PrimaryColours.BLUE,
        },
    ])

    # 5.5 assembly shitstorm
    labels.extend([
        {
            "name": "asszembly1shitstorm",
            "jump": "dead",
            "pos": (10.5, 2),
            "colour": PrimaryColours.ORANGE,
        },
    ])