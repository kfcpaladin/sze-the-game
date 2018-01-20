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
        bag.who, 
        {
            "infoBox": AttrDict({
                "pos": Vector(720, 95), 
                "size": Vector(625, 415),
            }),
            "descriptionBox": AttrDict({
                "pos": Vector(720, 95+470),
                "size": Vector(625, 100),
            }),
        },
    )
    # allow bag tooltip to cover attribute screen 
    use bag_screen(bag)

# quests
screen diary_quests(quests=quests):
    modal True
    add loadImage("screen_bg_diaryNormal.png")
    use diary_nav
    use diary_title("Quests")
    # Show panels
    use attribute_screen(sze)
    use quest_screen(quests)

# achievements
screen diary_achievements(achievements=achievements):
    modal True
    add loadImage("screen_bg_diaryNormal.png")
    use diary_nav
    use diary_title("Achievements")
    use attribute_screen(sze)
    use achieve_screen(achievements)

screen diary_statistics(who=sze):
    # prevent interaction underneath
    modal True
    # Include the navigation.
    add loadImage("screen_bg_diaryNormal.png")
    use diary_nav
    use diary_title("Statistics")
    # display info
    use attribute_screen(who)
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

##############################################################################
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
    diary = Diary(*diaryScreens)


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
        



