# INTRODUCTION

label start:
# list of areas: lkilgour, uquad, lquad, hall, cohen, quad, wilkins, place, bridge, fortstreet, carpark, bcourts, currycourts, oval, valley, food, gym, library, rquad, kilgour, rowe
    $ allowedareas = {"lkilgour", "uquad", "lquad", "hall", "cohen", "quad", "wilkins", "place", "bridge", "fortstreet", "carpark", "bcourts", "currycourts", "oval", "valley", "food", "gym", "library", "rquad", "kilgour", "rowe"}
    $ kahootpoints = 0
    $ timer_range = 0
    $ timer_jump = 0
    $ intelligence = 0
    $ moxcounter1 = 0
    $ moxcounter2 = 0
    $ charm = 0
    $ strength = 0
    $ strengthtutorial = False
    $ inteltutorial = False
    $ thirst = 0
    $ fort = 0
    $ friendshiptutorial = False
    $ charmtutorial = False
    $ thirsttutorial = False
    $ forttutorial = False
    $ timetravelcount = 0
    $ phys1p3p1chaopissed = False
    $ yangrant1_2eingutidee = False
    $ quest1electionpromise = False
    $ quest1electionpromise1 = False
    $ discovernorton = False
    $ quest2jintiandeliveryservicecofounder = False
    $ metderek = False
    
    scene bg disclaimer
    pause
    scene black
    with fade
    scene bg intro
    with fade
    pause
    # remove this these things to enable music later
    play music "Herbert von Karajan -Intermezzo Sinfonico- Cavalleria Rusticana.mp3"
    scene black
    with fade
    "The Year is 2015"
    "It is the first day of school and you do not look forward to another miserable year of Fort Street."
    "But nevertheless, you pack your bags, and get ready, resigned to another year of mediocrity."
    sze "I had always loved her, since she first graced my eyes in Year 7."
    show bg field
    with fade
    sze "Her name is Serena, a name which evokes images of clear, running brooks, and endless fields of wildflower meadows"
    hide bg field
    with dissolve
    show bg parisafremov
    with fade
    sze "Or perhaps it conjures an image of quaint Parisian cafes at night"
    sze "beside a rose garden in fragrant bloom, with the moon and stars out in full, and Mascagni's Cavalleria Rusticana: Intermezzo of Act 1 played softly in the background"
    sze "But for now, her name wrings out nought but sadness. More sadness than another year of school."
    jump schoolday1
