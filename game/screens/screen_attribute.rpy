# Attribute screen 
screen attribute_screen(who, customConfig={}):
    default attributeConfig = AttrDict({
        "who": who,
        "colour": AttrDict({
            "negative": colour.red,
            "neutral": colour.yellow,
            "positive": colour.green,
        }),
        "infoBox": AttrDict({
            "pos": Vector(40, 95),
            "size": Vector(625, 415),
        }),
        "descriptionBox": AttrDict({
            "pos": Vector(40, 95+470),
            "size": Vector(625, 100),
        }),
        "currentAttribute": None,
    }).combine(customConfig)
    use attribute_info(attributeConfig, attributeConfig.infoBox.pos, attributeConfig.infoBox.size)
    use attribute_info_description(attributeConfig.who, attributeConfig.currentAttribute, attributeConfig.descriptionBox.pos, attributeConfig.descriptionBox.size)


# Show bar graph of all attributes
screen attribute_info(attributeConfig, pos, size):
    vbox:
        xoffset pos.x
        yoffset pos.y
        xsize size.x
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
                    xsize size.x-25
                    ysize size.y
                    for attribute in attributeConfig.who.attributes:
                        use attribute_info_entry(attributeConfig, attribute, size.x-25)
                vbar value YScrollValue(_vpgrid_name)

# show attribute information entry
screen attribute_info_entry(attributeConfig, attribute, width):
    default iconSize = 80
    frame:
        style "attribute_info_entry"
        xsize width
        if attribute.value > 0:
            background Solid(attributeConfig.colour["positive"])
        elif attribute.value == 0:
            background Solid(attributeConfig.colour["neutral"])
        else:
            background Solid(attributeConfig.colour["negative"])
        hbox:
            xsize width
            ysize iconSize
            spacing 5
            use icon_frame(loadImage("icon_{0}.png".format(attribute.name)), iconSize, iconSize, loadImage("icon_default.png"))
            vbox:
                text "{b}" + " {0} ({1})".format(unicode.title(attribute.name), attribute.value) + "{/b}"
                use bar_graph_widget(attribute.value)
                textbutton "Show description":
                    action [
                        Function(attributeConfig.update, currentAttribute=attribute.name)
                    ]

# show attribute descrition
screen attribute_info_description(who, attribute, pos, size):
    vbox:
        xoffset pos.x
        yoffset pos.y
        frame:
            xsize size.x
            ymaximum 100
            has vbox
            if attribute != None:
                text "{b}Brief{/b}"
                # text who.getTutorialMessage(attribute)
                text "{b}Description{/b}"
                # text who.getStatMessage(attribute)
            else:
                text "{b}Select an attribute{/b}"


###########################################################################
style attribute_info_entry:
    ymaximum 50

