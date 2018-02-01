init -9 python:
    """
        A subclass of the generic AdvancedColour class, which offers support for 
        transitioning rainbow colours.
        The colour will start off from red, before transitioning into the spectrum
        and then repeating the process again.
        The rate at which the rainbow transitions is available as a parameter:
            rainbow = RainbowColour() for default rate=25, or
                    = RainbowColour(x) for a custom rate=x
    """
    class RainbowColour(AdvancedColour):
        def __init__(self, rate=25):
            AdvancedColour.__init__(self, "#f00")   # start off at red
            self.currentCycle = 0
            self.maxCycles = len(self.components)-1
            self.fading = False
            self.rate = rate

        """
            Cycles through the colour spectrum like a rainbow
            Starts off as the follow:
                Start = (255, 0, 0)
                Add Green = (255, 0->255, 0) => (255, 255, 0)
                Fade Red  = (255->0, 255, 0) => (0, 255, 0)
                Add Blue  = (0, 255, 0->255) => (0, 255, 255)
                Fade Green = (0, 255->0, 255) =>(0, 0, 255)
                Add Red =   (0->255, 0, 255) => (255, 0, 255)
                Fade Green = (255, 0, 255->0) => (255, 0, 0)
                Repeat = (255, 0, 0)
        """
        def cycle(self, rate):
            # get indexes
            if self.currentCycle >= self.maxCycles:
                self.currentCycle = 0
            nextIndex = self.currentCycle+1
            if nextIndex >= self.maxCycles:
                nextIndex = 0
            # get components
            currentComponent = self.components[self.currentCycle]
            currentValue = getattr(self, currentComponent)
            nextComponent = self.components[nextIndex]
            nextValue = getattr(self, nextComponent)
            # increasing stage
            if not self.fading:
                # increase current component
                if currentValue != self.range.max:
                    setattr(self, currentComponent, currentValue+rate)
                # increase next component if current if full
                elif nextValue != self.range.max:
                    setattr(self, nextComponent, nextValue+rate)
                # if both are full, decrease current
                else:
                    self.fading = True
            # start decreasing current value
            else:
                # decrease until current is 0, then cycle on
                if currentValue != 0:
                    setattr(self, currentComponent, currentValue-rate)
                # if 0, cycle and grow next component
                else:
                    self.currentCycle += 1
                    self.fading = False

    """
        ChangingRainbowColour will update automatically as determined by the gameloop in which
        it is attached to.
        It is hooked into an event listener, through self.event(...) and self.render(..),
        which makes sure that the rainbow colour will update every game loop.
    """
    class ChangingRainbowColour(RainbowColour, renpy.Displayable):
        def __init__(self, rate=25):
            RainbowColour.__init__(self)   
            renpy.Displayable.__init__(self)
            # add to ui when game starts, to be incoporated into the game loop
            config.overlay_functions.append(lambda: ui.add(self))

        """
            Triggered by the main game loop every 1/config.framerate seconds
            event = event handler
            render = make sure that the game will update this
        """
        def event(self, ev, x, y, st):
            self.cycle(self.rate)
        
        def render(self, width, height, st, at):
            return renpy.Render(0, 0)
        
        def remove(self):
            ui.remove(self)