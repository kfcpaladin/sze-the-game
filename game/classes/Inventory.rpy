########################################################################################################################
# inventory itself
python early:
    import renpy.store as store

    class Inventory(store.object):
        def __init__(self, who, name, max_items, grid_view):
            self.inv = []  # initialise list to store items, first in is top of list
            self.who = who
            self.name = name #name of inventory i.e. locker or bag
            self.max_items = max_items # maximum items it can hold, bag = 6, locker = infinte
            self.grid_view = grid_view
            # sorts
            #self.sort_by = self.sort_name #alphabetical
            #self.sort_order = True #ascending, descending

        def add(self, item, amount): #add an item +1
            self.inv.append(item)
            return ('success')

        def remove(self, item, amount=1): #remove an item -1
            self.inv.remove(item)
            return ('success')

        # sorts, figure out later
        #def sort_name(self):
        #    self.inv.sort(key=lambda i: i[0].name, reverse=self.sort_order)

        #def sort_qty(self):
        #    self.inv.sort(key=lambda i: i[1], reverse=self.sort_order)

        #def sort_value(self):
        #    self.inv.sort(key=lambda i: i[0].value, reverse=self.sort_order)