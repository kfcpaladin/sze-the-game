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
        friend.friendship += total

    # add item to bag
    def unlockItem(id, bag):
        item = items.get(id)
        inventories.bag.add(item)
        playsfx("xbox.ogg")
        popups.add(Popup(
            message="Unlocked item\n{0}".format(item.name),
            icon=item.icon,
            colour=themes.default.rainbow
        ))

    # unlock dildo
    def konamiCodeUnlock():
        unlockItem("neo armstrong", inventories.bag)
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
        unlockItem("god", inventories.bag)
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
        popups.add(Popup(
            message="Unlocked developer mode",
            icon=loadImage("icon_rina.png"),
            colour=themes.default.rainbow
        ))
        config.developer = True
        game.diaryIntro = True
        game.hasDiary = True
        diary.insert_page(DiaryPage("diary_developer"), 0)
        diary.append_page(DiaryPage("diary_roadmap"))
        renpy.show_screen("float_menu")
        ui.remove(developerCode)

    developerCode = CodeSequence(
        sequence=[getattr(pygame, "K_{0}".format(char)) for char in "godmode"],
        unlock=developerUnlock,
    )

