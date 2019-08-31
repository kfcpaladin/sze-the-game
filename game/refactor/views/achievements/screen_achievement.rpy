# Achievement screen entry point and config
screen achieve_screen(controller):
    use achieve_select(controller)
    use achieve_info(controller)
    use achieve_description(controller)

# Achievement select
screen achieve_select(controller):
    hbox:
        xoffset 720 
        yoffset 45
        frame:
            xsize 625
            ysize 40
            has hbox
            textbutton unicode.title("Hidden")    action [Function(controller.select_hidden)]
            textbutton unicode.title("Pending")   action [Function(controller.select_pending)]
            textbutton unicode.title("Completed") action [Function(controller.select_completed)]


# Achievement info
screen achieve_info(controller):
    vbox:
        xoffset 720 
        yoffset 95 
        xsize 625 
        frame:      
            has vbox    
            text "{b}" + "? Achievements" + "{/b}"
            if controller.achievements and len(controller.achievements) > 0:
                # Grid and scroll bar
                side "c r":
                    $ _vpgrid_name = "achievement_vpgrid"
                    vpgrid id (_vpgrid_name):
                        cols 1
                        spacing 10
                        draggable True
                        mousewheel True
                        xsize 600 
                        ysize 415 
                        # Show each quest in the dictionary
                        for achievement in controller.achievements:
                            use achieve_entry(controller, achievement)
                    vbar value YScrollValue(_vpgrid_name)
            else:
                text "No achievements"

# Achievement entry
screen achieve_entry(controller, achievement):
    default iconSize = 105
    frame:
        style "achieve_entry"
        xsize 600 
        if achievement.is_complete:
            background Solid(colour.green)
        elif not achievement.is_hidden:
            background Solid(colour.yellow)
        else:
            background Solid(colour.red)

        hbox:
            spacing 5
            ysize iconSize
            use icon_frame(achievement.icon, iconSize, iconSize, loadImage("achievement_default.png"))
            vbox:
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
screen achieve_description(controller):
    vbox:
        xoffset 720 
        yoffset (95+470)
        frame:          
            xsize 625
            ymaximum 100
            has vbox    
            $ achievement = controller.achievement
            if achievement:
                text "{{b}}Description: {{/b}}{0}".format(achievement.description)
            else:
                text "{b}An achievement has not been selected{/b}"


##############################################
style achieve_entry:  
    ysize 40
