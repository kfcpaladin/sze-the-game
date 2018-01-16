###########################################################################
screen statsscreen(who=sze):
    # Include the navigation.
    add "Quests.jpg"
    use diary_nav
    use diary_title("Statistics")
    # display info
    use attribute_info(who)
    use attribute_info_description
    use friend_info
    use friend_info_description

# Show bar graph of all attributes
screen attribute_info(who):
    vbox:
        style "attribute_info"
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
                    style "attribute_info_vpgrid"
                    for attribute in who.attributes:
                        use attribute_info_entry(attribute, who)
                vbar value YScrollValue(_vpgrid_name)

# show attribute information entry
screen attribute_info_entry(attribute, who):
    default attributeColour = {
        "negative": "#b30000",
        "neutral": "#e6ac00",
        "positive": "#009933",
    }
    $ attributeValue = getattr(who, attribute)
    frame:
        style "attribute_info_entry"
        if attributeValue > 0:
            background Solid(attributeColour["positive"])
        elif attributeValue == 0:
            background Solid(attributeColour["neutral"])
        else:
            background Solid(attributeColour["negative"])
        vbox:
            text "{b}" + " {0} ({1})".format(unicode.title(attribute), attributeValue) + "{/b}"
            use bar_graph_widget(attributeValue)
            textbutton "Show description":
                action [
                    Show("attribute_info_description", None, attribute, who)
                ]

# show attribute descrition
screen attribute_info_description(attribute=None, who=None):
    vbox:
        style "attribute_info_description"
        frame:
            xsize 625
            ymaximum 100
            has vbox
            if attribute != None and who != None:
                $ attributeValue = getattr(who, attribute)
                $ briefMsg = ""
                if attributeValue >= 0:
                    $ briefMsg = who.getTutorialMessage(attribute, "msgGain")
                else:
                    $ briefMsg = who.getTutorialMessage(attribute, "msgLoss")
                text "{b}Brief{/b}"
                text briefMsg
                text "{b}Description{/b}"
                text who.getStatMessage(attribute)
            else:
                text "{b}Select an attribute{/b}"
# Show friendship with everyone
screen friend_info:
    vbox:
        style "friend_info"
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
                    style "friend_info_vpgrid"
                    for friend in friendList:
                        use friend_info_entry(friend)
                vbar value YScrollValue(_vpgrid_name)

# Show friend info
screen friend_info_entry(friend):
    default friendColour = {
        "negative": "#b30000",
        "neutral": "#e6ac00",
        "positive": "#009933",
    }
    default iconSize = 100
    frame:
        style "friend_info_entry"
        if friend.friendship > 0:
            background Solid(friendColour["positive"])
        elif friend.friendship == 0:
            background Solid(friendColour["neutral"])
        else:
            background Solid(friendColour["negative"])
        hbox:
            xsize 600
            # imagebutton:
            #     idle Frame(friend.image)
            #     xmaximum iconSize
            #     ymaximum iconSize
            vbox:
                text "{b}" + " {0} ({1})".format(unicode.title(friend.name), friend.friendship) + "{/b}"
                use bar_graph_widget(friend.friendship)
                textbutton "Show description":
                    action [
                        Show("friend_info_description", friend=friend),
                    ]

# Show description for friend
screen friend_info_description(friend=None):
    vbox:
        style "friend_info_description"
        frame:
            xsize 625
            ymaximum 100
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
    default barColour = {
        "negative": "#b30000",
        "neutral": "#e6ac00",
        "positive": "#009933",
    }
    bar:
        value (value+100) 
        range 200 
        xalign 0.5 
        yoffset -7
        xmaximum 600
        hovered [
            Show("bar_graph_tooltip", value),
        ]


screen bar_graph_tooltip(value):
    $ mousePosition = getMousePosition()
    frame:
        xoffset mousePosition[0]
        yoffset mousePosition[1]
        vbox:
            text str(value)

###########################################################################
style attribute_info:
    xoffset 40
    xsize 625
    yoffset 95

style attribute_info_vpgrid:
    xsize 600
    ymaximum 415

style attribute_info_description:
    xsize 625
    ysize 20
    xoffset 40
    yoffset 565

style attribute_info_entry:
    xsize 600
    ymaximum 50

style friend_info:
    xoffset 720
    xsize 625
    yoffset 95

style friend_info_description:
    xsize 625
    ysize 20
    xoffset 720
    yoffset 565

style friend_info_vpgrid:
    xsize 625
    ymaximum 415

style friend_info_entry:
    xsize 600
    ymaximum 50