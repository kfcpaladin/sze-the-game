init -10 python:
    from copy import deepcopy
    class Inventory:
        def __init__(self, who, name, max_items):
            self.inv = []  # initialise list to store items, first in is top of list
            self.who = who
            self.name = name #name of inventory i.e. locker or bag
            self.max_items = max_items # maximum items it can hold, bag = 6, locker = infinte
            # sorts
            #self.sort_by = self.sort_name #alphabetical
            #self.sort_order = True #ascending, descending

        def add(self, item): #add an item
            if len(self.inv) < self.max_items or self.max_items is None:
                self.inv.append(deepcopy(item))

        def remove(self, item): #remove an item -1
            self.inv.remove(item)

        # sorts, figure out later
        #def sort_name(self):
        #    self.inv.sort(key=lambda i: i[0].name, reverse=self.sort_order)

        #def sort_qty(self):
        #    self.inv.sort(key=lambda i: i[1], reverse=self.sort_order)

        #def sort_value(self):
        #    self.inv.sort(key=lambda i: i[0].value, reverse=self.sort_order)

        def debugItems(self):
            for index, item in enumerate(self.inv):
                print("Item {0}: {1}".format(index, item.name))