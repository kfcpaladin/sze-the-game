# INTRODUCTION

label start:
    if config.developer:
        $ logDefaultCache() # for debugging improperly read files
    $ autosave()
    image blank = im.Recolor(loadImage("bg_arthur.png"), 255, 255, 255, 0)
    scene bg disclaimer
    if config.developer and not game.hasDiary:
        $ game.hasDiary = True
        $ game.diaryIntro = True
        "As a developer you gain access to the diary immediately"
        "Go to /game/scripts/options.rpy, and make config.developer = false to remove this"
    if game.hasDiary:
        show screen float_menu
    show screen gameLoop
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
    jump schoolday1
