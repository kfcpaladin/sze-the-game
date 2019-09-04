# developer page
screen diary_developer:
    modal True
    use diary_page("Developer menu"):
        use label_screen
        use sound_screen
        use time_screen
        use minigames_screen
        use screen_console

# bag
screen diary_bag(controller=view_controllers.bag, inventory=inventories.bag):
    modal True
    use diary_page(inventory.name, background="screen_bg_diaryGrid.png"):
        # custom positioning of attribute screen on right page
        use attribute_screen(
            view_controllers.attributes, 
            view_controllers.right_diary_page,
            themes.default)
        # allow bag tooltip to cover attribute screen 
        use bag_screen(
            controller, 
            inventory, 
            Rect2D(right=590, bottom=590).add_offset(Vector2D(43, 131)),
            themes.default)

# quests
screen diary_quests:
    modal True
    use diary_page("Quests"):
        # Show panels
        use attribute_screen(
            view_controllers.attributes,
            view_controllers.left_diary_page,
            themes.default)
        use quest_screen(
            view_controllers.quests,
            view_controllers.right_diary_page,
            themes.default)

# achievements
screen diary_achievements:
    modal True
    use diary_page("Achievements"):
        use attribute_screen(
            view_controllers.attributes,
            view_controllers.left_diary_page,
            themes.default)
        use achieve_screen(
            view_controllers.achievements,
            view_controllers.right_diary_page,
            themes.default)

# attribute and friend stats
screen diary_statistics:
    modal True
    use diary_page("Statistics"):
        # display info
        use attribute_screen(
            view_controllers.attributes,
            view_controllers.left_diary_page,
            themes.default)
        use friend_screen(
            view_controllers.friends, 
            Friend.get_all(), 
            view_controllers.right_diary_page,
            themes.default)

# roadmap
screen diary_roadmap:
    modal True
    use diary_page("Roadmap"):
        use roadmap_screen


        



