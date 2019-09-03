from abc import abstractmethod

class PongRenderer(object):
    def render_paddle(self, paddle):
        pass
    
    def render_ball(self, ball):
        pass

class Renderable(object):
    @abstractmethod
    def render(self, renderer):
        pass    