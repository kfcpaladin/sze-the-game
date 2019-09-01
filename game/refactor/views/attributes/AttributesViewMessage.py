class AttributesViewMessage(object):
    def __init__(self, attribute, brief, priority_list):
        self._attribute = attribute
        self._brief = brief
        self._priority_list = priority_list

    @property
    def name(self):
        return self._attribute.name

    @property
    def value(self):
        return self._attribute.value
    
    @property
    def brief(self):
        return self._brief
    
    @property
    def message(self):
        return self._priority_list.get_entry(self._attribute.value)