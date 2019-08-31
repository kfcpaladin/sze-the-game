from refactor.persistence import JSONImporter, JSONExporter
from .Character import Character
from .Attribute import Attribute
from .AttributeDependency import AttributeDependency

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

    JSONImporter.cache_object(("character", character.name), character)
    return character

@JSONImporter.register("attribute")
def import_attribute(data):
    name = data.get("name")
    value = data.get("value")
    return Attribute(name, value)

@JSONImporter.register("attribute_dependency")
def import_attribute_dependency(data):
    character_name = data.get("character_name")
    attribute_name = data.get("attribute")
    condition_data = data.get("condition")

    character = JSONImporter.fetch_cached_object(("character", character_name))
    attribute = character.get_attribute(attribute_name)
    condition = JSONImporter.visit("condition", condition_data)

    return AttributeDependency(attribute, condition)


@JSONExporter.register("character")
def export_character(character):
    data = {}
    data.setdefault("name", character.name)
    data.setdefault("image", character.image)
    data.setdefault("icon", character.icon)

    attributes_data = []
    for attribute in character.attributes:
        attribute_data = JSONExporter.visit("attribute", attribute)
        attributes_data.append(attribute_data)
    
    data.setdefault("attributes", attributes_data)

    return data

@JSONExporter.register("attribute")
def export_attribute(attribute):
    data = {}
    data.setdefault("name", attribute.name)
    data.setdefault("value", attribute.value)

    return data
