init 1 python:
    import copy
    bag = Inventory(**{
        "who": sze,
        "name": "Bag", 
        "money": 0,
        "max_items": 10, 
    })
    
    for key, item in itemList.iteritems():
        bag.add(item)

    locker = Inventory(**{
        "who": sze,
        "name": "Locker",
        "money": 0,
        "max_items": None,
    })

    khajiit = Inventory(**{
        "who": pra,
        "name": "Khajiit",
        "money": 99999,
        "max_items": None,
    })

    canteen = Inventory(**{
        "who": mox,
        "name": "Skinner",
        "money": 99999,
        "max_items": None,
    })