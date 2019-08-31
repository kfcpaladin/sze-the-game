import json
from refactor.persistence import JSONImporter

class NotificationLoader:

    def __init__(self):
        self._cache = {}
        self._handlers = {} 

    def load(self, handler_id, path):
        handler = self._handlers.get(handler_id, None)
        if not handler:
            raise KeyError("Handler {0} is not registered".format(handler_id))
        return handler(path)
    
    def register(self, handler_id):
        def wrapper(func):
            if handler_id in self._handlers:
                raise KeyError("Handler already regisitered {0}".format(handler_id))
            self._handlers.setdefault(handler_id, func)
            return func
        return wrapper

    def cache(self, func):
        def wrapped(path):
            value = self._cache.get(path, None)
            if not value:
                value = func(path)
                self._cache.setdefault(path, value)
            return value
        return wrapped

notification_loader = NotificationLoader()

@notification_loader.register("tutorial_message")
@notification_loader.cache
def load_tutorial_messages(path):
    return load_message_array(path, "tutorial_message")

@notification_loader.register("attribute_change_message")
@notification_loader.cache
def load_attribute_change_messages(path):
    return load_message_array(path, "attribute_change_message")

@notification_loader.register("priority_attribute_message")
@notification_loader.cache
def load_priority_attribute_message(path):
    messages = []
    with open(path, "r") as file:
        data = json.load(file)
        for attribute_name, messages_data in data.items():
            reformatted_data = {}
            reformatted_data.setdefault("attribute", attribute_name)
            reformatted_data.setdefault("messages", messages_data)
            message = JSONImporter.visit("priority_attribute_message", reformatted_data)
            messages.append(message)
    return messages

def load_message_array(path, handler):
    messages = []
    with open(path, "r") as file:
        datas = json.load(file)
        for data in datas:
            message = JSONImporter.visit(handler, data)
            messages.append(message)
    
    return messages



