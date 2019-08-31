init python:
    def autosave():
        popups.add(Popup(
            message="Autosaving",
            colour=colour.rainbow,
            icon=loadImage("icon_save.png")
        ))
        renpy.save("autosave")
        