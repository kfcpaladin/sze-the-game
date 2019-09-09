class Item(object):
    def __init__(self, id, name, description, icon=None):
        self.id = id
        self.name = name 
        self.description = description 
        self.icon = icon 

        self._actions = []

    @property
    def actions(self):
        return self._actions

    def add_action(self, action):
        self._actions.append(action)

    def use(self, person): 
        for action in self._actions:
            action.apply(person)
    
    def undo(self, person):
        for action in self._actions:
            action.undo(person)
    