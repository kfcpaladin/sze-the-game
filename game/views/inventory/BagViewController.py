from util import RenpyCallbacks
from util.gametools import Rect2D

class BagViewController(object):
    def __init__(self, total_rows, total_columns):
        self.total_rows = 5
        self.total_columns = 5

        self.tooltip_transparency = 0.8 
        self.item_transparency = 0.5

    def on_item_click(self, item):
        item.toggle_equip()
        RenpyCallbacks.get_instance().play_sfx("vpunch.ogg")

    def get_item_colour(self, item, theme):
        if item.is_equipped:
            return theme.positive.opacity(self.item_transparency)
        return theme.neutral.opacity(self.item_transparency)

    def get_tooltip_colour(self, item, theme):
        if item.is_equipped:
            return theme.positive.opacity(self.tooltip_transparency)
        return theme.neutral.opacity(self.tooltip_transparency)

    def get_tooltip_background_colour(self, theme):
        return theme.background.opacity(self.tooltip_transparency)

    def get_tile_rect(self, grid_rect, border_size=0):
        total_width = grid_rect.width - border_size * (self.total_columns+1)
        total_height = grid_rect.height - border_size * (self.total_rows+1)

        width = int(total_width / self.total_columns)
        height = int(total_height / self.total_rows)

        return Rect2D(bottom=height, right=width)