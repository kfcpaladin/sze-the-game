init python:
    def autosave():
        popups.add(Popup(
            message="Autosaving",
            colour=themes.default.rainbow,
            icon=loadImage("icon_save.png")
        ))
        renpy.save("autosave")
        