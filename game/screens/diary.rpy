###########################################################################################################################################################
screen float_menu:
    frame:
        background Solid("#ffffff00")
        align (0.84, 0.04)
        has vbox
        spacing 10
        textbutton _("Open Diary"): # _(...) prevents the sfx sound from being played twice
            action [
                Show(diary.getCurrentPage()), 
            ]
            xalign 0.5
        textbutton _("kms"):
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
                    Function(closeDescriptionScreens),
                    Hide(diary.getCurrentPage()),
                    Show(diary.getPage(index)),
                    Function(diary.setPage, index),
                ]
        textbutton "Close":
            action [
                Hide("diary_nav_buttons"),
                Function(closeDescriptionScreens),
                Hide(diary.getCurrentPage())
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

##############################################################################
# Due to the way description boxes are implemented, they need to be updated
# manually after each closing
init python:
    descriptionScreens = [
        "achieve_description",
        "attribute_info_description",
        "friend_info_description",
        "label_screen_description",
        "label_screen_unsafe",
        "minigames_screen_kahoot",
        "quest_description",
        "sound_screen_music_list",
    ]

    def closeDescriptionScreens():
        for screen in descriptionScreens:
            renpy.hide_screen(screen)
        



