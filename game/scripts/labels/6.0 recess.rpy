init python:

    # 6.0 recess
    labels.extend([
        {
            "name": "recess1",
            "jump": "recess1a",
            "pos": (13, 0),
        },
        {
            "name": "recess1a",
            "jump": ["english1", "dead", "actualdead", "recess1a"],
            "call": ["fortmap"],
            "pos": (13, 1),
        },
    ])