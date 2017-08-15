label econ1:
    "It's time for some economics 101 with Garth Chapman, and u are ready to absorb this {s}bullshit{s} uh, i mean buitifool knowledges."
    "Like sponges Chappo tells us he expects us to just be able to vomit back out what he tells us"
    "And as usual, the first class is underprepared with no content, so i guess it's time for a kahoot!"
    $ kahootpoints == 0
    call econ1kahoot1
    "Score is [kahootpoints]"
    jump dead

label econ1kahoot1:
    $ time = 15
    $ timer_range = 15
    $ timer_jump = 'econ1kahoot1slow'
    show screen countdown
    "Which country has the longest uninterrupted economic growth?"
    menu:
        "Australia":
            hide screen countdown
            "Correct"
            if time > 5:
                $ kahootpoints += 2
            else:
                $ kahootpoints += 1
            return
        "US":
            hide screen countdown
            e "Wrong"
            return
        "China":
            hide screen countdown
            e "Wrong"
            return
        "Uganda":
            hide screen countdown
            e "Wrong"
            return

label econ1kahoot1slow1:
    sze "\"Fuck im too slow\""
    return
