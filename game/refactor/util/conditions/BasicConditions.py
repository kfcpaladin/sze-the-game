from .ObservableCondition import ObservableCondition
from abc import abstractmethod

class ConditionForSingleProp(ObservableCondition):
    def __init__(self, prop):
        ObservableCondition.__init__(self)
        self.prop = prop
        self.value = self.check_condition()
        prop.observe(self)

    def on_change(self, old, new):
        self.value = self.check_condition()

    @abstractmethod
    def check_condition(self):
        pass

class LessThan(ConditionForSingleProp):
    def __init__(self, prop, x):
        self.x = x
        ConditionForSingleProp.__init__(self, prop) 
    
    def check_condition(self):
        return self.prop.value < self.x

class GreaterThan(ConditionForSingleProp):
    def __init__(self, prop, x):
        self.x = x
        ConditionForSingleProp.__init__(self, prop) 
    
    def check_condition(self):
        return self.prop.value > self.x

class EqualTo(ConditionForSingleProp):
    def __init__(self, prop, x):
        self.x = x
        ConditionForSingleProp.__init__(self, prop) 
    
    def check_condition(self):
        return self.prop.value == self.x

class GreaterEqual(ConditionForSingleProp):
    def __init__(self, prop, x):
        self.x = x
        ConditionForSingleProp.__init__(self, prop) 
    
    def check_condition(self):
        return self.prop.value >= self.x

class LessEqual(ConditionForSingleProp):
    def __init__(self, prop, x):
        self.x = x
        ConditionForSingleProp.__init__(self, prop) 
    
    def check_condition(self):
        return self.prop.value <= self.x

