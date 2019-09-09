##########################
# shows choices user has made
screen roadmap_screen:
    text "{color=#f00}{b}WIP roadmap of all possible choices and paths{/b}{/color}"
    vbox:
        xoffset 16
        yoffset 92
        side "c b r":
            area (0, 0, 1340, 660)

            viewport id "vp":
                draggable True
                imagemap:
                    ground loadImage("roadmap.png")
                    #hover  loadImage("screen_bg_map_selected.png")
                    #idle   loadImage("screen_bg_map_unavailable.png")

            bar value XScrollValue("vp")
            vbar value YScrollValue("vp")
    