default fortmap = load_fortmap()

init python:
    def load_fortmap():
        from models.fortmap import FortMap, Area
        areas = [
            "bcourts", "bridge", "carpark", "cohen", "currycourts", 
            "food", "fortstreet", "gym", "hall", "kilgour", 
            "library", "lkilgour", "lquad", "oval", "place", 
            "quad", "rowe", "rquad", "uquad", "valley", "wilkins", 
        ]

        fortmap = FortMap()
        for area in areas:
            fortmap.add_area(Area(area))

        return fortmap