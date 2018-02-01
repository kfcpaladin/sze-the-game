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

    # add item to bag
    def unlockItem(item, bag):
        playsfx("xbox.ogg")
        popup({
            "text": "Unlocked item\n{0}".format(item.name),
            "icon": item.icon,
            "colour": colour.rainbow,
        })
        bag.add(item)

    # unlock dildo
    def konamiCodeUnlock():
        unlockItem(unlockableItems["neo armstrong"], bag)
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
        unlockItem(unlockableItems["god"], bag)
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
            "colour": colour.rainbow,
        })
        config.developer = True
        game.diaryIntro = True
        game.hasDiary = True
        if "diary_developer" not in diary.screenNames:
            diary.screenNames.insert(0, "diary_developer")
            diary.currentPage += 1
        if "diary_roadmap" not in diary.screenNames:
            diary.screenNames.append("diary_roadmap")
        renpy.show_screen("float_menu")
        ui.remove(developerCode)

    developerCode = CodeSequence(
        sequence=[getattr(pygame, "K_{0}".format(char)) for char in "godmode"],
        unlock=developerUnlock,
    )

