init python:
    import copy
    inventory = Inventory(**{
        "who": sze,
        "name": "Bag", 
        "max_items": 10, 
        "grid_view": False,
    })
    #$ inventory = Inventory("Locker", 10)
    for item in itemList:
        for amount in xrange(2):
            newItem = copy.deepcopy(itemList[item])
            inventory.add(newItem, 1)
