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

    notifications_data = data.get("notifications", [])
    for notification_data in notifications_data:
        notifications = JSONImporter.visit("notifications", notification_data)
        for notification in notifications:
            character.add_notification(notification)

    return character

@JSONImporter.register("notifications")
def import_notifications(data):
    _type = data.get("type")
    messages_data = data.get("messages")

    if _type in ("attribute_change_message", "tutorial_message"):
        notifications = []
        for message_data in messages_data:
            notification = JSONImporter.visit(_type, message_data)
            notifications.append(notification)
        return notifications
    # priority compiles to asingle notification
    elif _type == "priority_attribute_message":
        notifications = []
        for attribute, message_list in messages_data.items():
            reformatted_data = {}
            reformatted_data.setdefault("attribute", attribute)
            reformatted_data.setdefault("messages", message_list)
            notification = JSONImporter.visit("priority_attribute_message", reformatted_data)
            notifications.append(notification)
        return notifications
    else:
        raise KeyError("Unknown notification type '{0}'".format(_type))



@JSONImporter.register("attribute")
def import_attribute(data):
    name = data.get("name")
    value = data.get("value")
    return Attribute(name, value)

