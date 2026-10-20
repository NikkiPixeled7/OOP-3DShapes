import math
from Main import Shape3D
class Torus(Shape3D):
    def __init__(self, type, colour, major_radius, minor_radius):
        super().__init__(type, colour)
        self.major_radius = major_radius
        self.minor_radius = minor_radius

    def volume(self):
        return (math.pi * self.minor_radius ** 2) * (2 * math.pi * self.major_radius)

    def surface_area(self):
        return 4 * (math.pi)**2 * self.major_radius * self.minor_radius

class Oloid(Shape3D):
    def __init__(self, type, colour, radius):
        super().__init__(type, colour)
        self.radius = radius

    def volume(self):
        return 3.0524185 * self.radius ** 3 # approximately cause the 3.05 is not exact

    def surface_area(self):
        return 4 * math.pi * self.radius ** 2
