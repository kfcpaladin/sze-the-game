python early:
    import pygame
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

    # class for handling key sequences
    class CodeSequence(renpy.Displayable):

        def __init__(self, sequence, unlock):
            renpy.Displayable.__init__(self)
            self.unlock = unlock
            self.unlocked = False
            self.index = 0
            self.sequence = sequence

        # This function listens for events.
        def event(self, ev, x, y, st):
            if self.unlocked:
                return
            # We only care about keydown events.
            if ev.type == pygame.KEYDOWN:
                if ev.key == self.sequence[self.index]:    
                    self.index += 1
                    if self.index == len(self.sequence):
                        self.index = 0
                        self.unlocked = True
                        self.unlock()
                else:
                    self.index = 0

        # Return a small empty render, so we get events.
        def render(self, width, height, st, at):
            return renpy.Render(0, 0)

init python:
    import pygame
    from copy import deepcopy

    def konamiCodeUnlock():
        playsfx("xbox.ogg")
        popup("Unlocked item: Neo Armstrong")
        bag.add(deepcopy(unlockableItems["neo armstrong"]))

    def kirbyUnlock():
        playsfx("xbox.ogg")
        popup("Unlocked item: Michael Kirby's Suit")
        bag.add(deepcopy(unlockableItems["god"]))

    konamiCode = CodeSequence(
        sequence=(
            pygame.K_UP, pygame.K_UP, pygame.K_DOWN, pygame.K_DOWN, 
            pygame.K_LEFT, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_RIGHT
        ),
        unlock=konamiCodeUnlock
    )

    kirbyCode = CodeSequence(
        sequence=(
            pygame.K_UP, pygame.K_DOWN, pygame.K_UP, pygame.K_DOWN, 
            pygame.K_LEFT, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_RIGHT
        ),
        unlock=kirbyUnlock
            
    )

    # this adds all the key sequences to the start
    def addKeySequences():
        ui.add(konamiCode)  
        ui.add(kirbyCode)

    config.overlay_functions.append(addKeySequences)

