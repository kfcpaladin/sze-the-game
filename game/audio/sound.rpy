# Used to configure the audio settings

python early:
    
    audioDir = {
        "folder": "audio",
        "subfolders": [
            "music", 
            "sfx"
        ],
        "default": "audio_default.ogg",
    }
    audioCache = {}

    """
        Play and stop music/sfx files
    """
    def playmusic(filename, **options):
        if not checkIfDefaultAudio(filename):
            renpy.music.play(loadAudio(filename), channel="music", **options)

    def playsfx(filename, loop=False, **options):
        if not checkIfDefaultAudio(filename):
            renpy.music.play(loadAudio(filename), channel="sound", loop=loop, **options)

    def stopmusic(channel="music"):
        renpy.music.stop(channel=channel)

    def stopsfx(channel="sound"):
        renpy.music.stop(channel=channel)

    """
        Give warning if audio could not be loaded
    """
    def checkIfDefaultAudio(filename):
        filepath = loadAudio(filename)
        if filepath == "{0}/{1}".format(audioDir["folder"], audioDir["default"]):
            renpy.music.play(filepath, channel="sound", loop=False)
            popup("{0} is not a valid music file".format(filename))
            return True
        else:
            return False
        

    """
        Attempts to load audio from all folders, before defaulting to default sound
    """
    import os.path
    def loadAudio(filename):
        if filename in audioCache:
            return audioCache[filename]
        for folder in audioDir["subfolders"]:
            filepath = "{0}/{1}/{2}".format(audioDir["folder"], folder, filename)
            if os.path.exists("game/{0}".format(filepath)):
                audioCache[filename] = filepath
                return filepath
        filepath = "{0}/{1}".format(audioDir["folder"], audioDir["default"])
        audioCache[filename] = filepath
        return filepath
        
init python:
    ###########################################
    # Audio
    ## Sounds that are used when button and imagemaps are clicked.
    style.button.activate_sound = loadAudio("button_select.ogg")
    style.imagemap.activate_sound = loadAudio("button_select.ogg")
    ## Sounds that are used when entering and exiting the game menu.
    config.enter_sound = loadAudio("button_select.ogg")
    config.exit_sound = loadAudio("button_select.ogg")
    ## A sample sound that can be played to check the sound volume.
    config.sample_sound = loadAudio("button_select.ogg")
    ## Music that is played while the user is at the main menu.
    config.main_menu_music = loadAudio("p3IwatodaiDorm.ogg")