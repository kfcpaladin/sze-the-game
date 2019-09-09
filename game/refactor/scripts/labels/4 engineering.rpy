init python:
    # 4 engineering
    labels.extend([
        {
            "name": "eng1p1",
            "jump": ["eng1p1p1", "eng1p1p2", "eng1p1p3", "eng1p1naughtycorner"],
            "pos": (6, 0),
            "colour": PrimaryColours.BLUE,
        },
        {
            "name": "eng1p1naughtycorner",
            "jump": ["dead", "timetravel1", "eng1p2"],
            "pos": (6, 1),
            "colour": PrimaryColours.BLUE,
        },
        {
            "name": "timetravel1",
            "jump": "schoolday1",
            "pos": (6, 2),
            "colour": PrimaryColours.BLUE,
        },
        {
            "name": "eng1p1p1",
            "jump": "eng1p1p3",
            "pos": (6.25, 0.5),
            "colour": PrimaryColours.BLUE,
        },
        {
            "name": "eng1p1p2",
            "jump": "eng1p2",
            "pos": (6.25, 1.5),
            "colour": PrimaryColours.BLUE,
        },
        {
            "name": "eng1p1p3",
            "jump": ["yangrantp1_1", "yangrantp1_2", "yangrantp1_3"],
            "pos": (6.25, 2.5),
            "colour": PrimaryColours.BLUE,
        },
        {
            "name": "yangrantp1_1",
            "jump": "eng1p2",
            "pos": (6.5, 0),
            "colour": PrimaryColours.BLUE,
        },
        {
            "name": "yangrantp1_2",
            "jump": ["eng1p2"],
            "pos": (6.5, 1),
            "colour": PrimaryColours.BLUE,
        },
        {
            "name": "yangrantp1_3",
            "jump": "eng1p2",
            "pos": (6.5, 2),
            "colour": PrimaryColours.BLUE,
        },
        {
            "name": "eng1p2",
            "jump": ["asszembly1", "eng1p1naughtycorner"],
            "pos": (6.5, 3),
            "colour": PrimaryColours.BLUE,
        },
    ])