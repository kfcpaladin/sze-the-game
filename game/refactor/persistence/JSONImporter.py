from . import serialisation

class BufferedImporter(serialisation.Visitor):
    def __init__(self):
        serialisation.Visitor.__init__(self) 
        self._buffered_data = [] 
        self._object_cache = {} 

    def parse_buffered_data(self):
        for data in self._buffered_data:
            data.accept(self)
        self._buffered_data = []

    def cache_object(self, _id, value):
        self._object_cache.setdefault(_id, value)

    def fetch_cached_object(self, _id):
        return self._object_cache.get(_id)

    def add_buffered_data(self, buffered_data):
        if buffered_data in self._buffered_data:
            index = self._buffered_data.index(buffered_data)
            data = self._buffered_data[index]
            data.extend(buffered_data)
        else:
            self._buffered_data.append(buffered_data)


class BufferedData(serialisation.Visitable):
    def __init__(self, handler_id, data):
        self.handler_id = handler_id
        self.data = data
        self.buffered_operations = []

    def __eq__(self, other):
        return other.handler_id == self.handler_id and \
               other.data == self.data
    
    def extend(self, other):
        self.buffered_operations.extend(other.buffered_operations)

    def add_buffered_operation(self, operation):
        self.buffered_operations.append(operation)

    def accept(self, visitor):
        value = visitor.visit(self.handler_id, self.data)
        self._on_parse(value)
        return value
    
    def _on_parse(self, value):
        for operation in self.buffered_operations:
            operation(value)


JSONImporter = BufferedImporter()