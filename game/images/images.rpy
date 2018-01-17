# This is the image loading system
# You use loadImage(...) to load the image, providing the name of the file.
# You do not have to specify directory, but the directory must be present in
# imageDir["subfolders"].
# If an image could not be loaded, it will default to the default image, specified
# in imageDir["default"]
init -100 python:
    imageDir = {
        "folder" : "images",
        "subfolders": [
            "achievementIcons",
            "backgrounds",
            "characterImages",
            "icons",
            "items",
            "questIcons",
            "screenBackgrounds",
            "suicideScreens",
        ],
        "default": "image_default.png",
    }

    imageCache = {}

    import os.path
    def loadImage(filename):
        if filename is None:
            return None
        if filename in imageCache:
            return imageCache[filename]
        for folder in imageDir["subfolders"]:
            filepath = "{0}/{1}/{2}".format(imageDir["folder"], folder, filename)
            if os.path.exists("game/{0}".format(filepath)):
                imageCache[filename] = filepath
                return filepath
        filepath = "{0}/{1}".format(imageDir["folder"], imageDir["default"])
        imageCache[filename] = filepath
        return filepath


# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg disclaimer =   loadImage("bg_disclaimer.png")
image bg intro =        loadImage("bg_arthur.jpg")
image bg school =       loadImage("bg_memorial_hall.jpg")
image bg physclass =    loadImage("bg_physclass.png")
image bg principaldoor =loadImage("bg_principalofficedoor.jpg")
image bg principaloffice = loadImage("bg_principaloffice.jpg")
image bg workshop =     loadImage("bg_Workshop.jpg")
image bg hall =         loadImage("bg_hall.jpg")
image bg hallentrance = loadImage("bg_hallentrance.jpg")
image bg schoolfront =  loadImage("bg_wilkins_side.jpg")
image bg rowecorridor = loadImage("bg_fortrowecorridor.jpg")
image bg dream =        loadImage("bg_eoarchean.jpg")
image bg ded =          loadImage("bg_szeceded.jpg")
image bg field =        loadImage("bg_fields_by_applesin_mod.jpg")
image bg parisafremov = loadImage("bg_parisafremov.jpg")
image bg norton =       loadImage("bg_NortonSt.png")
image bg toilet =       loadImage("bg_toilet.png")
image bg d_workshop =   loadImage("bg_Workshopdark.jpg")
image bg dreamtree =    loadImage("bg_dreamtree.png")
image bg economics =    loadImage("bg_economics.png")

#not sure if that's legit spelling, plz check
style window:
    left_padding 150
image side arthur =     loadImage("char_arthurside.png")
image willis normal =   loadImage("char_willis1.png")
image side willis =     loadImage("char_willisside1.png")
image rusali normal =   loadImage("char_rusali.png")
image side rusali =     loadImage("char_rusali_side.png")
image moxham happy =    loadImage("char_moxhamhappy.png")
image moxham unhappy =  loadImage("char_moxhamunhappy.png")
image side moxham =     loadImage("char_moxhamside.png")
image grant normal =    loadImage("char_grant.png")
image pragash normal =  loadImage("char_pragashnormal.png")
image pragash shocked = loadImage("char_pragash2.png")
image yang normal =     loadImage("char_yang1.png")
image chao normal =     loadImage("char_chao2.png")
image chao happy =      loadImage("char_chaohappy.png")
image side pragash =    loadImage("char_pragash.png")
image side bill =       loadImage("char_billthecleaner.png")
image side dean =       loadImage("char_deanside.png")
image side chao =       loadImage("char_chaoport.png")
image le calculetor =   loadImage("char_calculetor.png")
image side le =         loadImage("char_lecalc.png")
image side yin =        loadImage("char_willyin.png")
image side richard =    loadImage("char_rick.png")
image side roy =        loadImage("char_RRRROOOOOOOYYYYYYYYYboi.png")
image side gary =       loadImage("char_garry.png")
image side todd =       loadImage("char_toddside.png")
image side derek =      loadImage("char_derkiederkside.png")
