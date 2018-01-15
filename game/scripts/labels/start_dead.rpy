init python:

    # dead
    labels.extend([
        {
            "name": "dead",
            "jump": "start",
            "colour": "#000000",
            "font_colour": "#ffffff",
            "pos": (4.5, -3.75),
        },
        {
            "name": "deadrestart",
            "jump": "start",
            "colour": "#000000",
            "font_colour": "#ffffff",
            "pos": (4, -3.75),
        },
        {
            "name": "actualdead",
            "jump": None,
            "colour": "#000000",
            "font_colour": "#ffffff",
            "pos": (3.5, -3.75),
        },
    ])

    # script
    labels.extend([
        {
            "name": "start",
            "jump": "schoolday1",
            "colour": "#5e33ff",
            "pos": (2, -3.75),
        },
    ])