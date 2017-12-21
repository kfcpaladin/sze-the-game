label econ1:
    "It's time for some economics 101 with Garth Chapman, and u are ready to absorb this {s}bullshit{/s} uh, i mean buitifool knowledges."
    "Like sponges Chappo tells us he expects us to just be able to vomit back out what he tells us"
    pra "\"Arthur, how many past papers have you done?\""
    sze "\"wtf this is first class pragash\""
    pra "\"wow arthur u will never be real economist. i spend every day of every second not doing engineering, but doing the SUPERIOR SUPREME subject, the one every one cares about, i know you love it, i love it, we all love it\""
    pra "\"ECONOMICSSSSSSSS!!!!!!!!!!!!!!!\""
    sze "\"wait wtf how many have you d-\""
    pra "\"This is the meaning to my life, rejoice, REJOICE! It is my time to shine, ask me any questions, for i shall answer thee, as i am the economics god, god of all economics, ekonomiks, echonomics, ekconomix\""
    pra "\"Opportunity cost, J-curve, Keynesian Income Expenditure Graph, Ecologically Sustainable Development, Fuel Quality Standards Act 2000, Fiscal consolidary discretionary macroeconomics policies, I know it all!!!!!!!!!!!\""
    sze "\"pragash plez-\""
    pra "\"now that i am here, where i belong, be prepared to cower down i fear of my intellectual might, for when Pragash is in economics, all is well!!!!!\""
    "But all was not well"
    "As usual, the first class was underprepared with no content, so i guess it's time for a kahoot!"
    $ game.kahoot = 0
    call econ1kahoot1
    "Score is [game.kahoot]"
    jump dead

label econ1kahoot1:
    $ time = 15
    $ timer_range = 15
    $ timer_jump = 'econ1kahoot1slow'
    $ playmusic("kahoot.ogg")
    show screen countdown
    "Which country has the longest uninterrupted economic growth?"
    menu:
        "Australia":
            $ stopmusic()
            hide screen countdown
            "Correct"
            if time > 5:
                $ game.gain("kahoot", 1)
            else:
                $ game.gain("kahoot", 2)
            return
        "US":
            $ stopmusic()
            hide screen countdown
            "Wrong"
            return
        "China":
            $ stopmusic()
            hide screen countdown
            "Wrong"
            return
        "Uganda":
            $ stopmusic()
            hide screen countdown
            "Wrong"
            return

label econ1kahoot1slow1:
    sze "\"Fuck im too slow\""
    return
