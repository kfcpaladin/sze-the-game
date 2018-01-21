init python:
    import pygame
    from copy import deepcopy
    # valley easter egg with serena
    def easterEggValley(friend):
        if not isinstance(friend, Friend):
            raise TypeError("Expected a Friend for easterEggValley, instead got {0}".format(type(friend)))
        while True:
            try:
                total = renpy.input("How friendly do you want to be with {0}?".format(friend.name))
                total = int(total)
            except:
                continue
            else:
                if type(total) not in (int, float):
                    continue
                break
        if(total >= 0):
            friend.gain("friendship", total)
        else:
            friend.loss("friendship", -total)

    # unlock dildo
    def konamiCodeUnlock():
        playsfx("xbox.ogg")
        popup("Unlocked item: Neo Armstrong")
        bag.add(deepcopy(unlockableItems["neo armstrong"]))
        ui.remove(konamiCode)

    konamiCode = CodeSequence(
        sequence=(
            pygame.K_UP, pygame.K_UP, pygame.K_DOWN, pygame.K_DOWN, 
            pygame.K_LEFT, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_RIGHT
        ),
        unlock=konamiCodeUnlock
    )

    # unlock kirby suit
    def kirbyUnlock():
        playsfx("xbox.ogg")
        popup("Unlocked item: Michael Kirby's Suit")
        bag.add(deepcopy(unlockableItems["god"]))
        ui.remove(kirbyCode)

    kirbyCode = CodeSequence(
        sequence=(
            pygame.K_UP, pygame.K_DOWN, pygame.K_UP, pygame.K_DOWN, 
            pygame.K_LEFT, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_RIGHT
        ),
        unlock=kirbyUnlock 
    )

    # unlock developer mode
    def developerUnlock():
        playsfx("xbox.ogg")
        popup({
            "text": "Unlocked developer mode",
            "icon": loadImage("icon_rina.png"),
        })
        config.developer = True
        game.diaryIntro = True
        game.hasDiary = True
        if "diary_developer" not in diary.screenNames:
            diary.screenNames.insert(0, "diary_developer")
        renpy.hide_screen("float_menu")
        renpy.show_screen("float_menu")
        ui.remove(developerCode)

    developerCode = CodeSequence(
        sequence=[getattr(pygame, "K_{0}".format(char)) for char in "godmode"],
        unlock=developerUnlock,
    )

    # this adds all the key sequences to the global ui which is updated by
    # renpys main game loop, via "def event(...)" method
    def addKeySequences():
        ui.add(konamiCode)  
        ui.add(kirbyCode)
        ui.add(developerCode)

    # can only add ui when other ui elements are added, not during 
    # game initialisation
    config.overlay_functions.append(addKeySequences)

