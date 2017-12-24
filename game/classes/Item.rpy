# Initialise item class 
python early:
    import renpy.store as store

    class Item(store.object):
        def __init__(self, name, desc, stat, icon=False, used=False):
            self.name = name # name of item
            self.desc = desc #description of item
            self.stat = stat #dictionary with values
            self.icon = icon #image
            self.used = used # boolean to indicate usage

            #more things about item
        def equip(self, person): # what happens when you use item
            if self.used is False:
                for stat, value in self.stat.iteritems():
                    person._changeAttribute(stat, value)
                self.used = True
        
        def unequip(self, person):
            if self.used is True:
                for stat, value in self.stat.iteritems():
                    person._changeAttribute(stat, -value)
                self.used = False
        
        def toggle(self, person):
            if self.used is False:
                self.equip(person)
            else:
                self.unequip(person)
