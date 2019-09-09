# Used to configure the audio settings
init -1 python:
    audioDir = {
        "folder": "assets/audio",
        "default": "audio_default.ogg",
    }
    audioCache = {}
    musicHistory = []
    
    scanDirectory(audioDir, audioCache) # located in scripts/scanDirectory.rpy

    """
        Play and stop music/sfx files
    """
    def playmusic(filename, **options):
        if not filename:    # if None was given (no previous music)
            return
        if not checkIfDefaultAudio(filename):
            musicHistory.append(filename)
            renpy.music.play(loadAudio(filename), channel="music", **options)

    def playsfx(filename, loop=False, **options):
        if not filename:
            return
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
        defaultAudio = loadAudio(audioDir["default"])
        if loadAudio(filename) == defaultAudio:
            renpy.music.play(defaultAudio, channel="sound", loop=False)
            popup("{0} is not a valid audio file".format(filename))
            return True
        else:
            return False
    
    """
        Load index from music history
    """
    def getMusicHistory(index):
        filename = None
        try:
            filename = musicHistory[index]
        except IndexError:
            pass
        return filename
        

    """
        Attempts to load audio from all folders, before defaulting to default sound
    """
    import os.path
    def loadAudio(filename):
        if filename in audioCache:
            return audioCache[filename]
        # failed to get file (doesnt exist), try get default
        try:
            return audioCache[audioDir["default"]]
        # if couldnt load file and default, error
        except KeyError:
            errorString = "Could not load default: {0}, for missing file {1}"
            raise IOError(errorString.format(audioDir["default"], filename))
    
    """
        arbituary sorting function to distinguish whether an 
        audio file is suitable for the relevant function
    """
    def sortAudioFile(filepath, audioFunction, audioFolder=audioDir["folder"]):
        audioPaths = {
            playmusic: "music",
            playsfx: "sfx",
        }
        for function, subfolder in audioPaths.iteritems():
            if audioFunction is function and filepath.startswith(os.path.join(audioFolder, subfolder).replace("\\", "/")):
                return True
        return False

# Default menu and gui sounds
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
