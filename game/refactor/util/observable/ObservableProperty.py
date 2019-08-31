class ObservableProperty(object):
    def __init__(self, value):
        self._value = value
        self._observers = [] 
        self._total_setters = 0
        self._total_on_change = 0
        self._total_calls = 0

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, _val):
        old_val = self._value
        self._value = _val
        self._total_setters += 1
        self._on_change(old_val, _val)

    def observe(self, observer):
        self._observers.append(observer)
        return observer
    
    def detach(self, observer):
        try:
            self._observers.remove(observer)
            return observer
        except ValueError:
            return None


    def _on_change(self, old, new):
        self._total_on_change += 1
        for observer in self._observers:
            observer(old, new)
            self._total_calls += 1
