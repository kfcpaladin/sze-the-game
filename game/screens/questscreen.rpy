screen questscreen:
    tag menu
    # Include the navigation.
    use navigation
    use navigation
    grid 2 1:
        style_group "prefs"
        xfill True
        vbox:
            frame:
                has vbox
                text "{b}Ongoing quests{/b}"
                for index, quest in enumerate(quests.ongoing):
                    text "Quest: {0}".format(index+1)
                    text "Title: {0}".format(quest["title"])
                    text "Brief: {0}".format(quest["shortMsg"])
                    text "Description: {0}".format(quest["longMsg"])
                    text " "
        vbox:
            frame:
                has vbox
                text "{b}Completed quests{/b}"
                for index, quest in enumerate(quests.completed):
                    text "Quest: {0}".format(index+1)
                    text "Title: {0}".format(quest["title"])
                    text "Brief: {0}".format(quest["shortMsg"])
                    text "Description: {0}".format(quest["longMsg"])
                    text " "
                