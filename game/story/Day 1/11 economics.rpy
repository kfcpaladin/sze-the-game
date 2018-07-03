label econ1:
    $ autosave()
    scene bg economics
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
    call econ1kahoot1
    call dead

label econ1kahoot1:
    call kahootGame(kahoot["econ1"], time_range=10)
    if _choice is not None:
        if _points > 0:
            "You got the answer correct"
            pra "This is very impressive Arthur"
            if _time_remain > 8:
                pra "Your performance was incredibly impressive"
                pra "But now that you have beaten me, I'm afraid that you are going to have to die"
            else:
                pra "I guess I win"
                sze "That was a fun game"
                pra "But since you were able to get the question right, I'm afraid you posed too much of a risk"
                sze "Wait what???"
                "???"
        else:
            "You got the answer incorrect"
            pra "Disappointing arthur"
            sze "Wait give me another change senpai"
            pra "I'm sorry, but I'm afraid I can't let you live anymore"
            sze "Wait, PLEASE NOOO.."
            "..."
    else:
        pra "A man who doesn't try will never succeed"
        sze "I forgot how to use a mouse"
        pra "That is irrelevant, your life is meaningless isnt it?"
        sze "I guess so?"
        pra "I'll spare you the trouble"