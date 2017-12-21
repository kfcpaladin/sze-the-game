# Used to configure the audio settings

python early:
    # Music directory
    musicdir = "./music/"

    def playmusic(filename, channel="music", **options):
        if type(filename) not in [str, basestring, unicode]:
            raise TypeError("Music filename needs to be a string, not {0}".format(type(filename)))
        renpy.music.play((musicdir + filename), channel=channel, **options)

    def stopmusic():
        renpy.music.stop()

    # SFX directory
    sfxdir = "./sfx/"

    def playsfx(filename, channel="sound", loop=False, **options):
        if type(filename) not in [str, basestring, unicode]:
            raise TypeError("SFX filename needs to be a string, not {0}".format(type(filename)))
        renpy.music.play((sfxdir + filename), channel=channel, loop=loop, **options)


init -1 python hide:
    ###########################################
    # Audio
    
    ## Sounds that are used when button and imagemaps are clicked.
    style.button.activate_sound = sfxdir + "8d82b5_Final_Fantasy_XI_Menu_Selection_Sound_Effect.ogg"
    style.imagemap.activate_sound = sfxdir + "8d82b5_Final_Fantasy_XI_Menu_Selection_Sound_Effect.ogg"

    ## Sounds that are used when entering and exiting the game menu.
    config.enter_sound = sfxdir + "8d82b5_Final_Fantasy_XI_Menu_Selection_Sound_Effect.ogg"
    config.exit_sound = sfxdir + "8d82b5_Final_Fantasy_XI_Menu_Selection_Sound_Effect.ogg"

    ## A sample sound that can be played to check the sound volume.
    config.sample_sound = sfxdir + "8d82b5_Final_Fantasy_XI_Menu_Selection_Sound_Effect.ogg"

    ## Music that is played while the user is at the main menu.
    config.main_menu_music = musicdir + "p3IwatodaiDorm.ogg"
