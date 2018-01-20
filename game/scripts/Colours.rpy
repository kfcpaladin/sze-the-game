init -1 python:
    class CustomColour:
        def __init__(self):
            self.clear = "#ffffff00"
            self.blue = "#333cff"
            self.green = "#009933"
            self.grey = "#b6b3b3"
            self.orange = "#ff5733"
            self.purple = "#5e33ff"
            self.red = "#ff0603"
            self.yellow = "#e6ac00"
            self.maroon = "#800000"
            self.black = self.rgb(0, 0, 0)
            self.white = self.rgb(255, 255, 255)

        def addRgb(self, name, red, green, blue, alpha=255):
            hexCode = self.rgb(red, green, blue)
            if alpha != 255:
                hexCode += "{:02x}".format(alpha)
            setattr(self, name, hexCode)

        def rgb(self, red, green, blue):
            red = self.constrainRGB(red)
            green = self.constrainRGB(green)
            blue = self.constrainRGB(blue)
            value = red*(16**4) + green*(16**2) + blue
            hexCode = "#{:06x}".format(value)
            return hexCode

        def constrainRGB(self, value):
            if value < 0:
                return 0
            elif value > 255:
                return 255
            else:
                return value

    colour = CustomColour()
