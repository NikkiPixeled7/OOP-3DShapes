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
        from mpl_toolkits.mplot3d.art3d import Poly3DCollection
        from scipy.spatial import ConvexHull

        r = self.radius
        t = np.linspace(0, 2 * math.pi, 200, endpoint=False)

        circle1 = np.column_stack((
            r * np.cos(t),
            r * np.sin(t),
            np.zeros_like(t)
        ))

        circle2 = np.column_stack((
            -r * np.ones_like(t),
            r * np.cos(t),
            r * np.sin(t)
        ))

        points = np.vstack((circle1, circle2))

        hull = ConvexHull(points)
        triangles = points[hull.simplices]

        surface = Poly3DCollection(
            triangles,
            facecolors=self.colour,
            edgecolors=self.colour,
            linewidths=0.1,
            alpha=1.0
        )

        ax.add_collection3d(surface)

        ax.set_xlim(-r, 2 * r)
        ax.set_ylim(-r, r)
        ax.set_zlim(-r, r)
        ax.set_box_aspect((3, 2, 2))

    def volume(self):
        return 3.0524185 * self.radius ** 3

    def surface_area(self):
        return 4 * math.pi * self.radius ** 2

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius

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
        return self.edge ** 3

    def surface_area(self):
        return 6 * (self.edge ** 2)

    def get_edge_length(self):
        return self.edge

    def set_edge_length(self, new_edge_length):
        self.edge = new_edge_length
