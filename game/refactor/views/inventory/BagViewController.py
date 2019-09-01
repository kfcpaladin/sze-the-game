from refactor.util import RenpyCallbacks
from refactor.util import Rect2D

class BagViewController(object):
    def __init__(self, total_rows, total_columns):
        self.total_rows = 5
        self.total_columns = 5

        self.equipped_colour = None
        self.unequipped_colour = None
        self.background_colour = None
        self._tooltip_transparency = 255 
        self._item_transparency = 255

    @property
    def tooltip_transparency(self):
        return self._tooltip_transparency

    @tooltip_transparency.setter
    def tooltip_transparency(self, value):
        self._tooltip_transparency = self._clamp_alpha(value)

    
    @property
    def item_transparency(self):
        return self._item_transparency

    @item_transparency.setter
    def item_transparency(self, value):
        self._item_transparency = self._clamp_alpha(value)
    
    def on_item_click(self, item):
        item.toggle_equip()
        RenpyCallbacks.get_instance().play_sfx("vpunch.ogg")

    def get_item_colour(self, item):
        if item.is_equipped:
            return self.equipped_colour.applyAlpha(self.item_transparency)
        return self.unequipped_colour.applyAlpha(self.item_transparency)

    def get_tooltip_colour(self, item):
        if item.is_equipped:
            return self.equipped_colour.applyAlpha(self.tooltip_transparency)
        return self.unequipped_colour.applyAlpha(self.tooltip_transparency)

    def get_tooltip_background_colour(self):
        return self.background_colour.applyAlpha(self.tooltip_transparency)

    def get_tile_rect(self, grid_rect, border_size=0):
        total_width = grid_rect.width - border_size * (self.total_columns+1)
        total_height = grid_rect.height - border_size * (self.total_rows+1)

        width = int(total_width / self.total_columns)
        height = int(total_height / self.total_rows)

        return Rect2D(bottom=height, right=width)

    
    def _clamp_alpha(self, value):
        if value < 0:
            return 0
        elif value > 255:
            return 255

        return value