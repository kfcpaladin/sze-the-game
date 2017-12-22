########################################################################################################################
# initialising inventory data structures

# player


# objects in inventory = Items
init python:
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


# inventory itself
init python:
    import renpy.store as store

    class Inventory(store.object):
        def __init__(self, name, max_items, grid_view):
            self.inv = []  # initialise list to store items, first in is top of list
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

############################## inventory screens ##############################################

# currently inefficent, can probably optimise
screen bag_button:
    textbutton "Open Bag" action [ Show("bag_screen"), Hide("bag_button")] align (0.95, 0.04)

screen bag_screen:
    modal True
    textbutton "Close Bag" action [ Hide("bag_screen"), Show("bag_button")] align (0.95, 0.04)
    frame:
        style_group "bagstyle"
        vbox:
            spacing 25
            vbox:
                use inventory_view
                #text "Bag:"
                #for item in inventory.inv:
                    #text ("[item]")
screen inventory_view:
    frame:
        style_group "bagstyle"
        area (0, 0, 500, 50)
        label _("Bag")
    frame:
        style_group "bagstyle"
        hbox:
            spacing 25
            vbox:
                side "c r":
                    style_group "bagstyle"
                    area (0, 0, 250, 500)
                    vpgrid id ("vp"+inventory.name):
                        draggable True
                        mousewheel True
                        xsize 300 ysize 400
                        cols 1 spacing 25
                        for item in inventory.inv:
                            $ name = item.name
                            $ desc = item.desc
                            hbox:
                                if item.icon:
                                    $ icon = item.icon
                                    $ hover_icon = im.Sepia(icon)
                                    imagebutton:
                                        idle icon
                                        hover hover_icon
                                        action [Hide("gui_tooltip"), Show("bag_button"), Hide("bag_screen")]
                                        hovered [ Play ("sound", "sfx/click.wav"), Show("gui_tooltip",item=item) ]
                                        unhovered Hide("gui_tooltip")
                                text name

                        #if len(inventory.inv) == 0:
                            #add Null(height=100,width=100)
                    vbar value YScrollValue("vp"+inventory.name)
        #hbox:
            #area (0, 0, 200, 200)

screen gui_tooltip(item=False):
    if item:
        hbox:
            xalign 0.3 yalign 0.3
            text "[item.desc]"


screen locker_screen:
    modal True
    textbutton "Close Locker" action [ Hide("locker_screen")] align (0.5, 0.04)
    frame:
        style_group "lockstyle"

        vbox:
            align (0.1, 0.3)
            spacing 25

            text "Lockers: and this shouldn't be the same as the bag, need to change..."
            for item in inventory.inv:
                $ name = item.name
                text name

init -2:
    ## STYLES ##
    # bag
    style bagstyle_frame:
        xalign 0.05
        yalign 0.35
    style bagstyle_label_text:
        size 30
    style bagstyle_label:
        xalign 0.5
    # lockers
    style lockstyle_frame:
        xalign 0.5
        yalign 0.5
    style lockstyle_label_text:
        size 30
    style lockstyle_label:
        xalign 0.5
    style lockstyle_frame:
        xalign 0.5
        yalign 0.5
    # quests
    style queststyle_frame:
        xalign 0.5
        yalign 0.5
    style queststyle_label_text:
        size 30
    style queststyle_label:
        xalign 0.5
