# Initialise item class 
python early:
    import renpy.store as store

    class Item(store.object):
        def __init__(self, name, desc, stat, icon=False, used=False):
            self.name = name # name of item
            self.desc = desc #description of item
            self.stat = stat
            self.icon = icon #image
            self.used = used

            #more things about item
        def equip(self, person): # what happens when you use item
            if self.used is False:
                for stat in self.stat:
                    person._changeAttribute(stat, self.stat[stat])
                self.used = True
        
        def unequip(self, person):
            if self.used is True:
                for stat in self.stat:
                    person._changeAttribute(stat, -self.stat[stat])
                self.used = False
        
        def toggle(self, person):
            if self.used is False:
                self.equip(person)
            else:
                self.unequip(person)