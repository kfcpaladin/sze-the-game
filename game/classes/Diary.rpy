python early:
    class Diary:
        def __init__(self, screenNames):
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

    