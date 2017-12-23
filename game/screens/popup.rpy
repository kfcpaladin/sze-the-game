style popup_vpgrid:
    xsize 500
    xalign 0.5
    yoffset 100

screen popup(messages=[], icons=[], duration=2, speed=0.5):
    default time_remain = duration
    timer speed:
        repeat True
        action If(time_remain > 0, true=[SetScreenVariable('time_remain', time_remain-speed)], false=[Hide('popup')])
    vpgrid:
        cols 1
        spacing 10
        draggable True
        mousewheel True
        style "popup_vpgrid"
        for message in messages:
            hbox:
                xsize 500
                ysize 40
                xalign 0.5
                frame:
                    xalign 0.5
                    has hbox
                    if not message:
                        $ message = "No message"    
                    text "{b}" + message + "{/b}"
                    