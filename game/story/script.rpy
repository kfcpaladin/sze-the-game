# INTRODUCTION

label start:
# list of areas: lkilgour, uquad, lquad, hall, cohen, quad, wilkins, place, bridge, fortstreet, carpark, bcourts, currycourts, oval, valley, food, gym, library, rquad, kilgour, rowe
    call _test_label
    $ renpy.say(centered, "Successful return on first pass")
    call _test_label
    $ renpy.say(centered, "Successful return on second pass")
    call _test_label
    $ renpy.say(centered, "Successful return on third pass")
    $ renpy.save("autosave")
    scene bg disclaimer
    with fade
    pause
    scene black
    with fade
    scene bg intro
    with fade
    pause
    scene black
    with fade
    "The Year is 2015"
    "It is the first day of school and you do not look forward to another miserable year of Fort Street."
    "But nevertheless, you pack your bags, and get ready, resigned to another year of mediocrity."
    stop music 
    sze "I had always loved her, since she first graced my eyes in Year 7."
    show bg field
    with fade
    play music "Herbert von Karajan -Intermezzo Sinfonico- Cavalleria Rusticana.ogg"
    sze "Her name is Serena, a name which evokes images of clear, running brooks, and endless fields of wildflower meadows"
    hide bg field
    with dissolve
    show bg parisafremov
    with fade
    sze "Or perhaps it conjures an image of quaint Parisian cafes at night"
    sze "beside a rose garden in fragrant bloom, with the moon and stars out in full, and Mascagni's Cavalleria Rusticana: Intermezzo of Act 1 played softly in the background"
    sze "But for now, her name wrings out nought but sadness. More sadness than another year of school."
    jump schoolday1

label _test_label:
    $ renpy.say(centered, "Called to test label")
    sze "This is a test label"
    sze "It will be used to guage wether the call back works properly"
    return
