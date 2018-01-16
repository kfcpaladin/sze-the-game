screen achievementscreen(achievements=achievements):
    add screenBackgroundDir + "diaryNormal.jpg"
    use diary_nav
    use diary_title("Achievements")
    default currentAchieveType = achievements.currentAchieveType
    # Create hbox to select achivement type to display
    hbox:
        style "achieve_select"
        frame:
            has hbox
            for achieveType in achievements.displayableAchieveTypes:
                textbutton unicode.title(achieveType):
                    action [
                        SetScreenVariable("currentAchieveType", achieveType),
                        Hide("achieve_description")
                    ]
    # Show achievements
    use achieve_info(currentAchieveType, achievements)
    use achieve_description

# Achievement info
screen achieve_info(achieveType, achievements):
    default achieveColour = {
        "hidden":       "#b30000",
        "available":    "#e6ac00",
        "completed":    "#009933"
    }
    $ currentAchievements = getattr(achievements, achieveType)
    $ colour = achieveColour[achieveType]
    vbox:
        style "achieve_info"
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
                        style "achieve_vpgrid"
                        # Show each quest in the dictionary
                        for achieveID, achievement in currentAchievements.iteritems():
                            use achieve_entry(achieveID, achievement, colour)
                    vbar value YScrollValue(_vpgrid_name)
            else:
                text "No achievements are currently {0}".format(achieveType)

# Achievement entry
screen achieve_entry(achieveID, achievement, colour):
    default achieveInfo = ["title", "brief"]
    frame:
        style "achieve_entry"
        background Solid(colour)
        vbox:
            text "{b}" + "Achievement: {0}".format(achieveID) + "{/b}"
            for option in achieveInfo:
                $ msg = "{b}" + "{0}: ".format(unicode.title(option)) + "{/b}"
                if not achievement[option]:
                    $ msg += "None"
                else:
                    $ msg += achievement[option] 
                text msg
            textbutton "Show description":
                action [
                    Show("achieve_description", achievement=achievement)
                ]

# Longer description of achievement
screen achieve_description(achievement=None):
    default achieveInfo = ["description", "dependencies"]
    vbox:
        style "achieve_description"
        frame:          
            xsize 625
            ymaximum 200
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


style achieve_info:  
    xsize 625
    ysize 450
    xoffset 720
    yoffset 95

style achieve_vpgrid: 
    xsize 600
    ysize 415

style achieve_entry:  
    xsize 600
    ysize 40

style achieve_description:  
    xsize 625
    ysize 200
    xoffset 720
    yoffset 565
    
style achieve_select:
    xmaximum 625
    xoffset 700
    ysize 20
    yoffset 45
