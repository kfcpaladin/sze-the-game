# make diary object
init python:
    # create diary objects
    diaryScreens = []
    # if developer allow access to developer console
    if config.developer:
        diaryScreens.append("diary_developer")
    # add normal screens
    diaryScreens.extend([
        "diary_bag",
        "diary_quests",
        "diary_achievements",
        "diary_statistics",
        "diary_roadmap"
    ])
    diary = Diary(diaryScreens)

    # developer description boxes are prone to being stuck
    descriptionScreens = [
        "bag_tooltip",
        "label_screen_description",
        "label_screen_unsafe",
        "minigames_screen_kahoot",
        "popup",
        "sound_screen_audio_list",
    ]

    def closeDiary():
        for screen in descriptionScreens:
            renpy.hide_screen(screen)
        renpy.hide_screen(diary.getCurrentPage())
        renpy.hide_screen("diary_nav_buttons")
        popupList.clear()