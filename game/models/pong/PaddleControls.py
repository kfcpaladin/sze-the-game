import pygame
from util.gametools import Controls

from util.colours import PrimaryColours

class PaddleControls(Controls):
    def __init__(self, paddle, up_key, down_key):
        self._paddle = paddle
        self.up_key = up_key
        self.down_key = down_key
    
    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[self.up_key]:
            self._paddle.move_up()
        elif pressed[self.down_key]:
            self._paddle.move_down()
        else:
            self._paddle.stop()