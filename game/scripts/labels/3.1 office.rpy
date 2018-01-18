init python:

    # 3.1 office
    labels.extend([
        {
            "name": "phys1p3principal1",
            "jump": ["dead", "phys1p3principal3", "phys1p3principal4"],
            "pos": (3.5, 0),
        },
        {
            "name": "phys1p3principal2",
            "jump": ["dead", "eng1p1"],
            "pos": (3.5, 1),
        },
        {
            "name": "phys1p3principal3",
            "jump": "eng1p1",
            "pos": (3.5, 2),
        },
        {
            "name": "phys1p3principal4",
            "jump": "eng1p1",
            "pos": (3.5, 3),
        },
    ])