from .ItemAction import ItemAction

class AttributeModifier(ItemAction):
    def __init__(self, attribute, value):
        self._attribute = attribute
        self._value = value

    def apply(self, person):
        person.get_attribute(self._attribute).value += self._value

    def undo(self, person):
        person.get_attribute(self._attribute).value -= self._value

    @property
    def description(self):
        header = "+" if self._value >= 0 else "-"
        return "{header}{value} {attribute}".format(
            header=header,
            value=self._value,
            attribute=self._attribute)