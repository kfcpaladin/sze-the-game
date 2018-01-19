##############################################
screen questscreen(quests=quests):
    modal True
    add loadImage("screen_bg_diaryNormal.png")
    use diary_nav
    use diary_title("Quests")
    # Create hbox to select quest type to display
    default currentQuestType = quests.currentQuestType
    hbox:
        style "quest_select"
        frame:
            has hbox
            for questType in quests.displayableQuestTypes:
                textbutton unicode.title(questType):
                    action [
                        SetScreenVariable("currentQuestType", questType),   
                        Hide("quest_description")
                    ]
    # Show panels
    use attribute_info(sze)
    use quest_info(currentQuestType, quests)
    

# Quest info
screen quest_info(questType, quests, pos=Vector(720, 95), size=Vector(625, 415)):
    default questColour = {
        "unavailable":  colour.red,
        "available":    colour.yellow,
        "completed":    colour.red,
    }
    # values that are expected to change must be kept track of
    $ currentQuests = getattr(quests, questType)
    $ colour = questColour[questType]
    # default description
    use quest_description(pos=Vector(pos.x, pos.y+470), size=Vector(size.x, 100))
    vbox:
        xoffset pos.x 
        yoffset pos.y
        xsize size.x
        frame:         
            has vbox    
            text "{b}" + "{0} quests".format(unicode.title(questType)) + "{/b}"
            if currentQuests:
                # Grid and scroll bar
                side "c r":
                    $ _vpgrid_name = "quest_vpgrid"
                    vpgrid id (_vpgrid_name):
                        cols 1
                        spacing 10
                        draggable True
                        mousewheel True
                        xsize size.x-25
                        ysize size.y
                        # Show each quest in the dictionary
                        for questID, quest in currentQuests.iteritems():
                            use quest_entry(questID, quest, quests, colour, pos, size)
                    vbar value YScrollValue(_vpgrid_name)
            else:
                text "No quests are currently {0}".format(questType)

# Quest entry
screen quest_entry(questID, quest, quests, colour, pos, size):
    default questInfo = ["title", "brief"]
    default iconSize = 105
    frame:
        style "quest_entry"
        xsize size.x-25
        background Solid(colour)
        hbox:
            ysize iconSize
            spacing 5
            use icon_frame(quest["icon"], iconSize, iconSize, loadImage("quest_default.png"))
            vbox:
                ysize iconSize
                # quest info
                text "{b}" + "Quest: {0}".format(questID) + "{/b}"
                for option in questInfo:
                    $ msg = "{b}" + "{0}: ".format(unicode.title(option)) + "{/b}"
                    if not quest[option]:
                        $ msg += "None"
                    else:
                        $ msg += quest[option] 
                    text msg
                # interactive buttons
                hbox:
                    spacing 5
                    textbutton "Start quest":
                        action [
                            Function(quests.startQuest, questID),
                        ]
                    textbutton "Show description":
                        action [
                            Show("quest_description", None, quest, pos=Vector(pos.x, pos.y+470), size=Vector(size.x, 100))
                        ]
                    

# Longer description
screen quest_description(quest=None, pos, size):
    default questInfo = ["description", "dependencies"]
    vbox:
        xoffset pos.x
        yoffset pos.y
        xsize size.x
        ysize size.y
        frame:          # The frame window is used for dialogue, which has a maroon color
            xsize 625
            ymaximum 200
            has vbox    # Give it the size of the vbox
            if quest:
                for option in questInfo:
                    text "{b}" + "{0}".format(unicode.title(option)) + "{/b}"
                    if quest[option]:
                        text listToText(quest[option])
                    else:
                        text "None"
            else:
                text "{b}A quest has not been selected{/b}"


##############################################
style quest_entry:  
    ysize 70
    
style quest_select:
    xmaximum 625
    xoffset 700
    ysize 20
    yoffset 45
