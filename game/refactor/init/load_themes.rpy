default themes.default = load_default_colour_theme()

init -1 python:
    from refactor.util.colours import ColourTheme

    def load_default_colour_theme():
        theme = ColourTheme()
        return theme