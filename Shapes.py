import math
import matplotlib.pyplot as plt
import numpy as np

x = []
y = []
z = []

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

    def draw(self):
            pass
    
    def volume(self):
        print("Volume is the area of a 3d shape.")
        pass

    def surface_area(self):
        print("Surface area is the total area of the outer surface of a 3d shape.")
        pass

class Torus(Shape3D):
    def __init__(self, type, colour, major_radius, minor_radius):
        super().__init__("Torus", colour)
        self.major_radius = major_radius
        self.minor_radius = minor_radius

    def draw(self, ax):
        u = np.linspace(0, 2 * math.pi, 100)
        v = np.linspace(0, 2 * math.pi, 50)

        u, v = np.meshgrid(u, v)

        x = (self.major_radius + self.minor_radius * np.cos(v)) * np.cos(u)
        y = (self.major_radius + self.minor_radius * np.cos(v)) * np.sin(u)
        z = self.minor_radius * np.sin(v)

        ax.plot_surface(x, y, z, color=self.colour)

        ax.set_box_aspect((1, 1, 1))
        pass

    def volume(self):
        return (math.pi * self.minor_radius ** 2) * (2 * math.pi * self.major_radius)

    def surface_area(self):
        return 4 * (math.pi)**2 * self.major_radius * self.minor_radius

    def get_major_radius(self):
                return self.major_radius

    def get_minor_radius(self):
                return self.minor_radius
            
    def set_major_radius(self, new_major_radius):
        self.major_radius = new_major_radius

    def set_minor_radius(self, new_minor_radius):
            self.minor_radius = new_minor_radius

class Oloid(Shape3D):
    def __init__(self, type, colour, radius):
        super().__init__("Oloid", colour)
        self.radius = radius

    def draw(self, ax):
            r = self.radius

            s = np.linspace(0, 2 * np.pi, 100)
            t = np.linspace(math.pi / 3, 5 * math.pi / 3, 120)

            S, T = np.meshgrid(s, t)

            X = r * (S / (1 - np.cos(T)) + (1 - S) * np.cos(T))
            Y = r * (1-S) * np.sin(T)
            Z = r * S * np.sqrt(np.maximum(0, 1 - 2 * np.cos(T)) / (1 - np.cos(T)))

            ax.plot_surface(X, Y, Z, color=self.colour)

            ax.plot_surface(X, Y, -Z, color=self.colour)

            ax.set_box_aspect((1, 1, 1))

            pass

    def volume(self):
        return 3.0524185 * self.radius ** 3 # approximately cause the 3.05 is not exact

    def surface_area(self):
        return 4 * math.pi * self.radius ** 2

    def get_radius(self):
            return self.radius
        
    def set_radius(self, new_radius):
        self.radius = new_radius

class Rhombicosidodecahedron(Shape3D):
    def __init__(self, type, colour, edge_length):
        super().__init__("Rhombicosidodecahedron", colour)
        self.edge = edge_length

    def draw(self):
        pass

    def volume(self):
        return ((60 + 29 * math.sqrt(5)) / 3) * (self.edge ** 3)

    def surface_area(self):
        return (30 + 5 * math.sqrt(3) + 3 * math.sqrt(25 + 10 * math.sqrt(5))) * self.edge ** 2

    def get_edge_length(self):
        return self.edge
    
    def set_edge_length(self, new_edge_length):
        self.edge = new_edge_length
