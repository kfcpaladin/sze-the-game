init -1 python:
    from refactor.models.pong import PongRenderer

    class PongViewController(PongRenderer, renpy.Displayable):
        def __init__(self, game):
            renpy.Displayable.__init__(self)
            self._game = game        
            self._last_st = 0

        # Override renpy.Displayable
        def render(self, width, height, st, at):
            self._st = st            
            self._at = at

            dt = st - self._last_st
            self._last_st = st
            self._game.update(dt)

            screen = renpy.Render(width, height, st, at)
            self._screen = screen
            self._render_background(width, height)
            self._render_score(self._game.left_score, self._game.right_score)
            self._game.render(self)

            renpy.redraw(self, 0)
            return screen

        def event(self, ev, x, y, st):
            raise renpy.IgnoreEvent()

        # Override PongRenderer
        def render_paddle(self, paddle):
            self._render_entity_box(paddle, Solid(paddle.colour))
        
        def render_ball(self, ball):
            self._render_entity_box(ball, Solid(ball.colour))

        # custom render 
        def _render_score(self, left_score, right_score):
            text = renpy.render(
                Text("{0}/{1}".format(left_score, right_score)),
                100, 100, 0, 0)

            centre = self._game.bounding_box.get_relative_centre(0.5, 0.5)

            self._screen.blit(text, (centre.x-50, 50))


        def _render_box(self, width, height, position, texture):
            box = renpy.render(
                texture, 
                width, 
                height, 
                self._st, 
                self._at)            
            self._screen.blit(box, position)

        def _render_background(self, width, height):
            self._render_box(
                width,
                height,
                (0, 0),
                Image(loadImage("screen_bg_pong.png")))

        def _render_entity_box(self, entity, texture):
            self._render_box(
                entity.width, 
                entity.height, 
                (entity.position.x, entity.position.y),
                texture)

            
