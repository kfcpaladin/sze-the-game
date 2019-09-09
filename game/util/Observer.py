from abc import abstractmethod

class Observer(object):
    def __call__(self, old, new):
        self.on_change(old, new)

    @abstractmethod
    def on_change(self, old, new):
        pass