init -1 python:
    import itertools

    """
        A highly advanced colour class for use in the renpy visual novel
        Includes features such as:
            - mixing
            - inverting
            - changing alpha
            - getting hex code
            - getting rgb code
            - initialising with hex string, rgba keywords and rgba tuple
            - will essentially behave like a string for the renpy.display.imagelike.Solid() function
    """
    class AdvancedColour(str):
        """
            Create new superclass of str before __init__, so that it 
            can inherit the class while accepting multiple arguments
        """
        def __new__(self, *args, **kwargs):
            return super(AdvancedColour, self).__new__(self, "")

        def __init__(self, *args, **kwargs):
            self.__default__()  # need to initialise defaults first
            self.hexFormat = "{:02x}"   
            self.updateStringCache()    # get string cache after specifying hex format
            self.set(*args, **kwargs)   # set colour based on input args
        
        """
            Default instantiation of class
            Setups all the default rgb components, and the default values
        """
        def __default__(self):
            self.components = ("r", "g", "b", "a") # must be declared first, since __setattr__ depends on it
            self.range = AttrDict({
                "min": 0, 
                "max": 255,
            })
            self.defaultValues = (0, 0, 0, 255)
            self.stringType = (str, basestring, unicode)
            # avoid setting using __setattr__, to avoid uninitialisation of self.components
            for component, value in itertools.izip(self.components, self.defaultValues):
                self.__dict__[component] = value

        """
            Python default methods:
                __repr__ = fetched by console 
                __str__ = fetched by print()
                __add__ = fetched by + operator
                __sub__ = fetched by - operator
                __mul__ = fetched by * operator
                __div__ = fetched by / operator
                __format__ = fetched by str.format() 
        """
        def __repr__(self):
            return "AdvancedColour({})".format(self.stringCache)

        def __str__(self):
            return self.stringCache

        def __add__(self, colour):
            return self.mix(colour)

        def __sub__(self, colour):
            return self.mix(colour.getInverse())

        def __format__(self, format_spec):
            return self.stringCache

        def __setattr__(self, name, value):
            self.__dict__[name] = value
            if name in self.components: # if component changes, update string cache
                self.__dict__[name] = self.clamp(value)
                self.updateStringCache()
                
        def __mul__(self, scale):
            copy = self.getCopy()
            copy.multiply(scale)
            return copy

        def __div__(self, scale):
            return self.__mul__(1/float(scale))

        """
            Interface for accessing the hexCode string for Solid()
        """
        def __getitem__(self, key):
            return self.stringCache[key]
        
        def __getslice__(self, start, end):
            return self.stringCache[start:end]

        def __setitem__(self, key, value):
            self.stringCache[key] = value
        
        def __len__(self):
            return len(self.stringCache)

        """
            Usages include:
                set(0, 0, 0, 0) -> setRGB()
                set(r=0, g=0, b=0, a=0) -> setDict()
                set("#000000") -> setString() -> setFullString()
                set("#000") -> setString() -> setCompactString()
            Condition tree:
                One argument and is string -> setString()
                Multiple arguments -> setRGB()
                No arguments -> setDict()
        """
        def set(self, *args, **kwargs):
            if len(args) == 1 and type(args[0]) in self.stringType:
                self.setString(args[0])
            elif len(args) > 0:
                self.setRGB(args)
            else:
                self.setDict(kwargs)
        
        """
            setDict({"r":0, "g": 0, "b": 0, "a": 0})
            Sets the attributes of colour to those in dictionary
        """
        def setDict(self, dictCode):
            for component, value in dictCode.iteritems():
                setattr(self, component, self.clamp(value))

        """
            setDict(0, 0, 0, 0, ...)
            Uses izip() to read rgb values with components
            izip() terminates when either list ends
        """
        def setRGB(self, rgbCode):
            for value, component in itertools.izip(rgbCode, self.components):
                setattr(self, component, self.clamp(value))
        
        """
            Interface to set colour using a hexCode such as "#fff" or "#ffffff"
            Will check the length of the string to determine which is appropriate
            len("#fff".replace("#", "")) == 3..4 ==> compact hexCode
            len("#ffffff".replace("#", "")) == 6..8 ==> full hexCode
        """
        def setString(self, string):
            stringLength = len(string.replace("#", ""))
            if stringLength in (6, 8):      # "#ffffff" or "#ffffffff"
                self.setFullString(string)
            elif stringLength in (3, 4):    # "#fff" or "#ffff"
                self.setCompactString(string)
            else:
                raise ValueError("Invalid hexcode {}".format(string))
        
        """
            setFullString("#ffffff" or "#ffffffff")
            Breaks down string and converts into indiviudal component values
            Accepts full length hex code
        """
        def setFullString(self, string):
            string = string.replace("#", "")
            dictCode = {}
            for index, component in enumerate(self.components):
                start = 2*index
                end = 2*index+2
                if end <= len(string):
                    dictCode[component] = int(string[start:end], 16)
                else:
                    break
            self.setDict(dictCode)

        """
            setFullString("#fff" or "#ffff")
            Breaks down string and converts into indiviudal component values
            Accepts compact hex code, such as "#fff", which is then scaled 
        """
        def setCompactString(self, string):
            string = string.replace("#", "")
            dictCode = {}
            for index, component in enumerate(self.components):
                start = index
                end = index+1
                if end <= len(string):
                    # 255/15 = 17, used to map values between 0..15 to 0..255
                    dictCode[component] = 17*int(string[start:end], 16) 
                else:
                    break
            self.setDict(dictCode)

        """
            Get different formats of the colour:
                getHex = returns full hexCode "#ffffffff"
                getRGB = returns list of component values [255, 255, 255, 255]
                getDict = returns dict of component values {"r":255, ...}
        """
        def getHex(self):
            hexCode = "#"
            for component in self.components:
                hexCode += self.hexFormat.format(int(getattr(self, component)))
            return hexCode

        def getRGB(self):
            rgbCode = []
            for component in self.components:
                rgbCode.append(getattr(self, component))
            return rgbCode

        def getComponents(self):
            return [component for component in self.components]

        def getDict(self):
            dictCode = {}
            for component in self.components:
                dictCode[component] = getattr(self, component)
            return dictCode

        """
            Get a new instance of the colour:
                getCopy = returns full copy of colour
                getInverse = returns new instance of inverted colour
        """
        def getCopy(self):
            return AdvancedColour(**self.getDict())

        def getInverse(self):
            inverted = self.getCopy()
            inverted.invert()
            return inverted

        """
            Functions for mutating colours:
                mix = Combining a list of colours and averaging it out
                invert = Inverting a colour
                multiply = Scaling a colour by a scalar
                applyAlpha = Returning new object with different colour
        """
        def mix(self, *colours):
            averageValues = {}
            for component in self.components:
                totalValue = getattr(self, component) 
                for colour in colours:
                    totalValue += getattr(colour, component)
                averageValues[component] = totalValue/float(len(colours)+1)
            return AdvancedColour(**averageValues)
        
        def invert(self):
            for component in self.components:
                if component == 'a':    # do not invert alpha
                    continue
                value = getattr(self, component)
                setattr(self, component, self.range.max-value)

        def multiply(self, scale):
            for component in self.components:
                if component == 'a':    # do not scale alpha
                    continue
                value = getattr(self, component)
                newValue = self.clamp(value*scale)
                setattr(self, component, newValue)

        def applyAlpha(self, alpha):
            dictCode = self.getDict()
            if 'a' in dictCode:
                dictCode['a'] = alpha
            return AdvancedColour(**dictCode)

        """
            Used to make sure that a value is between min and max
            Usually min=0, max=255 for a standard rgb colour
        """
        def clamp(self, value):
            if value < self.range.min:
                value = self.range.min
            elif value > self.range.max:
                value = self.range.max
            return value

        """
            Used to update the string interpretation of the colour
            Called whenever a component value is changed
        """
        def updateStringCache(self):
            self.stringCache = self.getHex()

    

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

    """
        Function for turning a generic string into a coloured string
        string = string you want to convert
        rate = how much the rainbow progresses for each character
            - lower rate = slower changing rainbow
            - higher rate = faster changing rainbow
            - 127.5 = 255/2 or a normal looking rainbow
        exclude = characters to ignore when changing rainbow
        excludeColour = make excluded characters white if true
    """
    def rainbowText(string, rate=127.5, exclude="", excludeColour=""):
        rainbow = RainbowColour()
        rainbowString = ""
        excludeChar = " " + str(exclude)
        colourFormatter = "{{color={0}}}{1}{{/color}}"
        for char in string:
            # determine whether to colour character
            if char in excludeColour:
                rainbowString +=  char
            else:
                rainbowString += colourFormatter.format(rainbow, char)
            # only cycle for acceptable characters
            if char not in excludeChar and char not in excludeColour: 
                rainbow.cycle(rate)
        return rainbowString



            

            
