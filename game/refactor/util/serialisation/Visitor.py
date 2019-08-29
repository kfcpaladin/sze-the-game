
class Visitor:
    def __init__(self):
        self.handlers = {}

    def register(self, handler_id):
        def wrapper(func):
            self.handlers.setdefault(handler_id, func)
            return func
        return wrapper

    def visit(self, handler_id, obj):
        handler = self.handlers.get(handler_id, None)
        if handler:
            return handler(obj)
        return None
            
