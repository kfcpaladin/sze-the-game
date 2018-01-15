init python:

    # 3.0 physics rpy
    labels.extend([
        {
            "name": "phys1",
            "jump": ["phys1answered", "phys1nothing", "phys1talked"],
            "pos": (2.5, 0),
        },
        {
            "name": "phys1answered",
            "jump": ["phys1answered_a", "phys1answered_b"],
            "pos": (2.5, 1),
        },
        {
            "name": "phys1answered_a",
            "jump": "dead",
            "pos": (2.5, 2),
        },
        {
            "name": "phys1answered_b",
            "jump": "phys1part2",
            "pos": (2.5, 3),
        },
        {
            "name": "phys1nothing",
            "jump": "phys1part2",
            "pos": (2.75, 0.5),
        },
        {
            "name": "phys1talked",
            "jump": "phys1part2",
            "pos": (2.75, 1.5),
        },
        {
            "name": "phys1p2p1",
            "jump": ["phys1p3p2", "phys1p3principal1"],
            "call": "phys1p2p4",
            "pos": (2.75, 2.5),
        },
        {
            "name": "phys1p2p2",
            "jump": ["phys1p3p3", "phys1p3p1", "dead", "phys1p2p3"],
            "pos": (3, 0),
        },
        {
            "name": "phys1p2p3",
            "jump": ["phys1p3p1", "phys1p3principal2"],
            "call": "phys1p2p4",
            "pos": (3, 1),
        },
        {
            "name": "phys1p2p4",
            "jump": None,
            "pos": (3, 2),
        },
        {
            "name": "phys1p3p1",
            "jump": "eng1p1",
            "pos": (3, 3),
        },
        {
            "name": "phys1p3p2",
            "jump": "eng1p1",
            "pos": (3.25, 0.5),
        },
        {
            "name": "phys1p3p3",
            "jump": "eng1p1",
            "pos": (3.25, 1.5),
        }
    ])