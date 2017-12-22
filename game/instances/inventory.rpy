init python:
    inventory = Inventory(**{
        "who": sze,
        "name": "Bag", 
        "max_items": 10, 
        "grid_view": False,
    })
    #$ inventory = Inventory("Locker", 10)
    for item in itemList:
        inventory.add(itemList[item], 1)
