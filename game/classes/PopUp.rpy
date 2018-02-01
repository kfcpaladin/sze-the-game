# Used to manage popups
init -10 python:
    class PopUp:
        def __init__(self):
            self.popupList = []
            self.stringType = (str, unicode, basestring)
            self.defaultMessage = {
                "icon": None,
                "time_remain": 2,
                "colour": None,
            }

        # adds a message to a list
        def add(self, messages):
            # convert various types into a suitable format
            if type(messages) in self.stringType:
                if not self.checkInList(messages):
                    self.popupList.append(self.makeMessage(messages))
            # dict to proper dict
            elif type(messages) is dict:
                if self.checkMessage(messages):
                    self.popupList.append(messages)
            # add list of messages recursively
            elif type(messages) is list:
                for message in messages:
                    self.add(message)
            # if no other type
            else:
                raise TypeError("Expected str, dict, list for popup, not {0}".format(type(messages)))
            # update screen for each new message
            renpy.show_screen("popup", self)

        # checks if a message dict is of right format
        def checkMessage(self, message):
            if "text" not in message: 
                raise KeyError("Popup dict must have text component")
            # if dict already in list, skip
            if self.checkInList(message["text"]):
                return False
            # add missing params
            for key, defaultValue in self.defaultMessage.iteritems():
                if key not in message: 
                    message[key] = defaultValue
            # make newest message last longer than last item
            lastTime = self.getLastTime()
            if lastTime >= 1.5:
                message["time_remain"] = lastTime + 0.5
            else:
                message["time_remain"] += self.getLastTime()
            return True

        # make message from pure text
        def makeMessage(self, text, icon=None):
            message = {
                "text": text,
                "icon": icon,
                "time_remain": 2,
            }
            self.checkMessage(message)
            return message

        # get time of oldest item in list
        def getLastTime(self):
            if len(self.popupList) > 0:
                return self.popupList[-1]["time_remain"]
            else:
                return 1

        # reduce time remaining for all popups, and remove those that have expired
        def update(self, speed):
            removedPopups = []
            for popup in self.popupList:
                popup["time_remain"] -= speed
                if popup["time_remain"] <= 0:
                    removedPopups.append(popup)
            for popup in removedPopups:
                self.popupList.remove(popup)

        # check if a message is already in the list
        def checkInList(self, message):
            for popup in self.popupList:
                if popup["text"] == message:
                    return True
            return False

        # get total number of popups
        def getTotal(self):
            return len(self.popupList)

        # clear popup list
        def clear(self):
            self.popupList = []