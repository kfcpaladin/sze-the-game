class FortMap(object):
    def __init__(self):
        self._areas = {}

    def add_area(self, area):
        id = area.name
        if id in self._areas:
            raise KeyError("Area {0} already exists".format(id))
        self._areas.setdefault(id, area)
    
    def contains_area(self, name):
        return name in self._areas
    
    def get_area(self, area):
        if area not in self._areas:
            raise KeyError("Unknown area {0}".format(area))
        return self._areas.get(area) 