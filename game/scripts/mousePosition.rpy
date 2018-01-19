init python:
    import pygame
    def getMousePosition():
        realWidth, realHeight = renpy.get_physical_size()
        xScale = 1300/float(realWidth)
        yScale = 700/float(realHeight)
        x, y = pygame.mouse.get_pos()
        return (x*xScale, y*yScale)