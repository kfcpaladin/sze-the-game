screen diary_page(title, background="screen_bg_diaryNormal.png"):
    modal True # prevent interaction underneath
    add loadImage(background)
    use diary_nav
    use diary_title(title)
    transclude

# navigation for all diary pages
screen diary_nav:
    hbox xcenter 1366/2:
        for index, page in enumerate(diary.pages):
            textbutton _(str(index)) action [Function(diary.select_page, index)]
        textbutton "Close" action [Function(diary.close)]                    

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