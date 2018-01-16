###########################################################################
# Developer console

screen developerScreen:
    add "Quests.jpg"
    use diary_nav
    # Give title of page
    frame:
        area (0, 0, 500, 50)
        text "Developer Menu": 
            size 45
            xoffset 30
            yoffset 10
            font "DejaVuSans.ttf"
    
    # use developer consoles
    use label_screen
    use label_screen_description
    use sound_screen
    use time_screen
    use minigames_screen

# Labels explorer menu
screen label_screen:
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
                        use label_screen_entry(label)
                vbar value YScrollValue(_vpgrid_name)

# entry for labels menu
screen label_screen_entry(label):
    default defaultColour = "#009933"
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
                    action [
                        Hide("developerScreen"),
                        Hide("label_screen_description"),
                        Function(renpy.jump, label["name"])
                    ]
                textbutton "Call":
                    action [
                        Hide("developerScreen"),
                        Hide("label_screen_description"),
                        Function(renpy.call, label["name"])
                    ]
                textbutton "Show description":
                    action [
                        Show("label_screen_description", label=label)
                    ]

# description
screen label_screen_description(label=None):
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
    vbox:
        style "sound_screen"
        frame:
            has vbox
            text "{b}Sound Menu{/b}"
            hbox:
                spacing 5
                textbutton "Stop music":
                    action Function(stopmusic)
                textbutton "Stop sfx":
                    action Function(stopsfx)

# time control board
screen time_screen:
    vbox:
        style "time_screen"
        frame:
            has vbox
            text "{b}Time Control{/b}"
            hbox:
                spacing 5
                for time in game.currentTime:
                    textbutton time:
                        action [
                            Function(game.setTime, time)
                        ]

# minigames
screen minigames_screen:
    default showKahoot = False
    vbox:
        style "minigames_screen"
        frame:
            has vbox
            text "{b}Minigames{/b}"
            hbox:
                spacing 5
                textbutton "Pong":
                    action [
                        Hide("developerScreen"),
                        Jump("playPong"),
                    ]
                textbutton "Kahoot":
                    action If(
                        showKahoot is False,
                        true = [
                            SetScreenVariable("showKahoot", True)
                        ],
                        false = [
                            SetScreenVariable("showKahoot", False)
                        ]
                    )
    # toggle kahoot screen
    if showKahoot:
        use minigames_screen_kahoot(kahoot)

screen minigames_screen_kahoot(kahootQuestions):
    vbox:
        style "minigames_screen_kahoot"
        frame:
            has vbox
            text "{b}Questions{/b}"
            for name, kahootQuestion in kahootQuestions.iteritems():
                textbutton name:
                    xalign 0.5
                    action [
                        Hide("developerScreen"),
                        Hide("minigames_screen_kahoot"),
                        Function(renpy.call, "kahootGame", kahootQuestion)
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
    xoffset 900
    xsize 100
    yoffset 250