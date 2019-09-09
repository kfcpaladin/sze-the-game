define themes.default = load_default_colour_theme()

init -1 python:
    from util.colours import ColourTheme, PrimaryColours, RainbowColour

    def load_default_colour_theme():
        theme = ColourTheme()
        return theme