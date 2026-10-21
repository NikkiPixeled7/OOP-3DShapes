import matplotlib.pyplot as plt
import numpy as np
from Shapes import Shape3D, Torus, Oloid, Rhombicosidodecahedron
import tkinter as tk

window = tk.Tk()
window.title("3D Shape Viewer")
window.geometry("400x300")
window.configure(bg="Purple")
window.resizable(False, False)

first_shape = Torus("Torus", "Purple", 5, 1)
sec_shape = Oloid("Oloid", "Purple", 3)
third_shape = Rhombicosidodecahedron("Rhombicosidodecahedron", "Pink", 2)
shapes = [first_shape, sec_shape, third_shape]


for shape in shapes:
    print("Shape type: ", shape.get_type())
    print("Shape colour: ", shape.get_col())
    print("Shape volume: ", shape.volume())
    print("Shape surface area: ", shape.surface_area())
    print("-----------------------------")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

sec_shape.draw(ax)


ax.set_title("3D Shape: " + sec_shape.get_type())
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

ax.set_xticks(np.arange(-5, 6, 1))
ax.set_yticks(np.arange(-5, 6, 1))
ax.set_zticks(np.arange(-5, 6, 1))

plt.show()
