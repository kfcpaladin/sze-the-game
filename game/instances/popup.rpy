init python:
    popupList = PopUp()
    def popup(messages):
        popupList.add(messages)

    def autoSavePopup():
        popupList.add({
            "text": "Autosaving",
            "icon": loadImage("icon_save.png"),
        })