class ObservableProperty(object):
    def __init__(self, value):
        self._value = value
        self._observers = [] 
        self._binds = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, _val):
        old_val = self._value
        self._value = _val
        if old_val != _val:
            self._on_change(old_val, _val)

    def observe(self, observer):
        self._observers.append(observer)
        return observer

    def bind(self, other_prop):
        self._binds.append(other_prop)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
            return observer
        except ValueError:
            return None

    def _on_change(self, old, new):
        for observer in self._observers:
            observer(old, new)
            # observer.on_change(old, new)
        for other_prop in self._binds:
            other_prop.value = new