screen achievementscreen(achievements=achievements):
    modal True
    add loadImage("screen_bg_diaryNormal.png")
    use diary_nav
    use diary_title("Achievements")
    # Create hbox to select achivement type to display
    default currentAchieveType = achievements.currentAchieveType
    hbox:
        style "achieve_select"
        frame:
            has hbox
            for achieveType in achievements.displayableAchieveTypes:
                textbutton unicode.title(achieveType):
                    action [
                        SetScreenVariable("currentAchieveType", achieveType),
                        Hide("achieve_description"),
                    ]
    use attribute_info(sze)
    use achieve_info(currentAchieveType, achievements)

# Achievement info
screen achieve_info(achieveType, achievements, pos=Vector(720, 95), size=Vector(625, 415)):
    default achieveColour = {
        "hidden":       colour.red,
        "available":    colour.yellow,
        "completed":    colour.green,
    }
    # changes dynamically
    $ currentAchievements = getattr(achievements, achieveType)
    $ colour = achieveColour[achieveType]
    # default description box
    use achieve_description(pos=Vector(pos.x, pos.y+470), size=Vector(size.x, 100))
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
                        for achieveID, achievement in currentAchievements.iteritems():
                            use achieve_entry(achieveID, achievement, colour, pos, size)
                    vbar value YScrollValue(_vpgrid_name)
            else:
                text "No achievements are currently {0}".format(achieveType)

# Achievement entry
screen achieve_entry(achieveID, achievement, colour, pos, size):
    default achieveInfo = ["title", "brief"]
    default iconSize = 105
    frame:
        style "achieve_entry"
        xsize size.x-25
        background Solid(colour)
        hbox:
            spacing 5
            ysize iconSize
            use icon_frame(achievement["icon"], iconSize, iconSize, loadImage("achievement_default.png"))
            vbox:
                # acheivement info
                text "{b}" + "Achievement: {0}".format(achieveID) + "{/b}"
                for option in achieveInfo:
                    $ msg = "{b}" + "{0}: ".format(unicode.title(option)) + "{/b}"
                    if not achievement[option]:
                        $ msg += "None"
                    else:
                        $ msg += achievement[option] 
                    text msg
                # buttons
                hbox:
                    spacing 5
                    textbutton "Show description":
                        action [
                            Hide("achieve_description"),    # prevent old screen from covering new one
                            Show("achieve_description", achievement=achievement, pos=Vector(pos.x, pos.y+470), size=Vector(size.x, 100))
                        ]

# Longer description of achievement
screen achieve_description(achievement=None, pos, size):
    default achieveInfo = ["description", "dependencies"]
    vbox:
        xoffset pos.x
        yoffset pos.y
        frame:          
            xsize size.x
            ymaximum size.y
            has vbox    
            if achievement:
                for option in achieveInfo:
                    text "{b}" + "{0}".format(unicode.title(option)) + "{/b}"
                    if not achievement[option]:
                        text "None"
                    else:
                        text achievement[option]           
            else:
                text "{b}An achievement has not been selected{/b}"


##############################################
style achieve_entry:  
    ysize 40

style achieve_select:
    xmaximum 625
    xoffset 700
    ysize 20
    yoffset 45
