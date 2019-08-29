from refactor.persistence import JSONExporter

@JSONExporter.register_handler("attribute")
def export_attribute(attribute):
    data = {}
    data.setdefault("name", attribute.name)
    data.setdefault("value", attribute.value)
    return data
