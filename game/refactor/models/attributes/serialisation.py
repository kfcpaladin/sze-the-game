from refactor.persistence import JSONImporter, JSONExporter
from .Attribute import Attribute
from .AttributeDependency import AttributeDependency

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

@JSONExporter.register("attribute")
def export_attribute(attribute):
    data = {}
    data.setdefault("name", attribute.name)
    data.setdefault("value", attribute.value)

    return data