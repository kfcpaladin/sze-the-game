# make a quest list
screen quest_screen(quests, customConfig={}):
    default questConfig = AttrDict({
        "quests": quests,
        "colour": AttrDict({
            "unavailable":  colour.red,
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
        "questType": quests.currentQuestType,
        "currentDescription": None,
    }).combine(customConfig)

    use quest_select(questConfig, questConfig.selectBox.pos, questConfig.selectBox.size)
    use quest_info(questConfig, questConfig.infoBox.pos, questConfig.infoBox.size)
    use quest_description(questConfig, questConfig.descriptionBox.pos, questConfig.descriptionBox.size)

screen quest_select(questConfig, pos, size):
    hbox:
        xoffset pos.x
        yoffset pos.y
        frame:
            xsize size.x
            ysize size.y
            has hbox
            for questType in quests.displayableQuestTypes:
                textbutton unicode.title(questType):
                    action [
                        Function(questConfig.update, questType=questType, currentDescription=None),
                    ]

# Quest info
screen quest_info(questConfig, pos, size):
    # values that are expected to change must be kept track of
    $ questType = questConfig.questType
    $ currentQuests = getattr(questConfig.quests, questType)
    $ colour = questConfig.colour[questType]
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
                            use quest_entry(questConfig, questID, quest, colour, size.x-25)
                    vbar value YScrollValue(_vpgrid_name)
            else:
                text "No quests are currently {0}".format(questType)

# Quest entry
screen quest_entry(questConfig, questID, quest, colour, width):
    default iconSize = 105
    frame:
        style "quest_entry"
        xsize width
        background Solid(colour)
        hbox:
            ysize iconSize
            spacing 5
            use icon_frame(quest["icon"], iconSize, iconSize, loadImage("quest_default.png"))
            vbox:
                ysize iconSize
                # quest info
                text "{b}" + "Quest: {0}".format(questID) + "{/b}"
                for option in questConfig.infoBox.labels:
                    text "{b}"+"{0}: ".format(unicode.title(option))+"{/b}"+"{0}".format(quest[option])
                # interactive buttons
                hbox:
                    spacing 5
                    # only show start if in available
                    if questID in quests.available:
                        textbutton "Start quest":
                            action [
                                Function(quests.startQuest, questID),
                            ]
                    textbutton "Show description":
                        action [
                            Function(questConfig.update, currentDescription=quest)
                        ]
                    

# Longer description
screen quest_description(questConfig, pos, size):
    $ quest = questConfig.currentDescription
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
                for option in questConfig.descriptionBox.labels:
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
