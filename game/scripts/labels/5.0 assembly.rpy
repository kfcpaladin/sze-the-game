init python:
    # 5 assembly
    labels.extend([
        {
            "name": "asszembly1",
            "jump": ["asszembly1p1"],
            "pos": (9, 0),
            "colour": PrimaryColours.YELLOW,
        },
        {
            "name": "asszembly1p1",
            "jump": ["asszembly1jigolo", "asszembly1_2"],
            "pos": (9, 1),
            "colour": PrimaryColours.YELLOW,
        },
        {
            "name": "asszembly1_2",
            "jump": ["asszembly1_3"],
            "pos": (9, 2),
            "colour": PrimaryColours.YELLOW,
        },
        {
            "name": "asszembly1_3",
            "jump": ["asszembly1_4", "dead"],
            "call": ["quest1electionpromise1_a"],
            "pos": (9, 3),
            "colour": PrimaryColours.YELLOW,
        },
        {
            "name": "quest1electionpromise1_a",
            "jump": None,
            "pos": (9, 4),
            "colour": PrimaryColours.YELLOW,
        },
        {
            "name": "asszembly1_4",
            "jump": "recess1",
            "pos": (9, 5),
            "colour": PrimaryColours.YELLOW,
        },
    ])