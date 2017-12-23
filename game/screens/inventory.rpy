############################## inventory screens ##############################################
style bag_inventory:
    xoffset 44
    yoffset 132

style bag_item_frame:
    xsize 112
    ysize 112

style bag_item_box:
    xmaximum 112
    ymaximum 112

# currently inefficent, can probably optimise
screen inventory_view(inventory=inventory):
    add "Diary.jpg"
    use inventory_stats(inventory.who)
    # Variables
    $ colours = {
        "item_used": "#00993371",
        "item_not_used": "#e6ac0071",
        "tooltip": "#00000071",
        "background": "#00000000",
    }
    $ grid = {
        "size": (112, 112),
        "spacing": 5,
        "offset": (44, 132),
        "dimensions": (580, 580),
        "matrix": (5, int((len(inventory.inv)-1)/5)+1),
    }
    frame:
        area (0, 0, 500, 50)
        text "{0}".format(unicode.title(inventory.name)): 
            size 45
            xoffset 30
            yoffset 10
            font "DejaVuSans.ttf"
    frame:
        background Color(colours["background"])
        style "bag_inventory"
        hbox:
            ysize 580
            $ _grid_name = inventory.name
            vpgrid id (_grid_name):
                xsize grid["dimensions"][0] 
                ysize grid["dimensions"][1] 
                spacing 5
                cols grid["matrix"][0] 
                rows grid["matrix"][1] 
                draggable False
                mousewheel True
                for index, item in enumerate(inventory.inv):
                    # Create an item element in the list
                    frame:
                        style "bag_item_frame"
                        if item.used:
                            background Color(colours["item_used"])
                        else:
                            background Color(colours["item_not_used"]) 
                        hbox:
                            style "bag_item_box"
                            imagebutton:
                                style "bag_item_box"
                                idle Frame(item.icon, grid["size"][0], grid["size"][1], grid["size"][0], grid["size"][1])
                                hover Frame(im.Sepia(item.icon), grid["size"][0], grid["size"][1], grid["size"][0], grid["size"][1])
                                action [
                                    Play ("sound", "sfx/vpunch.ogg"),
                                    Function(item.toggle, inventory.who),
                                ]
                                hovered [ 
                                    Show("gui_tooltip",item=item) 
                                ]
                                unhovered Show("gui_tooltip")
            if grid["matrix"][1] > grid["matrix"][0]:
                frame:
                    vbar:
                        value YScrollValue(_grid_name)

screen gui_tooltip(item=False):
    $ desc_box = {
        "offset": (703, 95),
        "size": (646, 429),
    }
    $ colours = {
        "not_used": "#e6ac00",
        "used": "#009933",
    }
    # Description box
    frame:
        xoffset desc_box["offset"][0]
        yoffset desc_box["offset"][1]
        xsize   desc_box["size"][0]
        vbox:
            ymaximum desc_box["size"][1]
            # Give an item description if there is one
            if item:
                text "{b}Name: {/b}" + "{0}".format(item.name)
                frame:
                    xsize desc_box["size"][0]
                    if item.used:
                        background Solid(colours["used"])
                    else:
                        background Solid(colours["not_used"])
                    vbox:
                        xmaximum desc_box["size"][0]
                        text "{b}Brief: {/b}" + "{0}".format(item.desc)
                        text "{b}Stats: {/b}"
                        for stat, value in item.stat.iteritems():
                            if value > 0:
                                text "+{0} {1}".format(value, stat)
                            else:
                                text "{0} {1}".format(value, stat)
            # Indicate user to hover over item
            else:
                text "{b}Description{/b}"
                text "Hover over an item for description"

    # Statistics box

screen inventory_stats(person=False):
    $ stat_box = {
        "offset": (703, 577),
        "size": (646, 75),
    }
    frame:
        xoffset stat_box["offset"][0]
        yoffset stat_box["offset"][1]
        xsize   stat_box["size"][0]
        vbox:
            ymaximum stat_box["size"][1]
            if person:
                text "{b}" + "{0}'s statistics".format(unicode.title(person.name)) + "{/b}"
                for stat in person.attributes:
                    text "{0}: {1}".format(unicode.title(stat), getattr(person, stat))
            else:
                text "{b}Error: No user assigned to inventory{/b}"
