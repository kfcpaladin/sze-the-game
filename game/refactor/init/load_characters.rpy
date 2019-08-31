init python:
    from refactor.models.characters import MainCharacter
    # Declare characters used by this game.
    sze = MainCharacter('Sze', color="#FCFCFC", image="arthur")

    friendList = []
    # Define friends
    ale = Friend('Le Calculetor', friendship=0, color="#FFFFFF", image="le", icon=loadImage("icon_anthonyle.png"))
    bil = Friend('Bill the Cleaner', friendship=0, color="747D7D", image="bill", icon=loadImage("icon_billthecleaner.png"))
    but = Friend('Aradhya',      friendship=0, color="#FFFFFF", image="aradhya")
    cha = Friend('Chao',         friendship=0, color="#FFFFFF", image="chao",    icon=loadImage("icon_chao.png"))
    dea = Friend('Dean',         friendship=0, color="#FFFFFF", image="dean",    icon=loadImage("icon_dean.png"))
    dik = Friend('Richard',      friendship=0, color="#FFFFFF", image="richard", icon=loadImage("icon_richard.png"))
    dng = Friend('Steven',       friendship=0, color="#FFFFFF", image="steven")
    drk = Friend('Derek',        friendship=0, color="#FFFFFF", image="derek",   icon=loadImage("icon_derek.png"))
    flu = Friend('FLUITSIE',     friendship=0, color="#FFFFFF", image="fluitsma")
    gra = Friend('GRANT',        friendship=0, color="#FFFFFF", image="grant",   icon=loadImage("icon_grant.png"))
    jit = Friend('Gary',         friendship=5, color="#FFFFFF", image="gary",    icon=loadImage("icon_gary.png"))
    kok = Friend('Willis',       friendship=-10, color="#666666", image="willis",  icon=loadImage("icon_willis.png"))
    lee = Friend('Andrew',       friendship=0, color="#FFFFFF", image="andrew")
    mox = Friend('MOXHAM',       friendship=0, color="#FFFFFF", image="moxham",  icon=loadImage("icon_moxham.png"))
    pra = Friend('Pragash',      friendship=0, color="#FFFFFF", image="pragash", icon=loadImage("icon_pragash.png"))
    rin = Friend('Rina',         friendship=0, color="#007408", image="serena")  #icon=loadImage("icon_rina.png"))
    roy = Friend('Roy',          friendship=0, color="#FFFFFF", image="roy",     icon=loadImage("icon_roy.png"))
    rus = Friend('Rusali',       friendship=0, color="#FFFFFF", image="rusali",  icon=loadImage("icon_rusali.png"))
    slm = Friend('Schlam',       friendship=0, color="#FFFFFF", image="shlam")
    tod = Friend('Todd Treoir',  friendship=0, color="#99ff99", image="todd",    icon=loadImage("icon_todd.png"))
    web = Friend('Dr. Webb',     friendship=0, color="#FFFFFF", image="webb")
    wil = Friend('Will Yin',     friendship=40, color="#ff0000",image="yin",     icon=loadImage("icon_willyin.png"))
    wiy = Friend('Will Yang',    friendship=40, color="#FFFFFF",image="will",    icon=loadImage("icon_willyang.png"))
    zhn = Friend('Will Zhong',    friendship=0, color="#FFFFFF",image="Zhong",    icon=loadImage("icon_willyang.png"))
