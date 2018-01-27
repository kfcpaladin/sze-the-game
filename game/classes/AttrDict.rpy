# Allow for dictionaries to act like javascript dictionaries
# this if for clarity reasons
init -1 python:
    class AttrDict(renpy.python.RevertableDict):
        def __init__(self, init={}):
            dict.__init__(self, init)

        def __getattr__(self, name):
            return self[name]

        def __setattr__(self, name, value):
            self[name] = value

        def combine(self, otherDict):
            self.update(otherDict)
            return self