# display an inventory object 
screen bag_screen(bag, customConfig={}):
    default itemAlpha = 120
    default tooltipAlpha = 180
    default bagConfig = AttrDict({
        "itemColour": AttrDict({
            "item_used":     colour.green+"{:02x}".format(itemAlpha),
            "item_not_used": colour.yellow+"{:02x}".format(itemAlpha),
            "item_blocked":  colour.red+"{:02x}".format(itemAlpha),
        }),
        "tooltipColour": AttrDict({
            "item_used":     colour.green+"{:02x}".format(tooltipAlpha),
            "item_not_used": colour.yellow+"{:02x}".format(tooltipAlpha),
            "item_blocked":  colour.red+"{:02x}".format(tooltipAlpha),
            "background":    colour.maroon+"{:02x}".format(tooltipAlpha),
        }),
        "bag": bag, 
        "grid": AttrDict({
            "pos": Vector(43, 131),
            "size": Vector(580, 580),
            "iconSize": Vector(112, 112),
            "borderSize": 5,
            "matrix": Vector(5, int((len(bag.inv)-1)/5)+1),
        }),
        "tooltip": AttrDict({
            "xrange": AttrDict({
                "min": 300, 
                "max": 600
            }),
            "yrange": AttrDict({
                "min": 200, 
                "max": 400
            }),
        }),
    })

    use bag_inventory(bagConfig, bagConfig.grid.pos, bagConfig.grid.size, bagConfig.grid.iconSize, bagConfig.grid.borderSize, bagConfig.grid.matrix)



# display the bag inventory
screen bag_inventory(bagConfig, pos, size, iconSize, borderSize, matrix):
    # render inventory
    frame:
        background Solid(colour.clear)
        xoffset pos.x-borderSize
        yoffset pos.y-borderSize
        hbox:
            # render inventory grid
            $ _grid_name = "{0}_vpgrid".format(bagConfig.bag.name)
            vpgrid id (_grid_name):
                xsize size.x
                ysize size.y
                spacing borderSize
                cols matrix.x
                rows matrix.y
                draggable False
                mousewheel True
                for item in bagConfig.bag.inv:
                    use bag_item(bagConfig, item, iconSize.x, iconSize.y)
            # if rows exceed columns, assume we need to scroll
            if matrix.y > matrix.x:
                frame:
                    ysize size.y
                    vbar:
                        value YScrollValue(_grid_name)
    
# display a bag item
screen bag_item(bagConfig, item, width, height):
    frame:
        xsize width
        ysize height
        if item.used:
            background Solid(bagConfig.itemColour.item_used)
        else:
            background Solid(bagConfig.itemColour.item_not_used) 
        imagebutton:
            xmaximum width
            ymaximum height
            idle  Frame(item.icon, width, height, width, height)
            hover Frame(im.Sepia(item.icon), width, height, width, height)
            action [
                Function(playsfx, "vpunch.ogg"),
                Function(item.toggle, bagConfig.bag.who),
            ]
            hovered [
                Show("bag_tooltip", None, bagConfig, item, bagConfig.tooltip.xrange, bagConfig.tooltip.yrange)
            ]
            unhovered [
                Hide("bag_tooltip"),
            ]

# hovering tooltip for each item when hovered
screen bag_tooltip(bagConfig, item, xrange, yrange):
    if item:
        default mousePos = getMousePosition()
        # Description box
        vbox:
            xminimum xrange.min
            xmaximum xrange.max
            xoffset mousePos.x+20
            yoffset mousePos.y+40
            frame:
                background Solid(bagConfig.tooltipColour.background)
                has vbox
                text "{b}Name: {/b}" + "{0}".format(item.name)
                frame:
                    xminimum xrange.min
                    xmaximum yrange.max
                    if item.used:
                        background Solid(bagConfig.tooltipColour.item_used)
                    else:
                        background Solid(bagConfig.tooltipColour.item_not_used)
                    vbox:
                        text "{b}Brief: {/b}" + "{0}".format(item.desc)
                        text "{b}Stats: {/b}"
                        for stat, value in item.stat.iteritems():
                            if value > 0:
                                text "+{0} {1}".format(value, stat)
                            else:
                                text "{0} {1}".format(value, stat)