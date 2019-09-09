class AttributesViewController(object):
    def __init__(self):
        self._attribute_messages = []
        self._attribute_message = None
    
    def __iter__(self):
        for attribute_message in self._attribute_messages:
            yield attribute_message

    def get_attribute_colour(self, attribute, theme):
        if attribute.value > 0:
            return theme.positive
        elif attribute.value == 0:
            return theme.neutral
        return theme.negative

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


