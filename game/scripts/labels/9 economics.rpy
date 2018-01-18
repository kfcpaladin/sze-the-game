init python:

    # 9 economics
    labels.extend([
        {
            "name": "econ1",
            "jump": None,
            "call": ["econ1kahoot1", "dead"],
            "pos": (19, 0),
        },
        {
            "name": "econ1kahoot1",
            "jump": None,
            "call": ["kahootGame"],
            "pos": (19, 1),
        },
    ])