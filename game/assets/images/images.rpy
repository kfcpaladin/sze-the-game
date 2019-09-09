# This is the image loading system
# You use loadImage(...) to load the image, providing the name of the file.
# You do not have to specify directory, but the directory must be present in
# imageDir["subfolders"].
# If an image could not be loaded, it will default to the default image, specified
# in imageDir["default"]
init -1 python:
    imageDir = {
        "folder" : "assets/images",
        "default": "image_default.png",
    }
    imageCache = {}
    scanDirectory(imageDir, imageCache) # located in scripts/scanDirectory.rpy

    import os.path
    def loadImage(filename):
        # None filenames are allowed
        if filename is None:
            return None
        # try get image
        if filename in imageCache:
            return imageCache[filename]
        # try get default
        try:
            return imageCache[imageDir["default"]]
        except KeyError:
            errorString = "Could not load default: {0}, for missing file {1}"
            raise IOError(errorString.format(imageDir["default"], filename))

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg black =        Solid(PrimaryColours.BLACK)
image bg d_workshop =   loadImage("bg_Workshopdark.png")
image bg ded =          loadImage("bg_szeceded.png")
image bg disclaimer =   loadImage("bg_disclaimer.png")
image bg dream =        loadImage("bg_eoarchean.png")
image bg dreamtree =    loadImage("bg_dreamtree.png")
image bg economics =    loadImage("bg_economics.png")
image bg english =      loadImage("bg_english.png")
image bg field =        loadImage("bg_fields_by_applesin_mod.png")
image bg hall =         loadImage("bg_hall.png")
image bg hallentrance = loadImage("bg_hallentrance.png")
image bg intro =        loadImage("bg_arthur.png")
image bg loadingdock =  loadImage("bg_strathloadingdock.png")
image bg loadingdocksign = loadImage("bg_strathloadingdocksign.png")
image bg norton =       loadImage("bg_NortonSt.png")
image bg paris =        loadImage("bg_aneveninginparislushpin.jpg")
image bg physclass =    loadImage("bg_physclass.png")
image bg principaldoor =loadImage("bg_principalofficedoor.png")
image bg principaloffice = loadImage("bg_principaloffice.png")
image bg rowecorridor = loadImage("bg_fortrowecorridor.png")
image bg school =       loadImage("bg_memorial_hall.png")
image bg schoolfront =  loadImage("bg_wilkins_side.png")
image bg toilet =       loadImage("bg_toilet.png")
image bg workshop =     loadImage("bg_Workshop.png")
image bg bdr1night =    loadImage("bg_starterbedroom1.jpg")
image bg bdr1day =      loadImage("bg_starterbedroom2.jpg")
image bg bdr1dwndsk =   loadImage("bg_starterbedroom3.jpg")
image bg classdoor =    loadImage("bg_outsideclass.jpg")
image bg kilgourup =    loadImage("bg_rayretireupperkilgour.jpg")

# minigame background
image bg pong = loadImage("screen_bg_pong.png")

#not sure if that's legit spelling, plz check
style window:
    left_padding 150
image chao happy =      loadImage("char_chaohappy.png")
image chao normal =     loadImage("char_chao2.png")
image grant normal =    loadImage("char_grant.png")
image le calculetor =   loadImage("char_calculetor.png")
image moxham happy =    loadImage("char_moxhamhappy.png")
image moxham unhappy =  loadImage("char_moxhamunhappy.png")
image pragash normal =  loadImage("char_pragashnormal.png")
image pragash shocked = loadImage("char_pragash2.png")
image rusali normal =   loadImage("char_rusali.png")
image side arthur =     loadImage("char_arthurside.png")
image side bill =       loadImage("char_billthecleaner.png")
image side chao =       loadImage("char_chaoport.png")
image side dean =       loadImage("char_deanside.png")
image side derek =      loadImage("char_derkiederkside.png")
image side gary =       loadImage("char_garry.png")
image side le =         loadImage("char_lecalc.png")
image side moxham =     loadImage("char_moxhamside.png")
image side pragash =    loadImage("char_pragash.png")
image side richard =    loadImage("char_rick.png")
image side rina =       loadImage("char_rina.png")
image side roy =        loadImage("char_RRRROOOOOOOYYYYYYYYYboi.png")
image side rusali =     loadImage("char_rusali_side.png")
image side todd =       loadImage("char_toddside.png")
image side willis =     loadImage("char_willisside1.png")
image side yin =        loadImage("char_willyin.png")
image todd normal =     loadImage("char_toddside.png") # placeholder?
image willis normal =   loadImage("char_willis1.png")
image yang normal =     loadImage("char_yang1.png")
image sze normal =      loadImage("char_sze1.png")
