init -2 python:
    import os
    """
        scanDirectory will determine all subfolders in a folder, and then store all
        images inside a cache, so that they can be accessed through filenames
        This is used for images and audio files, so that they can all be preloaded before
        game starts, and accessed for debugging
        Also this can also reveal conflicts in filenames
        config = {
            "folder": ...,
            "subfolders": [],
            "default": ...,
        }
        cache = {}
        gameDir = all sources and assets
    """
    def scanDirectory(config, cache, gameDir=renpy.config.gamedir):
        directory = os.path.join(gameDir, config["folder"])
        if not os.path.isdir(directory):
            raise IOError("\"{0}\" is not a valid directory".format(directory))
        # start scanning recursively
        scanSubFolder(directory, cache, gameDir)


    """
        This will scan a subfolder, and add each file in it to the 
        specified cache,
        cache = {
        "filename": "filepath",
        }
    """
    def scanSubFolder(subfolderPath, cache, gameDir):
        for filename in os.listdir(subfolderPath):
            if filename[0] == ".":
                continue
            filepath = os.path.join(subfolderPath, filename)
            # if a file, add to cache
            if os.path.isfile(filepath):
                if filename in cache:
                    raise IOError("{0} is conflicting with existing file {1}".format(filepath, cache[file]))
                else:
                    # for windows replace "\\" to "/"
                    filepath = filepath.replace(gameDir, "")
                    filepath = filepath.replace("\\", "/")
                    # remove gameDirectory prefix since renpy scans in game/ by default
                    cache[filename] = removePrefix(filepath, "/")
            # recursively scan each folder
            elif os.path.isdir(filepath):
                scanSubFolder(filepath, cache, gameDir)

    # remove prefix from a string
    def removePrefix(string, prefix):
        if string.startswith(prefix):
            return string[len(prefix):]
        return string  # or whatever

    """
        This will sort, format and print a fileCache dictionary into console
    """
    def readCache(cache):
        sortedFileList = sorted(cache)
        for file in sortedFileList:
            filepath = cache[file]
            # give a warning symbol if file could not be loaded
            warning = ""
            for config in (audioDir, imageDir):
                if filepath == os.path.join(config["folder"], config["default"]):
                    warning = " ==> "
            # print filenames and its path
            print "{0}{1}: {2}".format(warning, file, filepath)

    """
        Log the cache during initialisation
    """
    def logCache(filename, cacheDict):
        logfile = open(os.path.join(renpy.config.basedir, filename), "w")
        for name, cache in cacheDict.iteritems():
            logfile.write(">>> Reading {0}\n".format(name))
            sortedFileList = sorted(cache)
            for file in sortedFileList:
                filepath = cache[file]
                # give a warning symbol if file could not be loaded
                warning = ""
                for config in (audioDir, imageDir):
                    if filepath == os.path.join(config["folder"], config["default"]):
                        warning = " ==> "
                # print filenames and its path
                logfile.write("{0}{1}: {2}\n".format(warning, file, filepath))
            logfile.write("\n")

init python:
    def logDefaultCache():
        logCache(
            "fileCacheStatus.log",
            {
                "images": imageCache,
                "audio": audioCache,
            }
        )

    if config.developer:
        logDefaultCache()
