
class Visitor:
    def __init__(self):
        self.handlers = {}

    def register(self, handler_id):
        def wrapper(func):
            if handler_id in self.handlers:
                raise KeyError("Handler {0} already registered".format(handler_id))
            self.handlers.setdefault(handler_id, func)
            return func
        return wrapper

    def visit(self, handler_id, obj):
        handler = self.handlers.get(handler_id, None)
        if handler:
            return handler(obj)
        raise UnknownVisitorHandler(handler_id)

class UnknownVisitorHandler(Exception):
    def __init__(self, handler_id):
        Exception.__init__(self, "Unknown handler id {0}".format(handler_id))
        self.handler_id = handler_id
            
