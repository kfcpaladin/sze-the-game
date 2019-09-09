# Attribute screen 
screen attribute_screen(controller, rect, theme):
    $ info_rect = rect.resize_from_top_left(height=415)
    $ description_rect = rect.resize_from_bottom_left(height=100).add_offset(Vector2D(0, -100))

    use attribute_info(controller, info_rect, theme)
    use attribute_info_description(controller, description_rect, theme)


# Show bar graph of all attributes
screen attribute_info(controller, rect, theme):
    vbox:
        xoffset rect.left 
        yoffset rect.top 
        xsize rect.width
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
                    xsize rect.width-25 
                    ysize rect.height
                    for attribute in controller:
                        use attribute_info_entry(controller, attribute, rect, theme)
                vbar value YScrollValue(_vpgrid_name)

# show attribute information entry
screen attribute_info_entry(controller, attribute, rect, theme):
    default iconSize = 80
    frame:
        style "attribute_info_entry"
        xsize rect.width-25 
        background Solid(controller.get_attribute_colour(attribute, theme))
        hbox:
            xsize rect.width-25
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
screen attribute_info_description(controller, rect, theme):
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
                text attribute.brief
                text "{b}Description{/b}"
                text attribute.message
            else:
                text "{b}Select an attribute{/b}"


###########################################################################
style attribute_info_entry:
    ymaximum 50

