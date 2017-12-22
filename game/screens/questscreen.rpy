style quest_entry:
    ysize 80
    xsize 650

style quest_panel:
    xsize 650
    yminimum 200
    ymaximum 650

style quest_grid:
    yoffset 40
    xmaximum 1300

screen questscreen(quests=quests):
    tag menu
    use navigation # Include the navigation.
    # Used to keep track of the quest types, and which one to show
    default displays = ["ongoing", "completed"]
    default current_display = displays[0]   
    default current_quests = getattr(quests, current_display)
    # Create hbox to select quest type to display
    hbox:
        frame:
            has hbox
            ymaximum 20
            for display in displays:
                textbutton unicode.title(display):
                    action [SetScreenVariable("current_display", display),              
                            SetScreenVariable("current_quests", getattr(quests, display)),
                            SetScreenVariable("current_quest", None)    # Reset the current quest to show
                           ]
    # Create quest display
    grid 2 1:
        style "quest_grid"
        # Used to determine which quest is displayed in the right panel
        default current_quest = None    
        # Left vertical box for ongoing quests
        vbox:
            style "quest_panel"
            frame:  # The frame window is used for dialogue, which has a maroon color
                has vbox    # Give it the size of the vbox 
                text "{b}" + "{0} quests".format(unicode.title(current_display)) + "{/b}"
                # Grid and scroll bar
                side "c r":
                    # Create a grid of 1 column, and n rows
                    $ _vpgrid_name = "quest_vpgrid"
                    vpgrid id (_vpgrid_name):
                        cols 1
                        spacing 20
                        draggable True
                        mousewheel True
                        for index, quest in enumerate(current_quests):
                            # Create horizontal boxes with style "quest_entry" for each grid box
                            frame:
                                style "quest_entry"
                                background Solid("#F2AB4E")
                                vbox:    
                                    text "{b}" + "Quest: {0}".format(index+1) + "{/b}"
                                    text "Title: {0}".format(quest["title"])
                                    text "Brief: {0}".format(quest["shortMsg"]) 
                                    textbutton "Show description": 
                                        action SetScreenVariable("current_quest", index) 
                                    if current_display == "ongoing":
                                        textbutton "Complete quest":
                                            action Function(quests.completeQuest, index)
                    # Add scrollbar
                    vbar value YScrollValue(_vpgrid_name)
        # Right vertical box for longer description
        vbox:
            xoffset 20
            style "quest_panel"
            frame:  # The frame window is used for dialogue, which has a maroon color
                has vbox    # Give it the size of the vbox
                if current_quest >= len(current_quests):
                    $ current_quest = None
                if current_quest is None:
                    text "{b}A quest has not been selected{/b}"
                else:
                    text "{b}" + "Quest {0} description:".format(current_quest+1) + "{/b}"
                    text current_quests[current_quest]["longMsg"]

    
                