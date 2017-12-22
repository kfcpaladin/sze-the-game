init python:
    inventory = Inventory("Bag", 10, False)
    #$ inventory = Inventory("Locker", 10)
    for item in itemList:
        inventory.add(itemList[item], 1)
