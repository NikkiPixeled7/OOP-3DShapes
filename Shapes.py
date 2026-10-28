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
        volume = (math.pi * self.minor_radius ** 2) * (2 * math.pi * self.major_radius)
        volume = round(volume, 2)
        return volume

    def surface_area(self):
        surface_area = 4 * (math.pi)**2 * self.major_radius * self.minor_radius
        surface_area = round(surface_area, 2)
        return surface_area

    def get_major_radius(self):
                return self.major_radius

    def get_minor_radius(self):
                return self.minor_radius
            
    def set_major_radius(self, new_major_radius):
        self.major_radius = new_major_radius

    def set_minor_radius(self, new_minor_radius):
            self.minor_radius = new_minor_radius


class Icosahedron(Shape3D):
    def __init__(self, type, colour, side_length):
        super().__init__("Icosahedron", colour)
        self.side_length = side_length

    def draw(self, ax):
        from mpl_toolkits.mplot3d.art3d import Poly3DCollection

        phi = (1 + math.sqrt(5)) / 2
        r = self.side_length

        vertices = np.array([
            [-1,  phi,  0],
            [ 1,  phi,  0],
            [-1, -phi,  0],
            [ 1, -phi,  0],
            [ 0, -1,  phi],
            [ 0,  1,  phi],
            [ 0, -1, -phi],
            [ 0,  1, -phi],
            [ phi,  0, -1],
            [ phi,  0,  1],
            [-phi,  0, -1],
            [-phi,  0,  1]
        ], dtype=float)

        vertices = vertices / np.linalg.norm(vertices[0]) * r

        from scipy.spatial import ConvexHull
        hull = ConvexHull(vertices)

        faces = vertices[hull.simplices]

        surface = Poly3DCollection(
            faces,
            facecolors=self.colour,
            edgecolors="black",
            linewidths=0.8,
            alpha=1.0
        )

        ax.add_collection3d(surface)

        ax.set_xlim(-r, r)
        ax.set_ylim(-r, r)
        ax.set_zlim(-r, r)
        ax.set_box_aspect((1, 1, 1))

    def volume(self):
        volume = ((5 * (3 + math.sqrt(5))) / 12) * (self.side_length ** 3)
        # the constant is 2.1816949906249123 which is more efficient but like this is cooler ^
        volume = round(volume, 2)
        return volume
    
    def surface_area(self):
        surface_area = 5 * math.sqrt(3) * (self.side_length ** 2)
        surface_area = round(surface_area, 2)
        return surface_area

    def get_side_length(self):
        return self.side_length

    def set_side_length(self, new_side_length):
        self.side_length = new_side_length

class Cube(Shape3D):
    def __init__(self, type, colour, edge_length):
        super().__init__("Cube", colour)
        self.edge = edge_length

    def draw(self, ax):
        from mpl_toolkits.mplot3d.art3d import Poly3DCollection

        r = self.edge / 2

        points = np.array([
            [-r, -r, -r],
            [ r, -r, -r],
            [ r,  r, -r],
            [-r,  r, -r],
            [-r, -r,  r],
            [ r, -r,  r],
            [ r,  r,  r],
            [-r,  r,  r]
        ])

        faces = [
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [0, 1, 5, 4],
            [2, 3, 7, 6],
            [1, 2, 6, 5],
            [0, 3, 7, 4]
        ]

        surface = Poly3DCollection(
            [points[face] for face in faces],
            facecolors=self.colour,
            edgecolors="black",
            linewidths=1
        )

        ax.add_collection3d(surface)

        ax.set_xlim(-r, r)
        ax.set_ylim(-r, r)
        ax.set_zlim(-r, r)
        ax.set_box_aspect((1, 1, 1))

    def volume(self):
        volume = self.edge ** 3
        volume = round(volume, 2)
        return volume

    def surface_area(self):
        surface_area = 6 * (self.edge ** 2)
        surface_area = round(surface_area, 2)
        return surface_area

    def get_edge_length(self):
        return self.edge

    def set_edge_length(self, new_edge_length):
        self.edge = new_edge_length
