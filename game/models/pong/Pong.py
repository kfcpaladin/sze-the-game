from util.gametools import Entity, Surface, Persistent, Controls, Renderable
from .Ball import Ball

class Pong(object):
    def __init__(self, bounding_box):
        self._surfaces = []
        self._entities = []
        self._renderables = []
        self._controls = []
        self._persistent = []
        self._balls = []

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
        self._update_controls()
        self._update_entities(dt)
        self._check_collision()
        self._check_balls_scored()
        

    def end(self):
        self._is_ended = True

    def add(self, entity):
        if isinstance(entity, Entity):
            self._entities.append(entity)
        if isinstance(entity, Persistent):
            entity.store()
            self._persistent.append(entity)
        if isinstance(entity, Surface):
            self._surfaces.append(entity)
        if isinstance(entity, Ball):
            self._balls.append(entity)
        if isinstance(entity, Renderable):
            self._renderables.append(entity)
        if isinstance(entity, Controls):
            self._controls.append(entity)
    
    def render(self, renderer):
        for renderable in self._renderables:
            renderable.render(renderer)

    def _reset_entities(self):
        for entity in self._persistent:
            entity.load()
    
    def _update_controls(self):
        for control in self._controls:
            control.update()

    def _update_entities(self, dt):
        for entity in self._entities:
            entity.update(dt)
    
    def _check_collision(self):
        for entity in self._entities:
            for surface in self._surfaces:
                if entity is surface:
                    continue
                surface.on_collision(entity)
    
    def _check_balls_scored(self):
        for ball in self._balls:
            if ball.rect.left < self._bounding_box.left:
                self._right_score += 1
                ball.load()
            elif ball.rect.right > self._bounding_box.right:
                self._left_score += 1
                ball.load()

