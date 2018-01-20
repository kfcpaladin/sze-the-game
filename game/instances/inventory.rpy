init python:
    import copy
    bag = Inventory(**{
        "who": sze,
        "name": "Bag", 
        "max_items": 10, 
    })
    
    for key, item in itemList.iteritems():
        bag.add(copy.deepcopy(item))

    locker = Inventory(**{
        "who": sze,
        "name": "Locker",
        "max_items": None,
    })