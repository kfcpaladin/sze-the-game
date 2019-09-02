from renpy.color import Color
from .PrimaryColours import PrimaryColours
from .RainbowColour import RainbowColour

class ColourTheme(object):
    def __init__(self):
        self.primary = PrimaryColours.GREEN
        self.seconday = PrimaryColours.RED

        self.warning = PrimaryColours.YELLOW
        self.error = PrimaryColours.RED

        self.positive = PrimaryColours.GREEN
        self.negative = PrimaryColours.RED
        self.neutral = PrimaryColours.YELLOW

        self.background = PrimaryColours.MAROON
        
        self.dark = PrimaryColours.BLACK
        self.light = PrimaryColours.WHITE

        self.text = PrimaryColours.WHITE

        self._rainbow = RainbowColour()

    @property
    def rainbow(self):
        return Color(self._rainbow.rgba)