# INTRODUCTION

label start:
# list of areas: lkilgour, uquad, lquad, hall, cohen, quad, wilkins, place, bridge, fortstreet, carpark, bcourts, currycourts, oval, valley, food, gym, library, rquad, kilgour, rowe
    $ allowedareas = {"lkilgour", "uquad", "lquad", "hall", "cohen", "quad", "wilkins", "garden", "bridge", "fortstreet", "carpark", "bcourts", "currycourts", "oval", "valley", "food", "gym", "library", "rquad", "kilgour", "rowe"}
    $ kahootpoints = 0
    $ timer_range = 0
    $ timer_jump = 0
    $ moxcounter1 = 0
    $ moxcounter2 = 0
    $ intelligence = 0
    $ charm = 0
    $ strength = 0
    $ thirst = 0
    $ fort = 0
    $ strengthtutorial = False
    $ inteltutorial = False
    $ friendshiptutorial = False
    $ charmtutorial = False
    $ thirsttutorial = False
    $ forttutorial = False
    $ rinfriendship = 0
    $ kokfriendship = 0
    $ flufriendship = 0
    $ rusfriendship = 3
    $ prafriendship = 0
    $ deafriendship = 0
    $ wilfriendship = 40
    $ chafriendship = 0
    $ grafriendship = 0
    $ moxfriendship = 0
    $ dikfriendship = 0
    $ drkfriendship = 0
    $ jitfriendship = 5
    $ royfriendship = 0
    $ leefriendship = 0
    $ butfriendship = 0
    $ dngfriendship = 0
    $ timetravelcount = 0
    $ metderek = False
    $ phys1p3p1chaopissed = False
    $ yangrant1_2eingutidee = False
    $ quest1electionpromise = False
    $ quest1electionpromise1 = False
    $ discovernorton = False
    $ quest2jintiandeliveryservicecofounder = False
    
    $ ball = Item("ball", "bouncy thing", "strength", "images/ball.png")
    $ axe = Item("axe", "weaponz", "strength", "images/axe.png")
    $ money = Item("monies", "cash monies wads", "charisma", "images/bag.png")
    $ fireaxe = Item("fireaxe", "weaponz", "strength", "images/axe.png")
    $ calc = Item("calculator", "smarts + 1", "smart", "images/calc1.png")
    $ inventory = Inventory("Bag", 10, False)
    #$ inventory = Inventory("Locker", 10)
    $ inventory.add(ball, 1)
    $ inventory.add(axe, 1)
    $ inventory.add(money, 1)
    $ inventory.add(money, 1)
    $ inventory.add(fireaxe, 1)
    $ inventory.add(calc, 1)
    scene black
    with fade
    scene bg intro
    with fade
    pause
    show screen bag_button
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
