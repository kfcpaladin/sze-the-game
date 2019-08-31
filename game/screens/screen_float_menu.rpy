# float menu for the game
screen float_menu:
    use refreshTimer
    frame:
        background Solid(colour.transparent)
        align (0.84, 0.04)
        has vbox
        spacing 10
        textbutton _("Open Diary"): # _(...) prevents the sfx sound from being played twice
            action [
                Hide("popup"), # prevent popup screen from being frozen
                Show(diary.getCurrentPage()), 
            ]
            xalign 0.5
        textbutton _("{color=[colour.white]}{b}kms{b}{/color}"):
            background Solid(colour.rainbow)
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