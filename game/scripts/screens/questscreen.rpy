screen questscreen:
    tag menu
    # Include the navigation.
    use navigation
    frame:
        style_group "prefs"
        xfill True
    for index, quest in enumerate(quests.quests):
        hbox:
            spacing 25
            vbox: 
                area (0, 0, 250, 500) 
                xsize 1000 ysize 400
                text "Quest {0}".format(index)
                text "Title: {0}".format(quest["title"])
                text "Brief: {0}".format(quest["shortMsg"])
                text "Description: {0}".format(quest["longMsg"])