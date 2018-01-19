############################## inventory screens ##############################################
# currently inefficent, can probably optimise
screen bag_view(bag=bag):
    modal True
    # screen components
    add loadImage("screen_bg_diaryGrid.png")
    use diary_nav
    use diary_title(bag.name)
    # show inventory and stats
    use bag_inventory(bag)
    use attribute_info(bag.who, pos=Vector(695, 95), size=Vector(650,415))

# display the bag inventory
screen bag_inventory(bag, pos=Vector(43,131), size=Vector(580, 580), iconSize=Vector(112, 112), borderThickness=5):
    # Variables
    default clearColour = "#00000000"
    default matrix = Vector(5, int((len(bag.inv)-1)/5)+1)
    # render inventory
    frame:
        background clearColour
        xoffset pos.x-borderThickness
        yoffset pos.y-borderThickness
        hbox:
            # render inventory grid
            $ _grid_name = "{0}_vpgrid".format(bag.name)
            vpgrid id (_grid_name):
                xsize size.x
                ysize size.y
                spacing borderThickness
                cols matrix.x
                rows matrix.y
                draggable False
                mousewheel True
                for item in bag.inv:
                    use bag_item(item, iconSize.x, iconSize.y)
            # if rows exceed columns, assume we need to scroll
            if matrix.y > matrix.x:
                frame:
                    ysize size.y
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
                Function(playsfx, "vpunch.ogg"),
                Function(item.toggle, bag.who),
            ]
            hovered Show("bag_tooltip", None, item) 
            unhovered Hide("bag_tooltip")


screen bag_tooltip(item):
    default colour = {
        "not_used": colour.yellow,
        "used": colour.green,
    }
    default mousePos = getMousePosition()
    default transparency = "{:02x}".format(180)
    default minWidth = 300
    default maxWidth = 600
    # Description box
    vbox:
        xminimum minWidth
        xmaximum maxWidth
        xoffset mousePos[0]+20
        yoffset mousePos[1]+40
        frame:
            background Solid("#800000"+transparency)
            has vbox
            # Give an item description if there is one
            if item:
                text "{b}Name: {/b}" + "{0}".format(item.name)
                frame:
                    xminimum minWidth
                    xmaximum maxWidth
                    if item.used:
                        background Solid(colour["used"]+transparency)
                    else:
                        background Solid(colour["not_used"]+transparency)
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
                text "{b}Error: {/b}Item is None type"