# Attribute screen 
screen attribute_screen(controller, rect):
    $ info_rect = rect.resize_from_top_left(height=415)
    $ description_rect = rect.resize_from_bottom_left(height=100).add_offset(Vector2D(0, -100))

    use attribute_info(controller, info_rect)
    use attribute_info_description(controller, description_rect)


# Show bar graph of all attributes
screen attribute_info(controller, info_rect):
    vbox:
        xoffset info_rect.left 
        yoffset info_rect.top 
        xsize info_rect.width
        frame:
            has vbox
            text "{b}Attribute Status{/b}"
            side "c r":
                $ _vpgrid_name = "attribute_info_grid"
                vpgrid id(_vpgrid_name):
                    cols 1
                    draggable True
                    mousewheel True
                    spacing 10
                    xsize info_rect.width-25 
                    ysize info_rect.height
                    for attribute in controller:
                        use attribute_info_entry(controller, attribute, info_rect)
                vbar value YScrollValue(_vpgrid_name)

# show attribute information entry
screen attribute_info_entry(controller, attribute, info_rect):
    default iconSize = 80
    frame:
        style "attribute_info_entry"
        xsize info_rect.width-25 
        if attribute.value > 0:
            background Solid(colour.green)
        elif attribute.value == 0:
            background Solid(colour.yellow)
        else:
            background Solid(colour.red)
        hbox:
            xsize info_rect.width-25
            ysize iconSize
            spacing 5
            use icon_frame(loadImage("icon_{0}.png".format(attribute.name)), iconSize, iconSize, loadImage("icon_default.png"))
            vbox:
                text "{b}" + " {0} ({1})".format(attribute.name.title(), attribute.value) + "{/b}"
                use bar_graph_widget(attribute.value)
                textbutton "Show description":
                    action [
                        Function(controller.set_attribute, attribute)
                    ]

# show attribute descrition
screen attribute_info_description(controller, rect):
    vbox:
        xoffset rect.left 
        yoffset rect.top 
        frame:
            xsize rect.width
            ymaximum rect.height
            has vbox
            $ attribute = controller.attribute_message
            if attribute != None:
                text "{b}Brief{/b}"
                # text who.getTutorialMessage(attribute)
                text "{b}Description{/b}"
                text attribute.message
            else:
                text "{b}Select an attribute{/b}"


###########################################################################
style attribute_info_entry:
    ymaximum 50

