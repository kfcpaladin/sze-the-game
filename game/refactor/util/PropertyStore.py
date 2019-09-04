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

    def __getattribute__(self, name):
        prop = object.__getattribute__(self, "_values").get(name)
        if prop is not None:
            return prop.value
        return object.__getattribute__(self, name)
    
    def __setattr__(self, name, value):
        try:
            prop = self.get_prop(name)
            prop.value = value
        except (KeyError, AttributeError):
            object.__setattr__(self, name, value)


    def get(self, name):
        return self.get_prop(name).value
    
    def set(self, name, value):
        self.get_prop(name).value = value