# Achievement screen entry point and config
screen achieve_screen(controller, rect, theme):
    $ select_rect = rect.resize_from_top_left(height=40).add_offset(Vector2D(0, -50))
    $ info_rect = rect.resize_from_top_left(height=415)
    $ description_rect = rect.resize_from_bottom_left(height=100).add_offset(-Vector2D(0, 100))

    use achieve_select(controller, select_rect, theme)
    use achieve_info(controller, info_rect, theme)
    use achieve_description(controller, description_rect, theme)

# Achievement select
screen achieve_select(controller, rect, theme):
    hbox:
        xoffset rect.left
        yoffset rect.top
        frame:
            xsize rect.width
            ysize rect.height 
            has hbox 
            textbutton unicode.title("Hidden")    action [Function(controller.select_hidden)]
            textbutton unicode.title("Pending")   action [Function(controller.select_pending)]
            textbutton unicode.title("Completed") action [Function(controller.select_completed)]


# Achievement info
screen achieve_info(controller, rect, theme):
    vbox:
        xoffset rect.left
        yoffset rect.top
        xsize rect.width
        frame:      
            has vbox    
            text "{b}" + "{0} Achievements".format(controller.current_filter_name.title()) + "{/b}"
            if controller.achievements and len(controller.achievements) > 0:
                # Grid and scroll bar
                side "c r":
                    $ _vpgrid_name = "achievement_vpgrid"
                    vpgrid id (_vpgrid_name):
                        cols 1
                        spacing 10
                        draggable True
                        mousewheel True
                        xsize rect.width-25 
                        ysize rect.height 
                        # Show each quest in the dictionary
                        for achievement in controller.achievements:
                            use achieve_entry(controller, achievement, rect, theme)
                    vbar value YScrollValue(_vpgrid_name)
            else:
                text "No achievements"

# Achievement entry
screen achieve_entry(controller, achievement, rect, theme):
    default iconSize = 105
    frame:
        style "achieve_entry"
        xsize rect.width 
        background Solid(controller.get_achievement_colour(achievement, theme))
        hbox:
            ysize iconSize
            spacing 5
            use icon_frame(achievement.icon, iconSize, iconSize, loadImage("achievement_default.png"))
            vbox:
                ysize iconSize
                # acheivement info
                text "{b}" + "Achievement: {0}".format(achievement.id) + "{/b}"
                text "{{b}}Title: {{/b}}{0}".format(achievement.title)
                text "{{b}}Brief: {{/b}}{0}".format(achievement.brief)
                # buttons
                hbox:
                    spacing 5
                    textbutton "Show description":
                        action [Function(controller.select_achievement, achievement=achievement)]

# Longer description of achievement
screen achieve_description(controller, rect, theme):
    vbox:
        xoffset rect.left
        yoffset rect.top 
        frame:          
            xsize rect.width
            ymaximum rect.height
            has vbox    
            $ achievement = controller.achievement
            if achievement:
                text "{{b}}Description: {{/b}}{0}".format(achievement.description)
            else:
                text "{b}An achievement has not been selected{/b}"