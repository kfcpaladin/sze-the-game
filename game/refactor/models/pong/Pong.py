from .BounceSurface import BounceSurface
from .Ball import Ball
from .PongRenderer import Renderable
from .Entity import Entity

class Pong(object):
    def __init__(self, bounding_box):
        self._surfaces = []
        self._balls = []
        self._entities = []
        self._renderables = []

        self._bounding_box = bounding_box
        self._is_ended = False

        self._left_score = 0
        self._right_score = 0

    @property
    def is_ended(self):
        return self._is_ended

    @property
    def left_score(self):
        return self._left_score
    
    @property
    def right_score(self):
        return self._right_score

    @property
    def bounding_box(self):
        return self._bounding_box

    def start(self):
        self._reset_entities()
        self._left_score = 0
        self._right_score = 0
        self._is_ended = False

    def update(self, dt):
        for entity in self._entities:
            entity.update(dt)
        # bounce 
        for ball in self._balls:
            for surface in self._surfaces:
                if ball is surface:
                    continue
                surface.bounce(ball)
        # track score 
        for ball in self._balls:
            if ball.rect.left < self._bounding_box.left:
                self._right_score += 1
                ball.load()
            elif ball.rect.right > self._bounding_box.right:
                self._left_score += 1
                ball.load()

    def end(self):
        self._is_ended = True

    def add(self, entity):
        if isinstance(entity, Entity):
            entity.store()
            self._entities.append(entity)
        if isinstance(entity, BounceSurface):
            self._surfaces.append(entity)
        if isinstance(entity, Ball):
            self._balls.append(entity)
        if isinstance(entity, Renderable):
            self._renderables.append(entity)
        
    def _reset_entities(self):
        for entity in self._entities:
            entity.load()
    
    def render(self, renderer):
        for renderable in self._renderables:
            renderable.render(renderer)

        
