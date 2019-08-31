##############################################################################
# developer page
screen diary_developer:
    modal True # prevent interaction underneath
    add loadImage("screen_bg_diaryNormal.png")
    use diary_nav
    use diary_title("Developer Menu")
    # use developer consoles
    use label_screen
    use sound_screen
    use time_screen
    use minigames_screen
    use screen_console

# bag
screen diary_bag(bag=bag):
    modal True
    # screen components
    add loadImage("screen_bg_diaryGrid.png")
    use diary_nav
    use diary_title(bag.name)
    # custom positioning of attribute screen on right page
    use attribute_screen(
        view_controllers.attributes, 
        view_controllers.right_diary_page)
    # allow bag tooltip to cover attribute screen 
    use bag_screen(bag)

# quests
screen diary_quests(quests=quests):
    modal True
    add loadImage("screen_bg_diaryNormal.png")
    use diary_nav
    use diary_title("Quests")
    # Show panels
    use attribute_screen(
        view_controllers.attributes,
        view_controllers.left_diary_page)
    use quest_screen(quests)

# achievements
screen diary_achievements:
    modal True
    add loadImage("screen_bg_diaryNormal.png")
    use diary_nav
    use diary_title("Achievements")
    use attribute_screen(
        view_controllers.attributes,
        view_controllers.left_diary_page)
    use achieve_screen(view_controllers.achievements)

# attribute and friend stats
screen diary_statistics(controller=view_controllers.attributes):
    # prevent interaction underneath
    modal True
    # Include the navigation.
    add loadImage("screen_bg_diaryNormal.png")
    use diary_nav
    use diary_title("Statistics")
    # display info
    use attribute_screen(
        view_controllers.attributes,
        view_controllers.left_diary_page)
    use friend_screen(friendList)

# roadmap
screen diary_roadmap:
    modal True
    add loadImage("screen_bg_diaryNormal.png")
    use diary_nav
    use diary_title("Roadmap")
    use roadmap_screen

##############################################################################
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
        



