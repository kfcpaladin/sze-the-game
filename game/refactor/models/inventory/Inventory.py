from .InventoryItem import InventoryItem

class Inventory(object):
    def __init__(self, who, name, money, max_items=None):
        self.inv = []  # initialise list to store items, first in is top of list
        self.who = who
        self.name = name #name of inventory i.e. locker or bag
        self.money = money
        self.max_items = max_items # maximum items it can hold, bag = 6, locker = infinte
        # sorts
        #self.sort_by = self.sort_name #alphabetical
        #self.sort_order = True #ascending, descending

    @property
    def items(self):
        return self.inv

    def add(self, item): #add an item
        if len(self.inv) < self.max_items or self.max_items is None:
            # decorate item with user data
            self.inv.append(InventoryItem(self.who, item))

    def remove(self, item): 
        self.inv.remove(item)

    def deposit(self, amount):
        self.money -= amount
    
    def withdraw(self, amount):
        self.money += amount

    # sorts, figure out later
    #def sort_name(self):
    #    self.inv.sort(key=lambda i: i[0].name, reverse=self.sort_order)

    #def sort_qty(self):
    #    self.inv.sort(key=lambda i: i[1], reverse=self.sort_order)

    #def sort_value(self):
    #    self.inv.sort(key=lambda i: i[0].value, reverse=self.sort_order)