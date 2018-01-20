label dead:
    scene black
    $ stopmusic()
    $ playsfx("game_over.ogg")
    $ renpy.hide_screen("float_menu")
    sze "I dead"
    menu:
        "Revert to latest autosave":
            $ renpy.load("autosave")
            return
        "Return to start":
            # theoretically if you died like 5000 times, you will run out of ram and your pc is die.
            scene bg ded
            with fade
            $ playsfx("respawn.ogg")
            "The Lord of Light has granted me another chance..."
            $ playmusic("p3IwatodaiDorm.ogg")
            jump start

label deadrestart:
    scene bg ded
    $ stopmusic()
    $ playsfx("game_over.ogg")
    $ renpy.hide_screen("float_menu")
    sze "I dead"
    $ playmusic("p3IwatodaiDorm.ogg")    
    jump start

label actualded:
    scene black
    $ stopmusic()
    $ playsfx("game_over.ogg")
    $ renpy.hide_screen("float_menu")
    sze "I dead"
    return

# HSPs +3 strength, -1 intel
# fish and chips +2 intel
# pho +1 strength +1 intel +1 thirst
# pork rolls +2 charm
# vegan shite = +3 fort -1 strength -1 dikfriendship
