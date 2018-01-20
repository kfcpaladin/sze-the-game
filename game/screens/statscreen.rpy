###########################################################################
screen statsscreen(who=sze):
    # prevent interaction underneath
    modal True
    # Include the navigation.
    add loadImage("screen_bg_diaryNormal.png")
    use diary_nav
    use diary_title("Statistics")
    # display info
    use attribute_info(who)
    use friend_info

# Show bar graph of all attributes
screen attribute_info(who, pos=Vector(40,95), size=Vector(625,415)):
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
                    for attribute in who.attributes:
                        use attribute_info_entry(who, attribute, pos, size)
                vbar value YScrollValue(_vpgrid_name)
    use attribute_info_description(pos=Vector(pos.x, pos.y+470), size=Vector(size.x, 100))

# show attribute information entry
screen attribute_info_entry(who, attribute, pos, size):
    default attributeColour = {
        "negative": colour.red,
        "neutral": colour.yellow,
        "positive": colour.green,
    }
    default iconSize = 80
    $ attributeValue = getattr(who, attribute)
    frame:
        style "attribute_info_entry"
        xsize size.x-25
        if attributeValue > 0:
            background Solid(attributeColour["positive"])
        elif attributeValue == 0:
            background Solid(attributeColour["neutral"])
        else:
            background Solid(attributeColour["negative"])
        hbox:
            xsize size.x-25
            ysize iconSize
            spacing 5
            use icon_frame(loadImage("icon_{0}.png".format(attribute)), iconSize, iconSize, loadImage("icon_default.png"))
            vbox:
                text "{b}" + " {0} ({1})".format(unicode.title(attribute), attributeValue) + "{/b}"
                use bar_graph_widget(attributeValue)
                textbutton "Show description":
                    action [
                        Hide("attribute_info_description"), 
                        Show("attribute_info_description", None, who, attribute, pos=Vector(pos.x, pos.y+470), size=Vector(size.x, 100)),
                    ]

# show attribute descrition
screen attribute_info_description(who=None, attribute=None, pos, size):
    vbox:
        xoffset pos.x
        yoffset pos.y
        frame:
            xsize size.x
            ymaximum 100
            has vbox
            if attribute != None and who != None:
                $ attributeValue = getattr(who, attribute)
                text "{b}Brief{/b}"
                text who.getTutorialMessage(attribute)
                text "{b}Description{/b}"
                text who.getStatMessage(attribute)
            else:
                text "{b}Select an attribute{/b}"

# Show friendship with everyone
screen friend_info(pos=Vector(720, 95), size=Vector(625, 415)):
    vbox:
        xoffset pos.x
        yoffset pos.y
        xsize size.x
        frame:
            has vbox
            text "{b}Friendship Status{/b}"
            side "c r":
                $ _vpgrid_name = "friend_info_grid"
                vpgrid id(_vpgrid_name):
                    cols 1
                    draggable True
                    mousewheel True
                    spacing 10
                    xsize size.x-25
                    ysize size.y
                    for friend in friendList:
                        use friend_info_entry(friend, pos, size)
                vbar value YScrollValue(_vpgrid_name)
    use friend_info_description(pos=Vector(pos.x, pos.y+470), size=Vector(size.x, 100))

# Show friend info
screen friend_info_entry(friend, pos, size):
    default friendColour = {
        "negative": colour.red,
        "neutral": colour.yellow,
        "positive": colour.green,
    }
    default iconSize = 80
    frame:
        style "friend_info_entry"
        xsize size.x-25
        ymaximum 50
        if friend.friendship > 0:
            background Solid(friendColour["positive"])
        elif friend.friendship == 0:
            background Solid(friendColour["neutral"])
        else:
            background Solid(friendColour["negative"])
        hbox:
            xsize size.x-25
            ysize iconSize
            spacing 5
            use icon_frame(friend.icon, iconSize, iconSize, loadImage("icon_default.png"))
            vbox:
                text "{b}" + " {0} ({1})".format(unicode.title(friend.name), friend.friendship) + "{/b}"
                use bar_graph_widget(friend.friendship)
                textbutton "Show description":
                    action [
                        Hide("friend_info_description"),
                        Show("friend_info_description", None, friend=friend, pos=Vector(pos.x, pos.y+470), size=Vector(size.x, 100)),
                    ]

# Show description for friend
screen friend_info_description(friend=None, pos, size):
    vbox:
        xoffset pos.x
        yoffset pos.y
        frame:
            xsize size.x
            ymaximum size.y
            has vbox
            if friend:
                text "{b}Description{/b}"
                if friend.description:
                    text friend.description
                else:
                    text "{0} has no description".format(unicode.title(friend.name))
            else:
                text "{b}Select a friend for description{/b}"


# Show bar graph
screen bar_graph_widget(value):
    bar:
        value (value+100) 
        range 200 
        xalign 0.5 
        yoffset -7
        xmaximum 600
        hovered [
            Show("bar_graph_tooltip", value),
        ]

# NOTE: This is not working
screen bar_graph_tooltip(value):
    $ mousePosition = getMousePosition()
    frame:
        xoffset mousePosition[0]
        yoffset mousePosition[1]
        vbox:
            text str(value)

# Icon frame for mounting icons
screen icon_frame(icon, width, height, default=loadImage("default.png")):
    frame:
        xsize width
        ysize height
        background Solid(colour.white)
        imagebutton:
            xmaximum width
            ymaximum height
            if icon:
                idle Frame(icon)
            else:
                idle Frame(default)

###########################################################################
style attribute_info_entry:
    ymaximum 50

style friend_info_entry:
    ymaximum 50