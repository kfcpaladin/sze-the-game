# float menu for the game
screen float_menu:
    frame:
        background Solid(colour.clear)
        align (0.84, 0.04)
        has vbox
        spacing 10
        if game.diaryIntro or config.developer:
            textbutton _("Open Diary"): # _(...) prevents the sfx sound from being played twice
                action [
                    Hide("popup"), # prevent popup screen from being frozen
                    Function(popupList.clear),
                    Show(diary.getCurrentPage()), 
                ]
                xalign 0.5
        textbutton _("kms"):
            action [
                Show("kms"),
            ] 
            xalign 0.5