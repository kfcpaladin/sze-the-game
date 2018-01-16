######################################################################################
# kahootGame will play a game of kahoot, given a dictionary of answers and questions
# kahoot = {
#     "question": "the question?",
#     "answers": {
#         "answer1": score1,
#         "answer2": score2,
#     }
# }
# It will store the game results in the following:
#     _points = Points from the game of kahoot
#     _time_remain = Time that was remaining when finished
#     _choice = The choice that was made (None if time ran out) 
label kahootGame(kahoot, show_result=True, **options):
    menu:
        "Start Kahoot?":
            $ playmusic("kahoot.ogg")
            call screen kahootscreen(question=kahoot["question"], answers=kahoot["answers"], **options)
            $ stopmusic()
            $ _points = _return["points"]
            $ _time_remain = _return["time_remain"]
            $ _choice = _return["choice"]
            if show_result:
                "You chose [_choice]"
                "You got [_points] points with [_time_remain] seconds remaining"
            return
        "Pussy out":
            "Your knees start shaking and your penis recedes into its cavity"
            "Finally you give up on the game of Kahoot"
            return

screen kahootscreen(question="No question?", answers={}, time_range=10,speed=0.25):
    default time_remain = time_range
    timer speed:
        repeat True
        action If(
            time_remain > 0,
            true=[
                SetScreenVariable('time_remain', time_remain-speed),
            ], 
            false=[
                Hide('kahootscreen', dissolve),
                Return({"points": 0, "time_remain": 0, "choice": None})
            ]
        )
    # Bar will have a value proportional to the time remaining
    bar:
        value time_remain 
        range time_range 
        xalign 0.5 
        yalign 0.1 
        xmaximum 600 at alpha_dissolve # This is the timer bar.
    
    # show question
    hbox:
        xalign 0.5
        yalign 0.2
        frame:
            has hbox
            text question

    # show all answers
    frame:
        background Color("#ffffff00")
        style "kahoot_answers"
        vbox:
            style "kahoot_answers"
            spacing 10
            for answer, points in answers.iteritems():
                textbutton answer:
                    xalign 0.5
                    action [
                        Hide('kahootscreen', dissolve),
                        Return({"points": points, "time_remain": time_remain, "choice": answer})
                    ]
                    hovered [
                        Function(playsfx, "8d82b5_Final_Fantasy_XI_Menu_Selection_Sound_Effect.ogg")
                    ]

#################################################################################
#timer bar
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

style kahoot_answers:
    xalign 0.5
    yalign 0.4





