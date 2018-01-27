# expects a list of dictionaries for popupList
# messages = [
#     {
#         "text": "...",
#         "icon": ...,
#         "time_remain": ...,
#     }, etc
# ]
screen popup(popups, pos=Vector(0, 50), size=Vector(400, 50), speed=0.1):
    timer speed:
        repeat True
        action If(
            popups.getTotal() > 0, 
            true = Function(popups.update, speed),
            false = Hide('popup', dissolve),
        )
    vpgrid:
        # define dynamic properties
        cols 1
        spacing 5
        xalign 0.5
        xsize size.x+25
        yoffset pos.y
        ymaximum 600
        # go through all popups
        for popup in reversed(popups.popupList):
            # get transparency number
            $ time_remain = popup["time_remain"]
            $ transparency = int(255*time_remain)
            if transparency > 255:
                $ transparency = 255
            elif transparency < 0:
                $ transparency = 0
            # determine if a normal of icon popup should be used
            if popup["icon"]:
                use popup_icon(popup, transparency, pos, size)
            else:
                use popup_message(popup, transparency, pos, size)

# popup message with associated icon
screen popup_icon(popup, transparency, pos, size):
    default borderSize = 5
    # start the box outline
    frame:
        xalign 0.5
        xsize size.x
        background Solid(colour.white.applyAlpha(transparency))
        # draw box background
        frame:
            style "popup_icon" # use for tight icon wrap
            xalign 0.5
            yalign 0.5
            xsize size.x
            ysize size.y
            if popup["colour"]:
                background Solid(popup["colour"].applyAlpha(transparency))
            else:
                background Solid(colour.maroon.applyAlpha(transparency))
            hbox:
                xsize size.x
                ysize size.y
                # end bxo rendering
                use popup_icon_frame(popup["icon"], size.y, size.y, transparency, loadImage("icon_default.png"))
                vbox:
                    xsize size.x-size.y-borderSize
                    ysize size.y
                    text "{{b}}{}{{b}}".format(popup["text"]):
                        xalign 0.5
                        yalign 0.5
                        text_align 0.5
            

# standard popup message
screen popup_message(popup, transparency, pos, size):
    default borderSize = 5
    # start the box outline
    frame:
        xalign 0.5
        xsize size.x
        background Solid(colour.white.applyAlpha(transparency))
        # draw box background
        frame:
            xalign 0.5
            yalign 0.5
            xsize size.x-borderSize
            ysize size.y-borderSize
            if popup["colour"]:
                background Solid(popup["colour"].applyAlpha(transparency))
            else:
                background Solid(colour.maroon.applyAlpha(transparency))
            # end bxo rendering
            vbox:
                xsize size.x-borderSize
                ysize size.y-borderSize
                text "{{b}}{}{{b}}".format(popup["text"]):
                    xalign 0.5
                    yalign 0.5
                    text_align 0.5

# icon frame with transparency parameter
screen popup_icon_frame(icon, width, height, transparency, default=loadImage("default.png")):
    imagebutton:
        xsize width
        ysize width
        if icon:
            idle Frame(icon)
        else:
            idle Frame(default)
        background Solid(colour.white.applyAlpha(transparency))

# tight wrap style
style popup_icon:
    ymaximum 200