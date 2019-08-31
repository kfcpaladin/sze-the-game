from refactor.util.observable import ObservableProperty
from refactor.util.serialisation import Visitable
from refactor.persistence import JSONExporter

class Attribute(ObservableProperty, Visitable):
    def __init__(self, name, value):
        ObservableProperty.__init__(self, value)
        self.name = name
    
    def accept(self, visitor):
        return visitor.visit("attribute", self)




        