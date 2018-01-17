# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
init -100 python:
    imageDir = {
        "folders": [
            "backgrounds",
            "characterImages",
            "items",
            "icons",
            "screenBackgrounds",
            "screenIcons",
        ],
        "default": "default.png",
    }

    imageCache = {}

    import os.path
    def loadImage(filename):
        if filename is None:
            return None
        if filename in imageCache:
            return imageCache[filename]
        for folder in imageDir["folders"]:
            if os.path.exists("game/images/{0}/{1}".format(folder, filename)):
                filepath = "{0}/{1}".format(folder, filename)
                imageCache[filename] = filepath
                return filepath
        imageCache[filename] = imageDir["default"]
        return imageDir["default"]



image bg disclaimer =   loadImage("disclaimer.png")
image bg intro =        loadImage("arthur.jpg")
image bg school =       loadImage("memorial_hall.jpg")
image bg physclass =    loadImage("physclass.png")
image bg principaldoor =loadImage("principalofficedoor.jpg")
image bg principaloffice = loadImage("principaloffice.jpg")
image bg workshop =     loadImage("Workshop.jpg")
image bg hall =         loadImage("hall.jpg")
image bg hallentrance = loadImage("hallentrance.jpg")
image bg schoolfront =  loadImage("wilkins_side.jpg")
image bg rowecorridor = loadImage("fortrowecorridor.jpg")
image bg dream =        loadImage("eoarchean.jpg")
image bg ded =          loadImage("szeceded.jpg")
image bg field =        loadImage("fields_by_applesin_mod.jpg")
image bg parisafremov = loadImage("parisafremov.jpg")
image bg norton =       loadImage("NortonSt.png")
image bg toilet =       loadImage("toilet.png")
image bg d_workshop =   loadImage("Workshopdark.jpg")
image bg dreamtree =    loadImage("dreamtree.png")
image bg economics =    loadImage("economics.png")

#not sure if that's legit spelling, plz check
style window:
    left_padding 150
image side arthur =     loadImage("arthurside.png")
image willis normal =   loadImage("willis1.png")
image side willis =     loadImage("willisside1.png")
image rusali normal =   loadImage("rusali.png")
image side rusali =     loadImage("rusali_side.png")
image moxham happy =    loadImage("moxhamhappy.png")
image moxham unhappy =  loadImage("moxhamunhappy.png")
image side moxham =     loadImage("moxhamside.png")
image grant normal =    loadImage("grant.png")
image pragash normal =  loadImage("pragashnormal.png")
image pragash shocked = loadImage("pragash2.png")
image yang normal =     loadImage("yang1.png")
image chao normal =     loadImage("chao2.png")
image chao happy =      loadImage("chaohappy.png")
image side pragash =    loadImage("pragash.png")
image side bill =       loadImage("billthecleaner.png")
image side dean =       loadImage("deanside.png")
image side chao =       loadImage("chaoport.png")
image le calculetor =   loadImage("calculetor.png")
image side le =         loadImage("lecalc.png")
image side yin =        loadImage("willyin.png")
image side richard =    loadImage("rick.png")
image side roy =        loadImage("RRRROOOOOOOYYYYYYYYYboi.png")
image side gary =       loadImage("garry.png")
image side todd =       loadImage("toddside.png")
image side derek =      loadImage("derkiederkside.png")
