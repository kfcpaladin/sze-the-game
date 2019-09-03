from abc import abstractmethod

class Renderer(object):
    @abstractmethod
    def render_bullet(self, bullet):
        pass
    
    @abstractmethod
    def render_head(self, head):
        pass
    
    @abstractmethod
    def render_gun(self, gun):
        pass
