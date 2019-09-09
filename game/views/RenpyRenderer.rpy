
init -10 python:
    class RenpyRenderer(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self._last_st = 0
            self._dt = 0
        
        @property
        def dt(self):
            return self._dt
        
        def render(self, width, height, st, at):
            self._st = st
            self._at = at

            self._dt = st - self._last_st
            self._last_st = st
        
            screen = renpy.Render(width, height, st, at)
            self.screen = screen
            return screen
        
        def render_box(self, width, height, position, texture):
            box = renpy.render(
                texture, 
                width, 
                height, 
                self._st, 
                self._at)            
            self.screen.blit(box, position)

        def render_background(self, width, height, texture):
            self.render_box(
                width,
                height,
                (0, 0),
                texture)

        def render_entity(self, entity, texture):
            self.render_box(
                entity.width, 
                entity.height, 
                (entity.position.x, entity.position.y),
                texture)