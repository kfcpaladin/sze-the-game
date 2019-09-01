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
screen diary_bag(controller=view_controllers.bag, inventory=inventories.bag):
    modal True
    # screen components
    add loadImage("screen_bg_diaryGrid.png")
    use diary_nav
    use diary_title(inventory.name)
    # custom positioning of attribute screen on right page
    use attribute_screen(
        view_controllers.attributes, 
        view_controllers.right_diary_page)
    # allow bag tooltip to cover attribute screen 
    use bag_screen(controller, inventory, Rect2D(right=590, bottom=590).add_offset(Vector2D(43, 131)))

# quests
screen diary_quests:
    modal True
    add loadImage("screen_bg_diaryNormal.png")
    use diary_nav
    use diary_title("Quests")
    # Show panels
    use attribute_screen(
        view_controllers.attributes,
        view_controllers.left_diary_page)
    use quest_screen(
        view_controllers.quests,
        view_controllers.right_diary_page)

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
screen diary_statistics:
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


        



