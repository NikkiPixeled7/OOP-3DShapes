import matplotlib.pyplot as plt
import numpy as np
from Shapes import Torus, Oloid, Cube
import tkinter as tk

def center_window(window, width, height):

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

first_shape = Torus("Torus", "Purple", 5, 1)
sec_shape = Oloid("Oloid", "Purple", 3)
third_shape = Cube("Cube", "Purple", 4)
shapes = [first_shape, sec_shape, third_shape]

for shape in shapes:
    print("Shape type: ", shape.get_type())
    print("Shape colour: ", shape.get_col())
    print("Shape volume: ", shape.volume())
    print("Shape surface area: ", shape.surface_area())
    print("-----------------------------")

def spawn_torus():
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

def spawn_oloid():
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

def spawn_cube():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    third_shape.draw(ax)
    ax.set_title("3D Shape: " + third_shape.get_type())
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_xticks(np.arange(-5, 6, 1))
    ax.set_yticks(np.arange(-5, 6, 1))
    ax.set_zticks(np.arange(-5, 6, 1))

    plt.show()

def homescreen():

    def torus_values():
        major_radius = float(entry_t1.get())
        minor_radius = float(entry_t2.get())
        first_shape.set_major_radius(major_radius)
        first_shape.set_minor_radius(minor_radius)
        print("Torus values updated: Major Radius =", major_radius, ", Minor Radius =", minor_radius)

    def oloid_values():
        radius = float(entry_o.get())
        sec_shape.set_radius(radius)
        print("Oloid values updated: Radius =", radius)

    def cube_values():
        edge_length = float(entry_c.get())
        third_shape.set_edge_length(edge_length)
        print("Cube values updated: Edge Length =", edge_length)

    window = tk.Tk()
    window.title("3D Shape Viewer")
    center_window(window, 750, 600)
    window.configure(bg="Purple")
    window.resizable(False, False)

    welcome_label = tk.Label(window, text="Choose A Shape:", font=("Times New Roman", 20, "bold"), bg="Purple")
    welcome_label.pack(pady=20)

    torus_button = tk.Button(window, text="Click for Torus", command=spawn_torus)
    torus_button.pack(pady=10, padx=35)

    entry_t1 = tk.Entry(window, placeholder="Enter major radius (default = 5)", font=("Arial", 12))
    entry_t1.pack(pady=5)

    entry_t2 = tk.Entry(window, placeholder="Enter minor radius (default = 1)", font=("Arial", 12))
    entry_t2.pack(pady=5)

    submit_btn_t = tk.Button(window, text="Submit", command=torus_values)
    submit_btn_t.pack(pady=10)

    pad_frame = tk.Frame(window, height=20, bg="Purple")
    pad_frame.pack(pady=12)

    oloid_button = tk.Button(window, text="Click for Oloid", command=spawn_oloid)
    oloid_button.pack(pady=10, padx=35)

    entry_o = tk.Entry(window, placeholder="Enter radius (default = 3)", font=("Arial", 12))
    entry_o.pack(pady=5)

    submit_btn_o = tk.Button(window, text="Submit", command=oloid_values)
    submit_btn_o.pack(pady=10)

    pad_frame2 = tk.Frame(window, height=20, bg="Purple")
    pad_frame2.pack(pady=12)

    cube_button = tk.Button(window, text="Click for Cube", command=spawn_cube)
    cube_button.pack(pady=10, padx=35)

    entry_c = tk.Entry(window, placeholder="Enter edge length (default = 4)", font=("Arial", 12))
    entry_c.pack(pady=5)

    submit_btn_c = tk.Button(window, text="Submit", command=cube_values)
    submit_btn_c.pack(pady=10)

    window.mainloop()

homescreen()
