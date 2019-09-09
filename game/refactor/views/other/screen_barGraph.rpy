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
        background Solid(themes.default.light)
        imagebutton:
            xmaximum width
            ymaximum height
            if icon:
                idle Frame(icon)
            else:
                idle Frame(default)