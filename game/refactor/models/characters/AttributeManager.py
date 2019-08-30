from refactor.util.serialisation import Visitable

class AttributeManager(Visitable):
    def __init__(self):
        super().__init__(self)
        self._attributes = {}

    def get(self, name):
        attribute = self._attributes.get(name, None)
        if attribute is None:
            raise KeyError("Unknown attribute {0} requested".format(name)) 
        return attribute

    def listen_change(self, name, condition=lambda x,y: True):
        attribute = self.get(name)
        def wrapper(func):
            def wrapped(old, new):
                if condition(old, new):
                    return func(old, new)
            attribute.observer(wrapped)
            return wrapped
        return wrapper

    def listen_loss(self, name):
        return self.listen_change(name, condition=lambda x,y: y<x)
    
    def listen_gain(self, name):
        return self.listen_change(name, condition=lambda x,y: y>x)

    def add(self, attribute):
        name = attribute.name
        if name in self._attributes:
            raise KeyError("Attribute {0} already exists".format(name))
        self._attributes.setdefault(name, attribute)

    def accept(self, visitor):
        return visitor.visit(AttributeManager, self)

