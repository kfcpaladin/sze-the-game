class ObservableProperty:
    def __init__(self, value):
        self._value = value
        self._observers = {} 

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, _val):
        old_val = self._value
        self._value = _val
        self._on_change(old_val, _val)

    def observe(self, observer):
        self._observers.setdefault(observer, None)
    
    def detach(self, observer):
        return self._observers.pop(observer, None)


    def _on_change(self, old, new):
        for observer in self._observers.keys():
            observer(old, new)
