class ItemCache(object):
    def __init__(self):
        self._items = {}

    def add(self, item):
        id = item.id
        if id in self._items:
            raise KeyError("Item {0} already registered".format(id))
        self._items.setdefault(id, item)

    def get(self, id):
        item = self._items.get(id)
        if item is None:
            raise KeyError("Item {0} doesn't exist".format(id))
        return item