from abc import abstractmethod

class RenpyCallbacks(object):
    _instance = None

    @staticmethod
    def set_instance(instance):
        # deal with pickling issues
        if RenpyCallbacks._instance is not None:
            return
            # raise RuntimeError("RenpyCallbacks already instantiated")
        RenpyCallbacks._instance = instance

    @staticmethod
    def get_instance():
        if RenpyCallbacks._instance is None:
            raise RuntimeError("RenpyCallbacks not instantiated")
        return RenpyCallbacks._instance 

    @abstractmethod
    def say(self, message, character=None):
        pass
    
    @abstractmethod
    def show_screen(self, screen, *args, **kwargs):
        pass

    @abstractmethod
    def hide_screen(self, screen):
        pass

    @abstractmethod
    def call_label(self, label):
        pass

    @abstractmethod
    def play_sfx(self, filepath):
        pass
    
    @abstractmethod
    def play_music(self, filepath):
        pass