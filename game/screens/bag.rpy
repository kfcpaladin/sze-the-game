############################## inventory screens ##############################################
# currently inefficent, can probably optimise
screen bag_view(bag=bag):
    # screen components
    add loadImage("diaryGrid.jpg")
    use diary_nav
    use diary_title(bag.name)
    use bag_stats(bag.who)
    use bag_tooltip
    # Variables
    default clearColour = "#00000000"
    default iconSize = (112, 112)
    default gapSize = 5
    default offset = (43, 131)
    default dimensions = (580, 580)
    default matrix = (5, int((len(bag.inv)-1)/5)+1)
    # render inventory
    frame:
        background clearColour
        xoffset offset[0] - gapSize
        yoffset offset[1] - gapSize
        hbox:
            
            $ _grid_name = "{0}_vpgrid".format(bag.name)
            vpgrid id (_grid_name):
                xsize dimensions[0]
                ysize dimensions[1]
                spacing gapSize
                cols matrix[0]
                rows matrix[1]
                draggable False
                mousewheel True
                for item in bag.inv:
                    use bag_item(item, iconSize[0], iconSize[1])
            if matrix[1] > matrix[0]:
                frame:
                    vbar:
                        value YScrollValue(_grid_name)

# display a bag item
screen bag_item(item, width, height):
    default colour = {
        "item_used":     "#00993371",   # Green
        "item_not_used": "#e6ac0071",   # Orange
        "item_blocked":  "#b30000",     # Red
    }
    frame:
        xsize width
        ysize height
        if item.used:
            background Color(colour["item_used"])
        else:
            background Color(colour["item_not_used"]) 
        imagebutton:
            xmaximum width
            ymaximum height
            idle  Frame(item.icon, width, height, width, height)
            hover Frame(im.Sepia(item.icon), width, height, width, height)
            action [
                Play ("sound", "sfx/vpunch.ogg"),
                Function(item.toggle, bag.who),
            ]
            hovered [ 
                Show("bag_tooltip",item=item) 
            ]
            unhovered Show("bag_tooltip")


screen bag_tooltip(item=None):
    default colour = {
        "not_used": "#e6ac00",
        "used": "#009933",
    }
    # Description box
    vbox:
        style "bag_tooltip"
        frame:
            style "bag_tooltip_frame"
            has vbox
            # Give an item description if there is one
            if item:
                text "{b}Name: {/b}" + "{0}".format(item.name)
                frame:
                    style "bag_tooltip_frame"
                    if item.used:
                        background Solid(colour["used"])
                    else:
                        background Solid(colour["not_used"])
                    vbox:
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
screen bag_stats(person):
    vbox:
        style "bag_stats"
        frame:
            style "bag_stats_frame"
            has vbox
            text "{b}" + "{0}'s statistics".format(unicode.title(person.name)) + "{/b}"
            for stat in person.attributes:
                text "{0}: {1}".format(unicode.title(stat), getattr(person, stat))

#########################################################################
style bag_tooltip:
    xoffset 703
    yoffset 95
    xsize 646
    ysize 429

style bag_tooltip_frame:
    xsize 646
    ymaximum 429

style bag_stats:
    xoffset 703
    yoffset 577
    xsize 646
    ysize 75

style bag_stats_frame:
    xsize 646
    ymaximum 75
