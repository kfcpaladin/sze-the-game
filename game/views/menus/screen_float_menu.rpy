# float menu for the game
screen float_menu:
    use refreshTimer
    frame:
        background Solid(PrimaryColours.CLEAR)
        align (0.84, 0.04)
        has vbox
        spacing 10
        textbutton _("Open Diary"): # _(...) prevents the sfx sound from being played twice
            action [
                Hide("popup"), # prevent popup screen from being frozen
                Function(diary.open)
            ]
            xalign 0.5
        textbutton _("{color=[PrimaryColours.WHITE]}{b}kms{b}{/color}"):
            background Solid(themes.default.rainbow)
            xminimum 150
            action [
                Show("kms"),
            ] 
            xalign 0.5

# a timer that does nothing but refresh a screen
screen refreshTimer(rate=0.1):
    timer rate:
        repeat True
        action Function(lambda: None)