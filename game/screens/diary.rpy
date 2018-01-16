###########################################################################################################################################################
screen float_menu:
    frame:
        background Solid("#ffffff00")
        align (0.84, 0.04)
        has vbox
        spacing 10
        textbutton "Open Diary":
            action [
                ShowMenu(diary.getCurrentPage()), 
            ]
            xalign 0.5
        textbutton "kms":
            action [
                ShowMenu("kms"),
            ] 
            xalign 0.5

# navigation for all diary pages
screen diary_nav:
    hbox xcenter 1366/2:
        for index, screenName in enumerate(diary.screenNames):
            textbutton _(str(index)):
                action [
                    Hide("diary_nav_buttons"),
                    Hide(diary.getCurrentPage()),
                    ShowMenu(diary.getPage(index)),
                    Function(diary.setPage, index),
                ]                    

# diary title
screen diary_title(title="Undefined"):
    $ title = unicode.title(title)
    frame:
        area (0, 0, 500, 50)
        text title: 
            size 45
            xoffset 30
            yoffset 10
            font "DejaVuSans.ttf"



