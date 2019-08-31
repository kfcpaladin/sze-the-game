from abc import abstractmethod
from refactor.util.serialisation import Visitable

class Condition(Visitable):
    def __call__(self, old, new):
        return self.check(old, new)

    @abstractmethod
    def check(self, old, new):
        pass

class LessThan(Condition):
    def __init__(self, value):
        self._value = value

    def check(self, old, new):
        return new < self._value
    
    def accept(self, visitor):
        return visitor.visit("condition_lt", self)

class EqualTo(Condition):
    def __init__(self, value):
        self._value = value
    
    def check(self, old, new):
        return new == self._value

    def accept(self, visitor):
        return visitor.visit("condition_eq", self)

class GreaterThan(Condition):
    def __init__(self, value):
        self._value = value
    
    def check(self, old, new):
        return new > self._value

    def accept(self, visitor):
        return visitor.visit("condition_eq", self)

class Not(Condition):
    def __init__(self, condition):
        self._condition = condition
    
    def check(self, old, new):
        return not self._condition(old, new)

    def accept(self, visitor):
        return visitor.visit("condition_not", self)
        
class And(Condition):
    def __init__(self, *conditions):
        self._conditions = conditions
    
    def check(self, old, new):
        for condition in self._conditions:
            if not condition(old, new):
                return False
        return True

    def accept(self, visitor):
        return visitor.visit("condition_and", self)

class Or(Condition):
    def __init__(self, *conditions):
        self._conditions = conditions
    
    def check(self, old, new):
        for condition in self._conditions:
            if condition(old, new):
                return True
        return False

    def accept(self, visitor):
        return visitor.visit("condition_or", self)