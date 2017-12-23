init python:
    import copy
    bag = Inventory(**{
        "who": sze,
        "name": "Bag", 
        "max_items": 10, 
    })
    #$ inventory = Inventory("Locker", 10)
    for item in itemList:
        for amount in xrange(2):
            newItem = copy.deepcopy(itemList[item])
            bag.add(newItem)

    locker = Inventory(**{
        "who": sze,
        "name": "Locker",
        "max_items": None,
    })