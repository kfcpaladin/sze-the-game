###########################################################################################################################################################
screen diary_button:
    textbutton "Open Diary" action [ Show("diary_page_1"), Hide("diary_button")] align (0.84, 0.04)
    textbutton "Pong" action [ Function(renpy.call, "playPong"), Hide("diary_button")] align (0.64, 0.04)

screen diary_page_1:
    modal True
    tag Diary
    add "Diary.jpg"
    mousearea:
        area (400, 0, 566, 100)
        hovered Show("diary_nav", transition=dissolve)
        unhovered Hide("diary_nav", transition=dissolve)
    text "Timetable" size 65 align (0.02, 0.03) font "times.ttf"
    text "To-Do"     size 65 align (0.98, 0.03) font "times.ttf"
    imagebutton idle "blank" area (1100, 0, 266, 768) action Show("diary_page_2")
    key "game_menu" action [Hide("diary_page_1"), Show("diary_button")]

screen diary_page_2:
    modal True
    tag Diary
    add "Diary.jpg"
    mousearea:
        area (400, 0, 566, 100)
        hovered Show("diary_nav")
        unhovered Hide("diary_nav")
    text "Page 2" size 65 align (0.02, 0.03) font "times.ttf"
    text "Lel"     size 65 align (0.98, 0.03) font "times.ttf"
    imagebutton idle "blank" area (0, 0, 266, 768) action Show("diary_page_1")
    imagebutton idle "blank" area (1100, 0, 266, 768) action Show("diary_page_3")
    key "game_menu" action [Hide("diary_page_2"), Show("diary_button")]

screen diary_page_3:
    modal True
    tag Diary
    add "Diary.jpg"
    mousearea:
        area (400, 0, 566, 100)
        hovered Show("diary_nav")
        unhovered Hide("diary_nav")
    text "Page 3" size 65 align (0.02, 0.03) font "times.ttf"
    text "Lel"     size 65 align (0.98, 0.03) font "times.ttf"
    imagebutton idle "blank" area (0, 0, 266, 768) action Show("diary_page_2")
    key "game_menu" action [Hide("diary_page_3"), Show("diary_button")]

screen diary_nav:
    hbox xcenter 1366/2:
        grid 3 1:
            textbutton _("1") action ShowMenu("diary_page_1")
            textbutton _("2") action ShowMenu("diary_page_2")
            textbutton _("3") action ShowMenu("diary_page_3")
