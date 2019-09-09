# Show friendship with everyone
screen friend_screen(controller, friends, rect, theme):
    $ info_rect = rect.resize_from_top_left(height=415)
    $ description_rect = rect.resize_from_bottom_left(height=100).add_offset(Vector2D(0, -100))

    # display screens
    use friend_info(controller, friends, info_rect, theme)
    use friend_description(controller, description_rect, theme)

screen friend_info(controller, friends, rect, theme):
    vbox:
        xoffset rect.left
        yoffset rect.top
        xsize rect.width
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
                    xsize rect.width-25
                    ysize rect.height
                    for friend in friends:
                        use friend_entry(controller, friend, rect, theme)
                vbar value YScrollValue(_vpgrid_name)

# Show friend info
screen friend_entry(controller, friend, rect, theme):
    default iconSize = 80
    frame:
        style "friend_info_entry"
        xsize rect.width-25
        background Solid(controller.get_friend_colour(friend, theme))
        hbox:
            xsize rect.width
            ysize iconSize
            spacing 5
            use icon_frame(friend.icon, iconSize, iconSize, loadImage("icon_default.png"))
            vbox:
                text "{b}" + " {0} ({1})".format(unicode.title(friend.name), friend.friendship) + "{/b}"
                use bar_graph_widget(friend.friendship)
                textbutton "Show description" action [Function(controller.select_friend, friend)]

# Show description for friend
screen friend_description(controller, rect, theme):
    $ friend = controller.friend
    vbox:
        xoffset rect.left
        yoffset rect.top
        frame:
            xsize rect.width
            ymaximum rect.height
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