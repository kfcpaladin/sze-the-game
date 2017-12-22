# Initialise item class 
python early:
    import renpy.store as store

    class Item(store.object):
        def __init__(self, name, desc, stat, icon=False, equip=False):
            self.name = name # name of item
            self.desc = desc #description of item
            self.stat = stat
            self.icon = icon #image
            self.equip = equip
            #more things about item
        # def use(self): # what happens when you use item