class InventoryItem(object):
    def __init__(self, user, item):
        self._item = item
        self._user = user
        self._is_equipped = False
    
    @property
    def id(self):
        return self._item.id
    
    @property
    def name(self):
        return self._item.name

    @property
    def description(self):
        return self._item.description
    
    @property
    def icon(self):
        return self._item.icon

    @property
    def actions(self):
        return self._item.actions

    @property
    def is_equipped(self):
        return self._is_equipped    
    
    def toggle_equip(self):
        self._is_equipped = not self._is_equipped
        if not self._is_equipped:
            self._item.undo(self._user)
        else:
            self._item.use(self._user)
         
     


    
