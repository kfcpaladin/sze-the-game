from refactor.persistence import JSONImporter, JSONExporter
from .Character import Character

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


