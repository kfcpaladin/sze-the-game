from .Attribute import Attribute
from refactor.util.dependency import BasicDependency

class AttributeDependency(BasicDependency):
    def __init__(self, attribute, condition):
        BasicDependency.__init__(self)
        self._attribute = attribute
        self._condition = condition
        self._attribute.observe(self._on_attribute_change)
        self._is_satisifed = False
    
    @property
    def is_satisfied(self):
        return self._is_satisifed

    def _on_attribute_change(self, old, new):
        self._is_satisifed = self._condition(old, new)
        self.notify_all()

    def accept(self, visitor):
        return visitor.visit("attribute_dependency", self)
    
