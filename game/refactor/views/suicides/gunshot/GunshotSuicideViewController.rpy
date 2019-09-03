init -2 python:
    from refactor.models.suicides.gunshot import Renderer

    class GunshotSuicideViewController(RenpyRenderer, Renderer):
        def __init__(self, manager):
            RenpyRenderer.__init__(self)
            self._manager = manager
        
        def event(self, ev, x, y, st):
            # listen click event for gun shot
            raise renpy.IgnoreEvent()

        def render(self, width, height, st, at):
            RenpyRenderer.render(self, width, height, st, at)
            self._manager.update(self.dt)

            self.render_background(width, height, Image(loadImage("kms_bg_bedroom.png")))
            self._manager.render(self)
            renpy.redraw(self, 0)
            return self.screen

        def on_click(self, mouse_position):
            pass
        
        def render_gun(self, gun):
            self.render_entity(gun, Image(loadImage("kms_icon_glockNoTrigger.png")))
        
        def render_bullet(self, bullet):
            self.render_entity(bullet, Image(loadImage("icon_rina.png")))
        
        def render_head(self, head):
            self.render_entity(head, Image(loadImage("char_arthurside.png")))

        


