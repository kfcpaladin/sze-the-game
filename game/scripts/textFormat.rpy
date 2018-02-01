init -2 python:
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
        excludeChar = " "+str(exclude)
        excludeFormat = False                           # used to ignore {tag} or {/tag}
        colourFormatter = "{{color={0}}}{1}{{/color}}"
        for char in string:
            if not excludeFormat and char == '{':       # toggle on format when starting {...}
                excludeFormat = True
            if char in excludeColour or excludeFormat:  # dont format if inside {...} or specified
                rainbowString +=  char
            else:
                rainbowString += colourFormatter.format(rainbow, char)
            # only cycle for acceptable characters and if not parsing format segment
            if char not in (excludeChar+excludeColour) and not excludeFormat: 
                rainbow.cycle(rate)
            if excludeFormat and char == '}':           # toggle off format when {...} is finished
                excludeFormat = False
        return rainbowString

    """
        Will gradually change the size of the text from start to end
        start = size of first character
        end = size of last character
    """
    def sizeText(string, start=25, end=25):
        excludeFormat = False                       # used to ignore {tag} or {/tag}
        increment = (end-start)/float(getLenWithoutFormat(string))
        newString = ""
        formatter = "{{size={0}}}{1}{{/size}}"
        for char in string:
            if not excludeFormat and char == '{':   # toggle on exclude
                excludeFormat = True
            if not excludeFormat:                   # normal character or formatting
                newString += formatter.format(int(start), char)
                start += increment
            else:
                newString += char
            if excludeFormat and char == '}':       # toggle off exclude
                excludeFormat = False
        return newString
    
    """
        Get the string length ignoring formatting stuff
        Will ignore characters inside {tag}
    """
    def getLenWithoutFormat(string):
        length = 0
        exclude = False
        for char in string:
            if not exclude and char == '{':
                exclude = True
            if not exclude:
                length += 1
            if exclude and char == '}':
                exclude = False
        return length
