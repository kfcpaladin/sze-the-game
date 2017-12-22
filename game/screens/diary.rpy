###########################################################################################################################################################
screen diary_button:
    textbutton "Open Diary" action [ Show("diary_screen"), Hide("diary_button")] align (0.84, 0.04)

screen diary_screen:
    modal True
    textbutton "Close Diary" action [ Hide("diary_screen"), Show("diary_button")] align (0.84, 0.04)
    add "Diary.jpg"
    text "Timetable" size 65 align (0.02, 0.03) font "times.ttf"
    text "To-Do"     size 65 align (0.98, 0.03) font "times.ttf"
    key "game_menu" action [Hide("diary_screen"), Show("diary_button")]