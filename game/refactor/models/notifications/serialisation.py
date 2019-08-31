from refactor.persistence import JSONImporter
from .AttributeChangeMessage import AttributeChangeMessage
from .TutorialMessage import TutorialMessage
from .PriorityAttributeMessage import PriorityMessage, PriorityAttributeMessage

@JSONImporter.register("attribute_change_message")
def import_change_message(data):
    attribute = data.get("attribute")
    msg_gain = data.get("msg_gain")
    msg_loss = data.get("msg_loss")
    return AttributeChangeMessage(attribute, msg_gain, msg_loss)

@JSONImporter.register("tutorial_message")
def import_tutorial_message(data):
    attribute = data.get("attribute")
    brief     = data.get("brief")
    msg_gain  = data.get("msgGain")
    msg_loss  = data.get("msgLoss")
    return TutorialMessage(attribute, brief, msg_gain, msg_loss)

@JSONImporter.register("priority_attribute_message")
def import_priority_attribute_message(data):
    attribute = data.get("attribute")
    messages_data = data.get("messages")

    message = PriorityAttributeMessage(attribute)
    for sub_message_data in messages_data:
        sub_message = JSONImporter.visit("priority_message", sub_message_data)
        message.add_entry(sub_message)

    return message

@JSONImporter.register("priority_message")
def import_priority_message(data):
    _min = data.get("min")
    message = data.get("msg")
    return PriorityMessage(message, _min)