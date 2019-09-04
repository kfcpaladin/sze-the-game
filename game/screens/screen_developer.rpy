# Labels explorer menu
screen label_screen(labels=labels):
    default labelConfig = AttrDict({
        "labels": labels,
        "currentDescription": None,
    })
    vbox:
        style "label_screen"
        frame:
            has vbox
            text "{b}Labels Menu{/b}"
            side "c r":
                $ _vpgrid_name = "label_screen_grid"
                vpgrid id(_vpgrid_name):
                    cols 1
                    draggable True
                    mousewheel True
                    spacing 10
                    style "label_screen_vpgrid"
                    for label in labels:
                        use label_screen_entry(labelConfig, label)
                vbar value YScrollValue(_vpgrid_name)
    use label_screen_description(labelConfig.currentDescription)

# entry for labels menu
screen label_screen_entry(labelConfig, label):
    default defaultColour = PrimaryColours.GREEN
    default showDescription = False
    $ colour = defaultColour
    if "colour" in label:
        $ colour = label["colour"]
    frame:
        background Solid(colour)
        style "label_screen_entry"
        vbox:
            
            text "{b}" + "{0}".format(label["name"]) + "{/b}" 
            hbox:
                spacing 5
                textbutton "Jump":
                    action If(
                        ("call" in label and label["call"]) or ("jump" in label and label["jump"]),
                        true = [
                            Function(diary.close),
                            Function(renpy.jump, label["name"]),
                        ],
                        false = [
                            Show("label_screen_unsafe", None, label),
                            Function(playsfx, "error.ogg"),
                        ]
                    )
                textbutton "Call":
                    action [
                        Function(diary.close),
                        Function(renpy.call, label["name"]),
                    ]
                textbutton "Show description":
                    action [
                        Function(labelConfig.update, currentDescription=label)
                    ]

# screen for unsafe jump
screen label_screen_unsafe(label, timeout=5):
    modal True
    timer timeout:
        repeat False
        action [
            Hide("label_screen_unsafe", dissolve)
        ]
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            text "{b}" + "Warning, {0} has no jump or call labels!".format(label["name"]) + "{/b}" xalign 0.5
            text "{b}" + "If you continue, you will return back to main menu" + "{/b}" xalign 0.5
            text "{b}" + "Continue?" + "{/b}" xalign 0.5
            hbox:
                xalign 0.5
                spacing 5
                textbutton "Yes":
                    action [
                        Function(diary.close),
                        Function(renpy.jump, label["name"]),
                    ]
                textbutton "No":
                    action [
                        Hide("label_screen_unsafe"),
                    ]

# description
screen label_screen_description(label):
    default options = ["jump", "call"]
    vbox:
        style "label_screen_description"
        frame:
            xsize 625
            has vbox
            if label:
                for option in options:
                    text "{b}" + "{0}".format(unicode.title(option)) + "{/b}"
                    if option in label and label[option]:
                        text listToText(label[option])
                    else:   
                        text "None"
            else:
                text "{b}Select a label for description{/b}"

# sound control board
screen sound_screen:
    default showMusicList = False
    default showSfxList = False
    vbox:
        style "sound_screen"
        frame:
            has vbox
            text "{b}Sound Menu{/b}"
            hbox:
                spacing 5
                # music commands
                textbutton "Play music":
                    action [
                        Show("sound_screen_audio_list", playFunction=playmusic),
                    ]
                textbutton "Stop music":
                    action Function(stopmusic)
                # sfx commands
                textbutton "Play sfx":
                    action [
                        Show("sound_screen_audio_list", playFunction=playsfx),
                    ]
                textbutton "Stop sfx":
                    action Function(stopsfx)


# list of cached audio files
screen sound_screen_audio_list(playFunction=playmusic):
    modal True
    vbox:
        style "sound_screen_audio_list"
        frame:
            xsize 500
            has vbox
            # title of window with close button
            hbox:
                xsize 500
                text "{b}Select file to play{/b}":
                    xalign 0.5
                    xoffset 80
                textbutton "x":
                    xalign 1
                    xoffset 120
                    action [
                        Hide("sound_screen_audio_list"),
                    ]
            # a list of all music files
            side "c r":
                $ _grid_name = "music_list_vpgrid"
                vpgrid id (_grid_name):
                    xsize 500
                    ymaximum 500
                    spacing 5
                    cols 1
                    draggable False
                    mousewheel True
                    for file, filepath in audioCache.iteritems():
                        # determine if file is "appropriate" for the function
                        # this is an arbituary distinction thats made for convenience
                        # i.e a file in sfx/ can still be played using playmusic()
                        # but it clutters the menu and removes clarity
                        if sortAudioFile(filepath, playFunction):   
                            textbutton file:
                                xsize 475
                                xalign 0.5 
                                action [
                                    Function(playFunction, file),
                                ]
                vbar:
                    value YScrollValue(_grid_name)

# time control board
screen time_screen:
    vbox:
        style "time_screen"
        frame:
            has vbox
            text "{b}" + "Time Control ({0})".format(clock.get_time()) + "{/b}" 
            hbox:
                spacing 5
                for time in clock.times:
                    textbutton time:
                        action [
                            Function(clock.set_time, time)
                        ]

# minigames
screen minigames_screen:
    vbox:
        style "minigames_screen"
        frame:
            has vbox
            text "{b}Minigames{/b}"
            hbox:
                spacing 5
                textbutton "Pong":
                    action [
                        Function(diary.close),
                        Function(renpy.call, "playPong"),
                    ]
                textbutton "Kahoot":
                    action [
                        Show("minigames_screen_kahoot", None, kahoot)
                    ]

screen minigames_screen_kahoot(kahootQuestions):
    modal True
    vbox:
        style "minigames_screen_kahoot"
        frame:
            xsize 300
            has vbox
            # window title with close button
            hbox:
                xsize 300
                text "{b}Questions{/b}":
                    xalign 0.5
                    xoffset 50
                textbutton "x":
                    xalign 1
                    xoffset 70
                    action [
                        Hide("minigames_screen_kahoot"),
                    ]
            # list of all kahoot questions
            side "c r":
                $ _grid_name = "minigames_screen_kahoot_vpgrid"
                vpgrid id (_grid_name):
                    xsize 300
                    spacing 5
                    cols 1
                    draggable False
                    mousewheel True
                    for name, kahootQuestion in kahootQuestions.iteritems():
                        textbutton name:
                            xsize 275
                            xalign 0.5
                            action [
                                Function(diary.close),
                                Function(renpy.call, "kahootGame", kahootQuestion)
                            ]
                vbar:
                    value YScrollValue(_grid_name)
            

# get call labels to all screens
screen screen_console:
    default availableScreens = ["fortmap"]
    vbox:
        style "screen_console"
        frame:
            has vbox
            text "{b}Screen Console{/b}"
            hbox:
                spacing 5
                for screen in availableScreens:
                    textbutton screen:
                        action [
                            ShowMenu(screen),
                        ]
                    

                

# convert list of strings to properly formatted
init python:
    def listToText(messages):
        if type(messages) is not list:
            messages = [messages]
        text = ""
        for index, message in enumerate(messages):
            if message is None:
                message = "None"
            text += str(message)
            if index is not len(messages)-1:
                text += ", "
        return text

###########################################################################
style label_screen:
    xoffset 40
    xsize 625
    yoffset 95

style label_screen_vpgrid:
    xsize 600
    ymaximum 415

style label_screen_description:
    xsize 625
    ysize 100
    xoffset 40
    yoffset 565

style label_screen_entry:
    xsize 600
    ymaximum 50

style sound_screen:
    xoffset 720
    xsize 625
    yoffset 95

style time_screen:
    xoffset 720
    xsize 625
    yoffset 185

style minigames_screen:
    xoffset 720
    xsize 625
    yoffset 275

style minigames_screen_kahoot:
    xsize 300
    xcenter 0.5
    ycenter 0.5

style screen_console:
    xoffset 720
    xsize 625
    yoffset 365

style sound_screen_audio_list:
    xsize 500
    spacing 5
    xcenter 0.5
    ycenter 0.5