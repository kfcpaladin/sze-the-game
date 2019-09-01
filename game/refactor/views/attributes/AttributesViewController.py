class AttributesViewController:
    def __init__(self):
        self._attribute_messages = []
        self._attribute_message = None
    
    def __iter__(self):
        for attribute_message in self._attribute_messages:
            yield attribute_message

    @property
    def attribute_message(self):
        return self._attribute_message

    @attribute_message.setter
    def attribute_message(self, attribute_message):
        self._attribute_message = attribute_message
    
    def set_attribute(self, attribute_message):
        self.attribute_message = attribute_message

    @property
    def attribute_messages(self):
        return self._attribute_messages

    def add_attribute_message(self, attribute_message):
        self._attribute_messages.append(attribute_message)


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