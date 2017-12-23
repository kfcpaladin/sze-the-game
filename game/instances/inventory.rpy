init python:
    import copy
    bag = Inventory(**{
        "who": sze,
        "name": "Bag", 
        "max_items": 10, 
    })
    #$ inventory = Inventory("Locker", 10)
    for key, item in itemList.iteritems():
        bag.add(item)

    locker = Inventory(**{
        "who": sze,
        "name": "Locker",
        "max_items": None,
    })