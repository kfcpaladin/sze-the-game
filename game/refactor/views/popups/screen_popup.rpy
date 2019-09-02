# rect = size of each popup
screen popup(controller, rect=Rect2D(right=400, bottom=50).add_offset(Vector2D(0, 50))):
    $ dt = 1.0/60.0
    timer dt:
        repeat True
        action If(
            controller.total > 0,
            true = Function(controller.update, dt),
            false = Hide('popup', dissolve),
        )
    vpgrid:
        # define dynamic properties
        cols 1
        spacing 5
        xalign 0.5
        xsize rect.width+25
        yoffset rect.top
        ymaximum 600 
        # go through all popups
        for popup in controller.popups:
            if popup.icon:
                use popup_icon(controller, popup, rect)
            else:
                use popup_message(controller, popup, rect)

# popup message with associated icon
screen popup_icon(controller, popup, rect):
    default borderSize = 5
    $ transparency = controller.get_transparency(popup)
    # start the box outline
    frame:
        xalign 0.5
        xsize rect.width 
        background Solid(PrimaryColours.WHITE.replace_opacity(transparency))
        # draw box background
        frame:
            style "popup_icon" # use for tight icon wrap
            xalign 0.5
            yalign 0.5
            xsize rect.width 
            ysize rect.height
            if popup.colour:
                background Solid(popup.colour.replace_opacity(transparency))
            else:
                background Solid(PrimaryColours.MAROON.replace_opacity(transparency))
            hbox:
                xsize rect.width
                ysize rect.height
                # end bxo rendering
                use popup_icon_frame(popup.icon, rect.height, transparency)
                vbox:
                    xsize rect.width-rect.height-borderSize
                    ysize rect.height
                    text "{{b}}{}{{b}}".format(popup.message):
                        xalign 0.5
                        yalign 0.5
                        text_align 0.5
            

# standard popup message
screen popup_message(controller, popup, rect):
    default borderSize = 5
    $ transparency = controller.get_transparency(popup)

    frame:
        xalign 0.5
        xsize rect.width
        background Solid(PrimaryColours.WHITE.replace_opacity(transparency))
        # draw box background
        frame:
            xalign 0.5
            yalign 0.5
            xsize rect.width-borderSize
            ysize rect.height-borderSize
            if popup.colour:
                background Solid(popup.colour.replace_opacity(transparency))
            else:
                background Solid(PrimaryColours.MAROON.replace_opacity(transparency))
            # end bxo rendering
            vbox:
                xsize rect.width-borderSize
                ysize rect.height-borderSize
                text "{{b}}{}{{b}}".format(popup.message):
                    xalign 0.5
                    yalign 0.5
                    text_align 0.5

# icon frame with transparency parameter
screen popup_icon_frame(icon, width, transparency, default=loadImage("icon_default.png")):
    imagebutton:
        xsize width
        ysize width
        if icon:
            idle Frame(icon)
        else:
            idle Frame(default)
        background Solid(PrimaryColours.WHITE.replace_opacity(transparency))

# tight wrap style
style popup_icon:
    ymaximum 200