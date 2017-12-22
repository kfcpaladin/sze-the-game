#################################################################################
#timer bar
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

style kahoot_answers:
    xalign 0.5
    yalign 0.7

######################################################################################
# kahootGame will play a game of kahoot, given a dictionary of answers and questions
# question = {
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
label kahootGame(question, show_result=True, **options):
    menu:
        "Start Kahoot?":
            $ playmusic("kahoot.ogg")
            call screen countdown(question=question["question"], answers=question["answers"], **options)
            $ stopmusic()
            $ _points = game.kahootScore["points"]
            $ _time_remain = game.kahootScore["time_remain"]
            $ _choice = game.kahootScore["choice"]
            $ game.kahootStarted = False
            $ game.kahootScore = {"points": 0, "time_remain": 0, "choice": None}
            if show_result:
                "You got [_points] points with [_time_remain] seconds remaining"
            return
        "Pussy out":
            "Your knees start shaking and your penis recedes into its cavity"
            "Finally you give up on the game of Kahoot"
            return

screen countdown(question="No question?", answers={}, time_range=10,speed=0.01):
    default time_remain = time_range
    if game.kahootStarted is False:
        $ game.kahootStarted = True
        
    timer speed:
        repeat True
        action If(time_remain > 0,
                    true=[
                        SetScreenVariable('time_remain', time_remain-speed),
                    ], 
                    false=[
                        Hide('countdown'),
                        SetField(game, 'kahootScore', {"points": 0, "time_remain": 0, "choice": None}),
                        Return(0)
                    ]
        )
    # Bar will have a value proportional to the time remaining
    bar:
        value time_remain 
        range time_range 
        xalign 0.5 
        yalign 0.1 
        xmaximum 600 at alpha_dissolve # This is the timer bar.
    hbox:
        xalign 0.5
        yalign 0.2
        frame:
            has hbox
            text question
    vpgrid id ("answers_vpgrid"):
        cols 1
        spacing 20
        draggable True
        mousewheel True
        style "kahoot_answers"
        for answer in answers:
            textbutton answer:
                xalign 0.5
                action [
                    Hide('countdown'), 
                    SetField(game, 'kahootScore', {"points": answers[answer], "time_remain": time_remain, "choice": answer}),
                    Return(0)
                ]
    vbar value YScrollValue("answers_vpgrid")





