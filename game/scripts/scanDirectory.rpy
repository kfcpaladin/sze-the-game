init -2 python:

    # scanDirectory will determine all subfolders in a folder, and then store all
    # images inside a cache, so that they can be accessed through filenames
    # This is used for images and audio files, so that they can all be preloaded before
    # game starts, and accessed for debugging
    # Also this can also reveal conflicts in filenames
    # config = {
    #     "folder": ...,
    #     "subfolders": [],
    #     "default": ...,
    # }
    # cache = {}
    # gameDir = all sources and assets
    def scanDirectory(config, cache, gameDir="game"):
        directory = os.path.join(gameDir, config["folder"])
        for subfolder in os.listdir(directory):
            subfolderPath = os.path.join(directory, subfolder)
            if os.path.isdir(subfolderPath):
                config["subfolders"].append(subfolder)
                scanSubFolder(subfolderPath, cache, gameDir)

    # This will scan a subfolder, and add each file in it to the 
    # specified cache,
    # cache = {
    #    "filename": "filepath",
    # }
    def scanSubFolder(subfolderPath, cache, gameDir):
        for file in os.listdir(subfolderPath):
            if file[0] == ".":
                continue
            filePath = os.path.join(subfolderPath, file)
            if os.path.isfile(filePath):
                if file in cache:
                    raise IOError("{0} is conflicting with existing file {1}".format(filePath, cache[file]))
                else:
                    # remove gameDirectory prefix since renpy scans in game/ by default
                    cache[file] = removePrefix(filePath, gameDir+"/") 

    # remove prefix from a string
    def removePrefix(string, prefix):
        if string.startswith(prefix):
            return string[len(prefix):]
        return string  # or whatever
