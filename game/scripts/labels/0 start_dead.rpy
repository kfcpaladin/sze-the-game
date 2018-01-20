init python:

    # dead
    labels.extend([
        {
            "name": "dead",
            "jump": "start",
            "colour": colour.black,
            "pos": (4.5, -3.75),
        },
        {
            "name": "deadrestart",
            "jump": "start",
            "colour": colour.black,
            "pos": (4, -3.75),
        },
        {
            "name": "actualdead",
            "jump": None,
            "colour": colour.black,
            "pos": (3.5, -3.75),
        },
    ])

    # script
    labels.extend([
        {
            "name": "start",
            "jump": "schoolday1",
            "colour": colour.purple,
            "pos": (2, -3.75),
        },
    ])