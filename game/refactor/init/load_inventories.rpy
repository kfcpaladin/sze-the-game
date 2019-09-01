default inventories.bag = load_bag(sze, items)    

default inventories.locker = Inventory(
    who=sze,
    name="Locker",
    money=0,
    max_items=None)

default inventories.khajiit = Inventory(
    who=pra,
    name="Khajiit",
    money=99999)

default inventories.canteen = Inventory(
    who=mox,
    name="Skinner",
    money=99999)


init -1 python:

    def load_bag(owner, items):
        bag = Inventory(
            who=owner,
            name="bag",
            money=0,
            max_items=10)

        bag.add(items.get("ball"))
        bag.add(items.get("axe"))
        bag.add(items.get("money"))
        bag.add(items.get("fireaxe"))
        bag.add(items.get("calc"))
        return bag


