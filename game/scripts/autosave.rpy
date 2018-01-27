init python:
    def autosave():
        popupList.add({
            "text": "Autosaving",
            "icon": loadImage("icon_save.png"),
            "colour": colour.rainbow,
        })
        renpy.save("autosave")
        