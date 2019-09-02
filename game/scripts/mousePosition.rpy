init python:
    import pygame

    # this is used for the hovering tooltips in screen_bag
    def getMousePosition():
        realWidth, realHeight = renpy.get_physical_size()
        xScale = 1300/float(realWidth)
        yScale = 700/float(realHeight)
        x, y = pygame.mouse.get_pos()
        return Vector2D(x*xScale, y*yScale)