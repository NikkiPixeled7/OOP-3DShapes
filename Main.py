import math
class Shape3D:
    def __init__(self, type, colour):
        self.type = type
        self.colour = colour

    def get_col(self):
        return self.colour

    def get_type(self):
        return self.type

    def set_col(self, new_colour):
        self.colour = new_colour

    def set_type(self, new_type):
        self.type = new_type
    
    def volume(self):
        print("Volume is the area of a 3d shape.")
        pass

    def surface_area(self):
        print("Surface area is the total area of the outer surface of a 3d shape.")
        pass
