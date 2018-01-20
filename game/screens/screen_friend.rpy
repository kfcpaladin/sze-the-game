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

##############################################################################
style friend_info_entry:
    ymaximum 50