# dependency that is polled
from refactor.util.dependency import BasicDependency

class LambdaDependency(BasicDependency):
    instances = []

    def __init__(self, func):
        self._func = func
        LambdaDependency.instances.append(self)

    def is_satisfied(self):
        return self._func()

    @staticmethod
    def notify_all_instances():
        for instance in LambdaDependency.instances:
            instance.notify_all()

    def accept(self, visitor):
        pass

    