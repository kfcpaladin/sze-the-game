from .Vector2D import Vector2D

class Rect2D:
    def __init__(self, top=0, left=0, right=0, bottom=0):
        self.top = top
        self.left = left
        self.right = right
        self.bottom = bottom
    
    def add_offset(self, offset):
        return Rect2D(
            top=self.top+offset.y,
            bottom=self.bottom+offset.y,
            right=self.right+offset.x,
            left=self.left+offset.x
        )

    def get_relative_centre(self, x, y):
        top = self.top + (y * self.height)
        left = self.left + (x * self.width)

        return Vector2D(x=left, y=top)

    @property 
    def centre(self):
        return self.get_relative_centre(0.5, 0.5)
    
    def resize_from_relative_centre(self, x, y, width=None, height=None):
        if width is None:
            width = self.width
        if height is None:
            height = self.height

        relative_centre = self.get_relative_centre(x, y)
        top = relative_centre.y
        left = relative_centre.x

        return Rect2D(
            top=top,
            left=left,
            bottom=top+height,
            right=left+width
        )

    def resize_from_top_left(self, width=None, height=None):
        return self.resize_from_relative_centre(0, 0, width, height)

    def resize_from_bottom_left(self, width=None, height=None):
        return self.resize_from_relative_centre(0, 1, width, height) 

    def resize_from_top_right(self, width=None, height=None):
        return self.resize_from_relative_centre(1, 0, width, height) 

    def resize_from_bottom_right(self, width=None, height=None):
        return self.resize_from_relative_centre(1, 1, width, height) 

    def get_at_origin(self):
        return self.add_offset(-Vector2D(self.width, self.height))

    def copy(self):
        return Rect2D(
            top=self.top,
            left=self.left,
            bottom=self.top,
            right=self.right
        )

    @property
    def width(self):
        return self.right - self.left
    
    @property
    def height(self):
        return self.bottom - self.top
    
    def check_overlap(self, other):
        if self.left > other.right:
            return False
        if self.right < other.left:
            return False 
        if self.top > other.bottom:
            return False
        if self.bottom < other.top:
            return False
        return True
    