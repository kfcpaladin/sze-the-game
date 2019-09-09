# make a quest list
screen quest_screen(controller, rect, theme):
    $ select_rect = rect.resize_from_top_left(height=40).add_offset(Vector2D(0, -50))
    $ info_rect = rect.resize_from_top_left(height=415)
    $ description_rect = rect.resize_from_bottom_left(height=100).add_offset(-Vector2D(0, 100))

    use quest_select(controller, select_rect, theme)
    use quest_info(controller, info_rect, theme)
    use quest_description(controller, description_rect, theme)

screen quest_select(controller, rect, theme):
    hbox:
        xoffset rect.left
        yoffset rect.top
        frame:
            xsize rect.width
            ysize rect.height 
            has hbox 
            textbutton unicode.title("Hidden")    action [Function(controller.select_hidden)]
            textbutton unicode.title("Unlocked")  action [Function(controller.select_unlocked)]
            textbutton unicode.title("Completed") action [Function(controller.select_completed)]

# Quest info
screen quest_info(controller, rect, theme):
    vbox:
        xoffset rect.left
        yoffset rect.top
        xsize rect.width
        frame:         
            has vbox    
            text "{b}" + "{0} Quests".format(controller.current_filter_name.title()) + "{/b}"
            if controller.quests and len(controller.quests) > 0:
                # Grid and scroll bar
                side "c r":
                    $ _vpgrid_name = "quest_vpgrid"
                    vpgrid id (_vpgrid_name):
                        cols 1
                        spacing 10
                        draggable True
                        mousewheel True
                        xsize rect.width-25
                        ysize rect.height 
                        for quest in controller.quests:
                            use quest_entry(controller, quest, rect, theme)
                    vbar value YScrollValue(_vpgrid_name)
            else:
                text "No quests are currently {0}".format(controller.current_filter_name)

# Quest entry
screen quest_entry(controller, quest, rect, theme):
    default iconSize = 105
    frame:
        style "quest_entry"
        xsize rect.width-25
        background Solid(controller.get_quest_colour(quest, theme))
        hbox:
            ysize iconSize
            spacing 5
            use icon_frame(quest.icon, iconSize, iconSize, loadImage("quest_default.png"))
            vbox:
                ysize iconSize
                # quest info
                text "{b}" + "Quest: {0}".format(quest.id) + "{/b}"
                text "{{b}}Title: {{/b}}{0}".format(quest.title)
                text "{{b}}Brief: {{/b}}{0}".format(quest.brief)
                # interactive buttons
                hbox:
                    spacing 5
                    # only show start if in available
                    if quest.is_unlocked and not quest.is_complete:
                        textbutton "Start quest"  action [Function(controller.start_quest, quest)]
                    textbutton "Show description" action [Function(controller.select_quest, quest)]
                    

# Longer description
screen quest_description(controller, rect, theme):
    vbox:
        xoffset rect.left
        yoffset rect.top 
        frame:          
            xsize rect.width 
            ymaximum rect.height 
            has vbox    
            $ quest = controller.quest
            if quest:
                text "{{b}}Description: {{/b}}{0}".format(quest.description)
            else:
                text "{b}A quest has not been selected{/b}"