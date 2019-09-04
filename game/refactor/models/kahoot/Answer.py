class Answer(object):
    def __init__(self, description, points, message=None):
        self.description = description
        self.points = points
        self._message = message
    
    @property
    def message(self):
        if self._message is None:
            return "You selected {0}".format(self.description)
        return self._message