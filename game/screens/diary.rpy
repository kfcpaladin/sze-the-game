###########################################################################################################################################################
screen diary_button(diary=diary):
    textbutton "Open Diary":
        action [
            ShowMenu(diary.getCurrentPage()), 
        ] 
        align (0.84, 0.04)

# screen diary_nav:
#     mousearea:
#         area (400, 0, 566, 100)
#         hovered [
#             Show("diary_nav_buttons")
#         ]
#         unhovered [
#             Hide("diary_nav_buttons")
#         ]

# navigation for all diary pages
screen diary_nav:
    hbox xcenter 1366/2:
        for index, screenName in enumerate(diary.screenNames):
            textbutton _(str(index)):
                action [
                    ShowMenu(diary.getPage(index)),
                    Hide(diary.getCurrentPage()),
                    Hide("diary_nav_buttons"),
                    Function(diary.setPage, index),
                ]                    

# diary title
screen diary_title(title="Undefined"):
    frame:
        area (0, 0, 500, 50)
        text title: 
            size 45
            xoffset 30
            yoffset 10
            font "DejaVuSans.ttf"


init -1 python:
    class Diary:
        def __init__(self, *screenNames):
            self.screenNames = screenNames
            self.currentPage = 0
        
        def getCurrentPage(self):
            return self.screenNames[self.currentPage]
        
        def setPage(self, index):
            index = self.constrain(index)
            self.currentPage = index

        def getPage(self, index):
            index = self.constrain(index)
            return self.screenNames[index]

        def constrain(self, index):
            if index >= len(self.screenNames):
                index = len(self.screenNames)-1
            elif index < 0:
                index = 0
            return index

    diary = Diary(
        "developerScreen",
        "bag_view",
        "questscreen",
        "achievementscreen",
        "statsscreen",
        "roadmap"
    )
