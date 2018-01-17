# Declare characters used by this game.
define sze = MainCharacter('Sze', color="#FCFCFC", image="arthur")
# Define friends
define ale = Friend('Le Calculetor', friendship=0, color="#FFFFFF", image="le", icon=loadImage("anthonyle.png"))
define bil = Friend('Bill the Cleaner', friendship=0, color="747D7D", image="bill", icon=loadImage("billthecleaner.png"))
define but = Friend('Aradhya',      friendship=0, color="#FFFFFF", image="aradhya")
define cha = Friend('Chao',         friendship=0, color="#FFFFFF", image="chao",    icon=loadImage("chao.png"))
define dea = Friend('Dean',         friendship=0, color="#FFFFFF", image="dean",    icon=loadImage("dean.png"))
define dik = Friend('Richard',      friendship=0, color="#FFFFFF", image="richard", icon=loadImage("richard.png"))
define dng = Friend('Steven',       friendship=0, color="#FFFFFF", image="steven")
define drk = Friend('Derek',        friendship=0, color="#FFFFFF", image="derek",   icon=loadImage("derek.png"))
define flu = Friend('FLUITSIE',     friendship=0, color="#FFFFFF", image="fluitsma")
define gra = Friend('GRANT',        friendship=0, color="#FFFFFF", image="grant",   icon=loadImage("grant.png"))
define jit = Friend('Gary',         friendship=5, color="#FFFFFF", image="gary",    icon=loadImage("gary.png"))
define kok = Friend('Willis',       friendship=0, color="#666666", image="willis",  icon=loadImage("willis.png"))
define lee = Friend('Andrew',       friendship=0, color="#FFFFFF", image="andrew")
define mox = Friend('MOXHAM',       friendship=0, color="#FFFFFF", image="moxham",  icon=loadImage("moxham.png"))
define pra = Friend('Pragash',      friendship=0, color="#FFFFFF", image="pragash", icon=loadImage("pragash.png"))
define rin = Friend('Rina',         friendship=0, color="#007408", image="serena")
define roy = Friend('Roy',          friendship=0, color="#FFFFFF", image="roy",     icon=loadImage("roy.jpg"))
define rus = Friend('Rusali',       friendship=0, color="#FFFFFF", image="rusali",  icon=loadImage("rusali.png"))
define slm = Friend('Schlam',       friendship=0, color="#FFFFFF", image="shlam")
define tod = Friend('Todd Treoir',  friendship=0, color="#99ff99", image="todd",    icon=loadImage("todd.png"))
define wil = Friend('Will Yin',     friendship=40, color="#ff0000",image="yin",     icon=loadImage("willyin.png"))
define wiy = Friend('Will Yang',    friendship=40, color="#FFFFFF",image="will",    icon=loadImage("willyang.png"))

init -1 python:
    friendList = []

