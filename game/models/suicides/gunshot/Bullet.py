from util.gametools import Entity, Renderable

class Bullet(Entity, Renderable):
    def __init__(self, width, height):
        Entity.__init__(self, width, height)

    def check_despawned(self, bounding_box):
        return not self.rect.check_overlap(bounding_box)    
    
    def render(self, renderer):
        return renderer.render_bullet(self)