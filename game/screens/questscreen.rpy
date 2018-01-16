##############################################
screen questscreen(quests=quests):
    add screenBackgroundDir + "diaryNormal.jpg"
    use diary_nav
    use diary_title("Quests")
    # Used to keep track of the quest types, and which one to show
    default currentQuestType = quests.currentQuestType

    # Create hbox to select quest type to display
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
    # right panel for info
    use quest_info(currentQuestType, quests)
    use quest_description

# Quest info
screen quest_info(questType, quests):
    default questColour = {
        "unavailable":  "#b30000",
        "available":    "#e6ac00",
        "completed":    "#009933"
    }
    $ currentQuests = getattr(quests, questType)
    $ colour = questColour[questType]
    vbox:
        style "quest_info"
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
                        style "quest_vpgrid"
                        # Show each quest in the dictionary
                        for questID, quest in currentQuests.iteritems():
                            use quest_entry(questID, quest, quests, colour)
                    vbar value YScrollValue(_vpgrid_name)
            else:
                text "No quests are currently {0}".format(questType)

# Quest entry
screen quest_entry(questID, quest, quests, colour):
    default questInfo = ["title", "brief"]
    frame:
        style "quest_entry"
        background Solid(colour)
        vbox:
            text "{b}" + "Quest: {0}".format(questID) + "{/b}"
            for option in questInfo:
                $ msg = "{b}" + "{0}: ".format(unicode.title(option)) + "{/b}"
                if not quest[option]:
                    $ msg += "None"
                else:
                    $ msg += quest[option] 
                text msg
            textbutton "Show description":
                action [
                    Show("quest_description", quest=quest)
                ]
            textbutton "Start quest":
                action [
                    Function(quests.startQuest, questID),
                    Hide("quest_description")
                ]

# Longer description
screen quest_description(quest=None):
    default questInfo = ["description", "dependencies"]
    vbox:
        style "quest_description"
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
style quest_info:  
    xsize 650
    ysize 450
    xoffset 720
    yoffset 95

style quest_vpgrid: 
    xsize 600
    ysize 415

style quest_entry:  
    xsize 650
    ysize 70

style quest_description:  
    xsize 625
    ysize 200
    xoffset 720
    yoffset 565
    
style quest_select:
    xmaximum 625
    xoffset 700
    ysize 20
    yoffset 45
