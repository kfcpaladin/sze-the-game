init python:
    diaryScreens = []
    # if developer allow access to developer console
    if config.developer:
        diaryScreens.append("developerScreen")
    # add normal screens
    diaryScreens.extend([
        "bag_view",
        "questscreen",
        "achievementscreen",
        "statsscreen",
        "roadmap"
    ])
    # create diary
    diary = Diary(*diaryScreens)