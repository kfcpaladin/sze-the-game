###########################################################################################################################################################
screen float_menu:
    frame:
        background Solid("#ffffff00")
        align (0.84, 0.04)
        has vbox
        spacing 10
        textbutton _("Open Diary"): # _(...) prevents the sfx sound from being played twice
            action [
                Hide("popup"), # prevent popup screen from being frozen
                Function(popupList.clear),
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
                    Function(closeDiary),
                    Show(diary.getPage(index)),
                    Function(diary.setPage, index),
                ]
        textbutton "Close":
            action [
                Function(closeDiary),
            ]                    

# diary title
screen diary_title(title="Undefined"):
    $ title = unicode.title(title)
    vbox:
        area (0, 0, 500, 50)
        text title: 
            size 45
            xoffset 40
            yoffset 20
            font "DejaVuSans.ttf"

##############################################################################
# Due to the way description boxes are implemented, they need to be updated
# manually after each closing
init python:
    descriptionScreens = [
        "achieve_description",
        "attribute_info_description",
        "bag_tooltip",
        "friend_info_description",
        "label_screen_description",
        "label_screen_unsafe",
        "minigames_screen_kahoot",
        "popup",
        "quest_description",
        "sound_screen_audio_list",
    ]

    def closeDiary():
        for screen in descriptionScreens:
            renpy.hide_screen(screen)
        renpy.hide_screen(diary.getCurrentPage())
        renpy.hide_screen("diary_nav_buttons")
        popupList.clear()
        



