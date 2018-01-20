# Show friendship with everyone
screen friend_screen(friends, customConfig={}):
    default friendConfig = AttrDict({
        "friends": friends,
        "colour": AttrDict({
            "negative": colour.red,
            "neutral": colour.yellow,
            "positive": colour.green,
        }),
        "infoBox": AttrDict({
            "pos": Vector(720, 95),
            "size": Vector(625, 415),
        }),
        "descriptionBox": AttrDict({
            "pos": Vector(720, 95+470),
            "size": Vector(625, 100),
        }),
        "currentFriend": None,
    }).combine(customConfig)
    # display screens
    use friend_info(friendConfig, friendConfig.infoBox.pos, friendConfig.infoBox.size)
    use friend_description(friendConfig.currentFriend, friendConfig.descriptionBox.pos, friendConfig.descriptionBox.size)

screen friend_info(friendConfig, pos, size):
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
                    for friend in friendConfig.friends:
                        use friend_entry(friendConfig, friend, size.x-25)
                vbar value YScrollValue(_vpgrid_name)

# Show friend info
screen friend_entry(friendConfig, friend, width):
    default iconSize = 80
    frame:
        style "friend_info_entry"
        xsize width
        if friend.friendship > 0:
            background Solid(friendConfig.colour.positive)
        elif friend.friendship == 0:
            background Solid(friendConfig.colour.neutral)
        else:
            background Solid(friendConfig.colour.negative)
        hbox:
            xsize width
            ysize iconSize
            spacing 5
            use icon_frame(friend.icon, iconSize, iconSize, loadImage("icon_default.png"))
            vbox:
                text "{b}" + " {0} ({1})".format(unicode.title(friend.name), friend.friendship) + "{/b}"
                use bar_graph_widget(friend.friendship)
                textbutton "Show description":
                    action [
                        Function(friendConfig.update, currentFriend=friend)
                    ]

# Show description for friend
screen friend_description(friend=None, pos, size):
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