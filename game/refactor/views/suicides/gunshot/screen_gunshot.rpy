screen kmsGun(controller=view_controllers.suicides.gunshot):
    modal True
    if controller.closed:
        timer 0.05:
            repeat False
            action [Function(controller.reset)]
    add controller
    if controller.closed:
        timer 0.05:
            repeat False
            action [
                Hide("kmsGun", Fade(2.5, 0.0, 1.0)),
                Show("deathFade"),
                Function(playsfx, "vpunch.ogg"),
                Function(game.set, "suicideCount", game.suicideCount + 1)
            ]
