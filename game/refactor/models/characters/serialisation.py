from refactor.persistence import JSONImporter
from .Character import Character
from .Attribute import Attribute

@JSONImporter.register("character")
def import_character(data):
    name = data.get("name")
    image = data.get("image")
    icon = data.get("icon", None)

    character = Character(name=name, image=image, icon=icon)

    attributes_data = data.get("attributes", [])
    for attribute_data in attributes_data:
        attribute = JSONImporter.visit("attribute", attribute_data)
        character.add_attribute(attribute)
    
    return character

@JSONImporter.register("attribute")
def import_attribute(data):
    name = data.get("name")
    value = data.get("value")
    return Attribute(name, value)

