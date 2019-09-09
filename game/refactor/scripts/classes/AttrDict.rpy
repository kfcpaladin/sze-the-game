# Allow for dictionaries to act like javascript dictionaries
# this if for clarity reasons
init -10 python:
    class AttrDict(renpy.python.RevertableDict):
        def __init__(self, init={}):
            dict.__init__(self, init)

        def __getattr__(self, name):
            return self[name]

        def __setattr__(self, name, value):
            self[name] = value
        
        # pickling
        def __getstate__(self):
            return self.__dict__

        def __setstate__(self, state):
            self.__dict__ = state

        def combine(self, otherDict):
            self.update(otherDict)
            return self