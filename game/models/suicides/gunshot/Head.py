from util.gametools import Entity, Renderable

class Head(Entity, Renderable):
    def __init__(self, width, height):
        Entity.__init__(self, width, height)
    
    def render(self, renderer):
        return renderer.render_head(self)