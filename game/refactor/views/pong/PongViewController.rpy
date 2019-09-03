init python:
    from refactor.models.pong import PongRenderer

    class PongViewController(PongRenderer, renpy.Displayable):
        def __init__(self, game):
            renpy.Displayable.__init__(self)
            self._game = game        

        # Override renpy.Displayable
        def render(self, width, height, st, at):
            self._st = st            
            self._at = at

            self._screen = renpy.Render(width, height, st, at)
            # game.update(1.0/30.0)
            game.render(self)
            return self._screen

        def render_paddle(self, paddle):
            self._render_entity_box(ball, Solid(paddle.colour))
        
        def render_ball(self, ball):
            self._render_entity_box(ball, Solid(ball.colour))

        def _render_entity_box(self, entity, texture):
            box = renpy.render(
                texture, 
                entity.width, 
                entity.height, 
                self._st, 
                self._at)            
            self._screen.blit(box, (entity.position.x, entity.position.y))

            
