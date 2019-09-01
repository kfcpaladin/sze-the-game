class PropertyStore(object):
    def __init__(self):
        self._values = {}
    
    def add(self, name, prop):
        if name in self._values:
            raise KeyError("Property with key {0} already added".format(name))
        self._values.setdefault(name, prop)
    
    def get_prop(self, name):
        prop = self._values.get(name)
        if prop is None:
            raise KeyError("Unknown property {0} in store".format(name))
        return prop
    
    def get(self, name):
        return self.get_prop(name).value
    
    def set(self, name, value):
        self.get_prop(name).value = value