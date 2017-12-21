screen questscreen:
    tag menu
    # Include the navigation.
    use navigation
    frame:
        style_group "prefs"
        xfill True
        for index, quest in enumerate(quests.quests):
            vbox:
                frame:
                    has vbox
                    text "Quest {0}".format(index)
                    text "Title: {0}".format(quest["title"])
                    text "Brief: {0}".format(quest["shortMsg"])
                    text "Description: {0}".format(quest["longMsg"])