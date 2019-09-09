init -2 python:
    from models.suicides.gunshot import Renderer

    class GunshotSuicideViewController(RenpyRenderer, Renderer):
        import pygame

        def __init__(self, manager):
            RenpyRenderer.__init__(self)
            self._manager = manager
        
        def event(self, event, x, y, st):
            if self.closed:
                return None 

            if x == -1 and y == -1:
                raise renpy.IgnoreEvent()

            self._manager.move_gun(Vector2D(x, y))
            if event.type == pygame.MOUSEBUTTONDOWN:
                self._manager.pull_trigger()
            elif event.type == pygame.MOUSEBUTTONUP:
                self._manager.release_trigger()

            raise renpy.IgnoreEvent()

        def render(self, width, height, st, at):
            RenpyRenderer.render(self, width, height, st, at)
            self._manager.update(self.dt)
            self.render_background(width, height, Image(loadImage("kms_bg_bedroom.png")))
            self._manager.render(self)
            renpy.redraw(self, 0)
            return self.screen

        @property
        def closed(self):
            return self._manager.has_died

        def reset(self):
            self._manager.reset()

        def render_gun(self, gun):
            self.render_entity(gun, Frame(loadImage("kms_icon_glockNoTrigger.png")))

        def render_shotgun(self, shotgun):
            self.render_entity(shotgun, Frame(loadImage("kms_shotgun.png")))
        
        def render_bullet(self, bullet):
            self.render_entity(bullet, Frame(loadImage("icon_rina.png")))
        
        def render_head(self, head):
            self.render_entity(head, Frame(loadImage("char_arthurside.png")))

        


