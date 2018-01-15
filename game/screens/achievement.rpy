screen achievement:
# ensures other menu screens are replaced
    tag menu

    # Include the navigation menu
    use navigation
    add "Quests.jpg"

    # Give title of page
    frame:
        area (0, 0, 500, 50)
        text "Achievements": 
            size 45
            xoffset 30
            yoffset 10
            font "DejaVuSans.ttf"
