from .ObservableCondition import ObservableCondition

class And(ObservableCondition):
    def __init__(self, *conditions):
        ObservableCondition.__init__(self)
        self._sub_conditions = [] 
        for condition in conditions:
            self.add_condition(condition)
    
    def add_condition(self, condition):
        self._sub_conditions.append(condition)
        condition.observe(self)
        self.value = self.check_condition()

    def on_change(self, old, new):
        self.value = self.check_condition()

    def check_condition(self):
        for condition in self._sub_conditions:
            if not condition.is_satisfied:
                return False
        return True
    
class Or(ObservableCondition):
    def __init__(self, *conditions):
        ObservableCondition.__init__(self)
        self._sub_conditions = []
        for condition in conditions:
            self.add_condition(condition)
    
    def add_condition(self, condition):
        self._sub_conditions.append(condition)
        condition.observe(self)
        self.value = self.check_condition()

    def on_change(self, old, new):
        self.value = self.check_condition()

    def check_condition(self):
        for condition in self._sub_conditions:
            if condition.is_satisfied:
                return True
        return False