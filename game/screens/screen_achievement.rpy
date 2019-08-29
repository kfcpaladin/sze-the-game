# Achievement screen entry point and config
screen achieve_screen(achievements, customConfig={}):
    default achieveConfig = AttrDict({
        "achievements": achievements, 
        "achieveColour": AttrDict({
            "hidden":       colour.red,
            "available":    colour.yellow,
            "completed":    colour.green,
        }),
        "selectBox": AttrDict({
            "pos": Vector(720, 45),
            "size": Vector(625, 40),
        }),
        "infoBox": AttrDict({
            "pos": Vector(720, 95),
            "size": Vector(625, 415),
            "labels": ("title", "brief"),
        }),
        "descriptionBox": AttrDict({
            "pos": Vector(720, 95+470),
            "size": Vector(625, 100),
            "labels": ("description", "dependencies"),
        }),
        "achieveType": "available",
        "currentDescription": None,
    }).combine(customConfig)
    use achieve_select(achieveConfig, achieveConfig.selectBox.pos, achieveConfig.selectBox.size)
    use achieve_info(achieveConfig, achieveConfig.infoBox.pos, achieveConfig.infoBox.size)
    use achieve_description(achieveConfig, achieveConfig.descriptionBox.pos, achieveConfig.descriptionBox.size)

# Achievement select
screen achieve_select(achieveConfig, pos, size):
    hbox:
        xoffset pos.x
        yoffset pos.y
        frame:
            xsize size.x
            ysize size.y
            has hbox
            for achieveType in ("hidden", "available", "completed"):
                textbutton unicode.title(achieveType):
                    action [
                        Function(achieveConfig.update, achieveType=achieveType, currentDescription=None),
                    ]


# Achievement info
screen achieve_info(achieveConfig, pos, size):
    # changes dynamically
    $ achieveType = achieveConfig.achieveType
    $ currentAchievements = achieveConfig.achievements.achievements 
    $ colour = achieveConfig.achieveColour[achieveType]
    vbox:
        xoffset pos.x
        yoffset pos.y
        xsize size.x
        frame:      
            has vbox    
            text "{b}" + "{0} achievements".format(unicode.title(achieveType)) + "{/b}"
            if currentAchievements:
                # Grid and scroll bar
                side "c r":
                    $ _vpgrid_name = "achievement_vpgrid"
                    vpgrid id (_vpgrid_name):
                        cols 1
                        spacing 10
                        draggable True
                        mousewheel True
                        xsize size.x-25
                        ysize size.y
                        # Show each quest in the dictionary
                        for achievement in currentAchievements:
                            use achieve_entry(achieveConfig, achievement, colour, size.x)
                    vbar value YScrollValue(_vpgrid_name)
            else:
                text "No achievements are currently {0}".format(achieveType)

# Achievement entry
screen achieve_entry(achieveConfig, achievement, colour, width):
    default iconSize = 105
    frame:
        style "achieve_entry"
        xsize width-25
        background Solid(colour)
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
                        action [
                            Function(achieveConfig.update, currentDescription=achievement)
                        ]

# Longer description of achievement
screen achieve_description(achieveConfig, pos, size):
    $ achievement = achieveConfig.currentDescription
    vbox:
        xoffset pos.x
        yoffset pos.y
        frame:          
            xsize size.x
            ymaximum size.y
            has vbox    
            if achievement:
                text "{{b}}Description: {{/b}}{0}".format(achievement.description)
                text "{{b}}Dependencies: {{/b}}{0}".format(len(achievement.unlock_dependencies.dependencies))
            else:
                text "{b}An achievement has not been selected{/b}"


##############################################
style achieve_entry:  
    ysize 40
