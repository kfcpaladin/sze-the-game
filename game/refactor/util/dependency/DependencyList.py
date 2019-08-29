from . import Dependency
from . import serialisation

class DependencyList(Dependency, serialisation.Visitable):
    def __init__(self):
        self._dependencies = []
        self._is_all_satisfied = False

    def __iter__(self):
        for dependency in self._dependencies:
            yield dependency

    def add(self, dependency):
        self.dependencies.append(dependency)
        dependency.listen(self._listen_dependency)

    @property
    def dependencies(self):
        return self._dependencies

    @property
    def is_satisfied(self):
        return self._is_all_satisfied

    def accept(self, visitor):
        return visitor.visit("dependency_list", self)

    def _listen_dependency(self, dependency):
        if not dependency.is_satisifed:
            self._set_is_all_satisfied(False)
        else:
            self._set_is_all_satisfied(self._check_all_satisfied())

    def _set_is_all_satisfied(self, is_all_satisifed):
        if self._is_all_satisfied is not is_all_satisifed:
            self._is_all_satisfied = is_all_satisifed
            self.notify_all()
        else:
            self._is_all_satisfied = is_all_satisifed

    def _check_all_satisfied(self):
        for dependency in self._dependencies:
            if not dependency.is_satisifed:
                return False
        return True