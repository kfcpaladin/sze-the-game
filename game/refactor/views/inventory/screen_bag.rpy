# display an inventory object 
screen bag_screen(controller, inventory, rect, theme):
    use bag_inventory(controller, inventory, rect, theme)

# display the bag inventory
screen bag_inventory(controller, inventory, rect, theme):
    # render inventory
    $ border_size = 5
    $ item_rect = controller.get_tile_rect(rect, border_size)
    frame:
        background Solid(PrimaryColours.CLEAR)
        xoffset rect.left-border_size
        yoffset rect.top-border_size
        hbox:
            # render inventory grid
            $ _grid_name = "{0}_vpgrid".format(inventory.name)
            vpgrid id (_grid_name):
                xsize rect.width
                ysize rect.height
                spacing border_size
                cols controller.total_columns
                rows controller.total_rows
                draggable False
                mousewheel True
                for item in inventory.items:
                    use bag_item(controller, item, item_rect.width, item_rect.height, theme)
            # if rows exceed columns, assume we need to scroll
            if controller.total_rows > controller.total_columns:
                frame:
                    ysize rect.height
                    vbar:
                        value YScrollValue(_grid_name)
    
# display a bag item
screen bag_item(controller, item, width, height, theme):
    frame:
        xsize width
        ysize height
        background Solid(controller.get_item_colour(item, theme))
        imagebutton:
            xmaximum width
            ymaximum height
            idle  Frame(item.icon, width, height, width, height)
            hover Frame(im.Sepia(item.icon), width, height, width, height)
            action [Function(controller.on_item_click, item)]
            hovered [Show("bag_tooltip", None, controller, item, theme)]
            unhovered [Hide("bag_tooltip")]

# hovering tooltip for each item when hovered
screen bag_tooltip(controller, item, theme, rect=Rect2D(left=300, right=600, top=200, bottom=400)):
    if item:
        default mousePos = getMousePosition()
        # Description box
        vbox:
            xminimum rect.left
            xmaximum rect.right
            xoffset mousePos.x+20
            yoffset mousePos.y+40
            frame:
                background Solid(controller.get_tooltip_background_colour(theme))
                has vbox
                text "{b}Name: {/b}" + "{0}".format(item.name)
                frame:
                    xminimum rect.left
                    xmaximum rect.right
                    background Solid(controller.get_tooltip_colour(item, theme))
                    vbox:
                        text "{b}Brief: {/b}" + "{0}".format(item.description)
                        text "{b}Stats: {/b}"
                        for action in item.actions:
                            text action.description