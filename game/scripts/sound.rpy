# Used to configure the audio settings

python early:
    # Define directory at start
    musicdir = "./music/"

    # Custom music function
    def playmusic(filename, **options):
        if type(filename) not in [str, basestring, unicode]:
            raise TypeError("Music filename needs to be a string, not {0}".format(type(filename)))
        try:
            directory = musicdir
        except:
            directory = ""
        renpy.music.play(directory + filename, **options)

    def stopmusic():
        renpy.music.stop()

init -1 python hide:
    ###########################################
    # Audio
    
    ## Sounds that are used when button and imagemaps are clicked.
    style.button.activate_sound = musicdir + "SFX/8d82b5_Final_Fantasy_XI_Menu_Selection_Sound_Effect.ogg"
    style.imagemap.activate_sound = musicdir + "SFX/8d82b5_Final_Fantasy_XI_Menu_Selection_Sound_Effect.ogg"

    ## Sounds that are used when entering and exiting the game menu.
    config.enter_sound = musicdir + "SFX/8d82b5_Final_Fantasy_XI_Menu_Selection_Sound_Effect.ogg"
    config.exit_sound = musicdir + "SFX/8d82b5_Final_Fantasy_XI_Menu_Selection_Sound_Effect.ogg"

    ## A sample sound that can be played to check the sound volume.
    config.sample_sound = musicdir + "SFX/8d82b5_Final_Fantasy_XI_Menu_Selection_Sound_Effect.ogg"

    ## Music that is played while the user is at the main menu.
    config.main_menu_music = musicdir + "p3IwatodaiDorm.ogg"