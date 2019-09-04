init python:

    # dead
    labels.extend([
        {
            "name": "dead",
            "jump": "start",
            "colour": PrimaryColours.BLACK,
            "pos": (4.5, -3.75),
        },
        {
            "name": "deadrestart",
            "jump": "start",
            "colour": PrimaryColours.BLACK,
            "pos": (4, -3.75),
        },
        {
            "name": "actualdead",
            "jump": None,
            "colour": PrimaryColours.BLACK,
            "pos": (3.5, -3.75),
        },
    ])

    # script
    labels.extend([
        {
            "name": "start",
            "jump": "schoolday1",
            "colour": PrimaryColours.PURPLE,
            "pos": (2, -3.75),
        },
    ])