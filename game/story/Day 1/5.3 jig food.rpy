label asszemblyjigolodiscoverthefood:
    sze "\"So we got away\""
    jit "\"Damn, you were a boss\""
    $ jit.friendship += 1
    jit "\"So let's see what lies beyond the fence\""
    "Both you and Jitian wander up along Parramatta Road for a distamce and decide to turn left onto a Nortom Street"
    scene bg norton
    jit "\"whoa, cheap ass viet rolls, a kebab shop and a pho place?!?!\""
    sze "\"rip, I'm broke\""
    jit "\"Fuck, me too\""
    jit "\"Oh, and there's a Grill'd, if you want tofu and apple burgers\""
    sze "\"Don't they also sell meat burgers?\""
    jit "\"Why would you want that when you can get kebabs\""
    jit "\"Anyways, this gives me a few ideas\""
    jit "\"Mate, imagine the money that we could make off of this...\""
    $ game.delivery = True
    $ game.norton = True
    sze "\"Like, 5 cents?\""
    sze "\"We should probs get back for recess...\""
    jit "\"Yeah, yeah, ok\""
    jump recess1a

    # HSPs +3 strength, -1 intel
    # fish and chips +2 intel
    # pho +1 strength +1 intel +1 thirst
    # pork rolls +2 charm
    # vegan shite = +3 fort -1 strength -1 dikfriendship
