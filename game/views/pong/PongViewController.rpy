init -1 python:
    from models.pong import PongRenderer

    class PongViewController(PongRenderer, RenpyRenderer):
        def __init__(self, game):
            RenpyRenderer.__init__(self)
            self._game = game        

        # Override renpy.Displayable
        def render(self, width, height, st, at):
            RenpyRenderer.render(self, width, height, st, at)
            self._game.update(self.dt)

            self.render_background(width, height, Image(loadImage("screen_bg_pong.png")))
            self._render_score(self._game.left_score, self._game.right_score)
            self._game.render(self)

            renpy.redraw(self, 0)
            return self.screen

        def event(self, ev, x, y, st):
            raise renpy.IgnoreEvent()

        # Override PongRenderer
        def render_paddle(self, paddle):
            self.render_entity(paddle, Solid(paddle.colour))
        
        def render_ball(self, ball):
            self.render_entity(ball, Solid(ball.colour))

        # custom render 
        def _render_score(self, left_score, right_score):
            text = renpy.render(
                Text("{0}/{1}".format(left_score, right_score)),
                100, 100, 0, 0)

            centre = self._game.bounding_box.get_relative_centre(0.5, 0.5)

            self.screen.blit(text, (centre.x-50, 50))


        

            
