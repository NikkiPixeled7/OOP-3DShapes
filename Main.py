import matplotlib.pyplot as plt
import numpy as np
from Shapes import Shape3D, Torus, Oloid, Rhombicosidodecahedron
import tkinter as tk

window = tk.Tk()
window.title("3D Shape Viewer")
window.geometry("400x300")
window.configure(bg="lightpurple")
window.resizable(False, False)

first_shape = Torus("Torus", "Purple", 5, 1)

print("Shape type: ", first_shape.get_type())
print("Shape colour: ", first_shape.get_col())
print("Shape volume: ", first_shape.volume())
print("Shape surface area: ", first_shape.surface_area())

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

first_shape.draw(ax)

ax.set_title("3D Shape: " + first_shape.get_type())
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

ax.set_xticks(np.arange(-5, 6, 1))
ax.set_yticks(np.arange(-5, 6, 1))
ax.set_zticks(np.arange(-5, 6, 1))

plt.show()
