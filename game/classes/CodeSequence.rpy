init -10 python:
    # class for handling key sequences
    class CodeSequence(renpy.Displayable):

        def __init__(self, sequence, unlock):
            renpy.Displayable.__init__(self)
            self.unlock = unlock
            self.unlocked = False
            self.index = 0
            self.sequence = sequence
            config.overlay_functions.append(lambda: ui.add(self))

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