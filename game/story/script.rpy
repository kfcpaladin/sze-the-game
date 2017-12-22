# INTRODUCTION

label start:
# list of areas: lkilgour, uquad, lquad, hall, cohen, quad, wilkins, place, bridge, fortstreet, carpark, bcourts, currycourts, oval, valley, food, gym, library, rquad, kilgour, rowe
    $ renpy.save("autosave")
    show screen diary_button
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
    $ playmusic("Herbert von Karajan -Intermezzo Sinfonico- Cavalleria Rusticana.ogg")
    sze "Her name is Serena, a name which evokes images of clear, running brooks, and endless fields of wildflower meadows"
    hide bg field
    with dissolve
    show bg parisafremov
    with fade
    sze "Or perhaps it conjures an image of quaint Parisian cafes at night"
    sze "beside a rose garden in fragrant bloom, with the moon and stars out in full, and Mascagni's Cavalleria Rusticana: Intermezzo of Act 1 played softly in the background"
    sze "But for now, her name wrings out nought but sadness. More sadness than another year of school."
    show screen bag_button
    jump schoolday1
