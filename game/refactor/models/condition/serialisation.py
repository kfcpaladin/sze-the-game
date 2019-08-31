from refactor.persistence import JSONImporter, JSONExporter
from .Condition import *

@JSONImporter.register("condition")
def import_condition(data):
    _type = data.get("type")
    # not relationship
    if _type[0] == 'n':
        condition = JSONImporter.visit("condition_"+_type[1:], data)
        return Not(condition)
    # Normal condition
    return JSONImporter.visit("condition_"+_type, data)

@JSONImporter.register("condition_lt")
def import_less_than(data):
    value = data.get("value")
    return LessThan(value)

@JSONImporter.register("condition_eq")
def import_equal_to(data):
    value = data.get("value")
    return EqualTo(value)

@JSONImporter.register("condition_gt")
def import_greater_than(data):
    value = data.get("value")
    return GreaterThan(value)

@JSONImporter.register("condition_and")
def import_and(data):
    return import_composite(data, And)

@JSONImporter.register("condition_or")
def import_or(data):
    return import_composite(data, Or)

def import_composite(data, composite):
    conditions_data = data.get("conditions")
    conditions = []
    for condition_data in conditions_data:
        condition = JSONImporter.visit("condition", condition_data)
        conditions.append(condition)

    return composite(conditions)
    
