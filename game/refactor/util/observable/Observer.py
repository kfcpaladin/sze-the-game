from abc import abstractmethod

class Observer(object):
    @abstractmethod
    def on_change(self, old, new):
        pass