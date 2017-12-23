############################## inventory screens ##############################################
# currently inefficent, can probably optimise
screen bag_view(bag=bag):
    add "Diary.jpg"
    use bag_stats(bag.who)
    # Variables
    $ colours = {
        "item_used": "#00993371",       # Green
        "item_not_used": "#e6ac0071",   # Orange
        "item_blocked": "#b30000",      # Red
        "background": "#00000000",      # Transparent
    }
    $ grid = {
        "size": (112, 112),
        "spacing": 5,
        "offset": (43, 131),
        "dimensions": (580, 580),
        "matrix": (5, int((len(bag.inv)-1)/5)+1),
    }
    frame:
        area (0, 0, 500, 50)
        text "{0}".format(unicode.title(bag.name)): 
            size 45
            xoffset 30
            yoffset 10
            font "DejaVuSans.ttf"
    frame:
        background Color(colours["background"])
        xoffset grid["offset"][0]-grid["spacing"]
        yoffset grid["offset"][1]-grid["spacing"]
        hbox:
            ysize 580
            $ _grid_name = bag.name
            vpgrid id (_grid_name):
                xsize grid["dimensions"][0] 
                ysize grid["dimensions"][1] 
                spacing 5
                cols grid["matrix"][0] 
                rows grid["matrix"][1] 
                draggable False
                mousewheel True
                for item in bag.inv:
                    # Create an item element in the list
                    frame:
                        xsize grid["size"][0]
                        ysize grid["size"][1]
                        if item.used:
                            background Color(colours["item_used"])
                        else:
                            background Color(colours["item_not_used"]) 
                        hbox:
                            xmaximum grid["size"][0]
                            ymaximum grid["size"][1]
                            imagebutton:
                                xmaximum grid["size"][0]
                                ymaximum grid["size"][1]
                                idle Frame(item.icon, grid["size"][0], grid["size"][1], grid["size"][0], grid["size"][1])
                                hover Frame(im.Sepia(item.icon), grid["size"][0], grid["size"][1], grid["size"][0], grid["size"][1])
                                action [
                                    Play ("sound", "sfx/vpunch.ogg"),
                                    Function(item.toggle, bag.who),
                                ]
                                hovered [ 
                                    Show("bag_tooltip",item=item) 
                                ]
                                unhovered Show("bag_tooltip")
            if grid["matrix"][1] > grid["matrix"][0]:
                frame:
                    vbar:
                        value YScrollValue(_grid_name)

screen bag_tooltip(item=False):
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

screen bag_stats(person=False):
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
