from util import RenpyCallbacks

class DiaryPage(object):
    def __init__(self, screen, cleanup_screens=[]):
        self._screen = screen
        # screens that need to be cleaned up b/c of buggy behaviour
        self._cleanup_screens = []
    
    def show(self):
        RenpyCallbacks.get_instance().show_screen(self._screen)
    
    def hide(self):
        RenpyCallbacks.get_instance().hide_screen(self._screen)
        for screen in self._cleanup_screens:
            RenpyCallbacks.get_instance().hide_screen(screen)