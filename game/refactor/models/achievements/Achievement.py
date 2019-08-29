from . import Visitable
from . import DependencyList

class Achievement(Visitable):
    def __init__(self, _id, title, brief, description, icon=None, is_hidden=False):
        self.id = _id
        self.title = title 
        self.brief = brief 
        self.description = description 
        self.icon = icon
        self.is_hidden = is_hidden

        self.unlock_dependencies = DependencyList() 
        self.unlock_dependencies.listen(self._on_dependencies_change)
        self.complete_dependencies = DependencyList() 
        self.unlock_dependencies.listen(self._on_dependencies_change)

        self._listeners = []

    @property
    def is_visible(self):
        return not self.is_hidden or self.is_completed

    @property
    def is_completed(self):
        return self.complete_dependencies.is_satisfied

    @property
    def is_unlocked(self):
        return self.unlock_dependencies.is_satisfied

    def add_unlock_dependency(self, dependency):
        self.unlock_dependencies.add(dependency)

    def add_complete_dependency(self, dependency):
        self.complete_dependencies.add(dependency)

    def listen_update(self, listener):
        self._listeners.append(listener)

    def notify_all(self):
        for listener in self._listeners:
            listener(self)

    def accept(self, visitor):
        return visitor.visit("achievement", self)

    # changes to any of the dependency lists
    def _on_dependencies_change(self, _):
        self.notify_all()