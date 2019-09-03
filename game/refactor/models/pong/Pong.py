from .BounceSurface import BounceSurface
from .Ball import Ball
from .PongRenderer import Renderable
from .Entity import Entity

class Pong(object):
    def __init__(self):
        self._surfaces = []
        self._balls = []
        self._entities = []
        self._renderables = []
    
    def update(self, dt):
        for entity in self._entities:
            entity.update()
        
        for ball in self._balls:
            for surface in self._surfaces:
                surface.bounce(ball)
    
    def add(self, entity):
        if isinstance(entity, Entity):
            self._entities.append(entity)
        if isinstance(entity, BounceSurface):
            self._surfaces.append(entity)
        if isinstance(entity, Ball):
            self._balls.append(entity)
        if isinstance(entity, Renderable):
            self._renderables.append(entity)
    
    def render(self, renderer):
        for renderable in self._renderables:
            renderable.render(renderer)

        
