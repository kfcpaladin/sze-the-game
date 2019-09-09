define items = load_items()

init -1 python:
    from models.inventory import Inventory, Item, ItemCache, AttributeModifier

    def load_items(): 
        items = ItemCache()

        # ball
        items.add(Item(
                id="ball",
                name="ball",
                description="bouncy thing",
                icon=loadImage("item_ball.png")))

        items.get("ball").add_action(AttributeModifier("charm", -1))
        items.get("ball").add_action(AttributeModifier("intellect", -1))
        items.get("ball").add_action(AttributeModifier("strength", 1))

        # axe
        items.add(Item(
                id="axe",
                name="axe",
                description="weaponz",
                icon=loadImage("item_axe.png")))

        items.get("axe").add_action(AttributeModifier("charm", 2))
        items.get("axe").add_action(AttributeModifier("intellect", -10))
        items.get("axe").add_action(AttributeModifier("strength", 10))

        # money
        items.add(Item(
                id="money",
                name="monies",
                description="cash monies wads",
                icon=loadImage("item_bag.png")))

        items.get("money").add_action(AttributeModifier("charm", 10))
        items.get("money").add_action(AttributeModifier("intellect", 4))
        items.get("money").add_action(AttributeModifier("strength", -3))

        # fireaxe
        items.add(Item(
                id="fireaxe",
                name="fireaxe",
                description="weaponz",
                icon=loadImage("item_axe.png")))

        items.get("fireaxe").add_action(AttributeModifier("charm", 5))
        items.get("fireaxe").add_action(AttributeModifier("intellect", -20))
        items.get("fireaxe").add_action(AttributeModifier("strength", 15))

        # calc
        items.add(Item(
                id="calc",
                name="calculator",
                description="smarts + 1",
                icon=loadImage("item_calc1.png")))

        items.get("calc").add_action(AttributeModifier("charm", -10))
        items.get("calc").add_action(AttributeModifier("intellect", 20))
        items.get("calc").add_action(AttributeModifier("strength", -10))

        # god
        items.add(Item(
                id="god",
                name="The god particle",
                description="Turns you into michael kirby",
                icon=loadImage("item_kirby.png")))

        items.get("god").add_action(AttributeModifier("charm", 1000))
        items.get("god").add_action(AttributeModifier("fort", 1000))
        items.get("god").add_action(AttributeModifier("intellect", 1000))
        items.get("god").add_action(AttributeModifier("strength", 1000))
        items.get("god").add_action(AttributeModifier("thirst", -1000))

        # neo armstrong
        items.add(Item(
                id="neo armstrong",
                name="neo armstrong cyclone jet armstrong cannon",
                description="The most powerful weapon used by an alien civilization, able to destroy wipe out entire species (sunrise don;t sue us)",
                icon=loadImage("item_cannon.png")))

        items.get("neo armstrong").add_action(AttributeModifier("charm", 1000))
        items.get("neo armstrong").add_action(AttributeModifier("fort", -100))
        items.get("neo armstrong").add_action(AttributeModifier("intellect", -1000))
        items.get("neo armstrong").add_action(AttributeModifier("strength", 1000))
        items.get("neo armstrong").add_action(AttributeModifier("thirst", 1000))

        return items

