import matplotlib.pyplot as plt
import numpy as np
from Shapes import Torus, Icosahedron, Cube
import tkinter as tk
from tkinter import messagebox, ttk

def center_window(window, width, height):

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

first_shape = Torus("Torus", "Purple", 5, 1)
sec_shape = Icosahedron("Icosahedron", "Purple", 3)
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

def spawn_Icosahedron():
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
        color = entry_tc.get()
        first_shape.set_major_radius(major_radius)
        first_shape.set_minor_radius(minor_radius)
        first_shape.set_col(color)
        print("Torus values updated: Major Radius =", major_radius, ", Minor Radius =", minor_radius, ", Color =", color)
        text = f"Surface Area: {first_shape.surface_area()}\nVolume: {first_shape.volume()}"
        messagebox.showinfo("Values Submitted.", text)

    def Icosahedron_values():
        side_length = float(entry_o.get())
        color = entry_oc.get()
        sec_shape.set_side_length(side_length)
        sec_shape.set_col(color)
        print("Icosahedron values updated: Radius =", side_length, ", Color =", color)
        text = f"Surface Area: {sec_shape.surface_area()}\nVolume: {sec_shape.volume()}"
        messagebox.showinfo("Values Submitted.", text)

    def cube_values():
        side_length = float(entry_c.get())
        color = entry_cc.get()
        third_shape.set_side_length(side_length)
        third_shape.set_col(color)
        print("Cube values updated: Edge Length =", side_length, ", Color =", color)
        text = f"Surface Area: {third_shape.surface_area()}\nVolume: {third_shape.volume()}"
        messagebox.showinfo("Values Submitted.", text)

    window = tk.Tk()
    window.title("3D Shape Viewer")
    center_window(window, 280, 600)
    window.configure(bg="#B48AEB")
    window.resizable(False, False)

    welcome_label = tk.Label(window, text="Choose A Shape:", font=("Times New Roman", 20, "bold"), bg="#B48AEB")
    welcome_label.pack(pady=2)

    instructions_text = tk.Label(window, text="*Drag Right-Click to Zoom*\n*Drag Middle-Click to Move*", font=("Times New Roman", 12), bg="#B48AEB")
    instructions_text.pack()

    seperator_frame = tk.Frame(window, bg="#A06AE7", height=1).pack(fill="x", pady=1)
    seperator_frame1 = tk.Frame(window, bg="#A06AE7", height=1).pack(fill="x", pady=1)

    torus_button = tk.Button(window, text="Click for Torus", command=spawn_torus)
    torus_button.pack(pady=10, padx=35)

    entry_t1 = tk.Entry(window, placeholder="Enter major radius (default = 5)", font=("Arial", 12))
    entry_t1.pack(pady=5)

    entry_t2 = tk.Entry(window, placeholder="Enter minor radius (default = 1)", font=("Arial", 12))
    entry_t2.pack(pady=5)

    entry_tc = tk.Entry(window, placeholder="Color (default = Purple)", font=("Arial", 12))
    entry_tc.pack(pady=5)

    submit_btn_t = tk.Button(window, text="Submit", command=torus_values)
    submit_btn_t.pack(pady=10)

    seperator_frame2 = tk.Frame(window, bg="#A06AE7", height=1).pack(fill="x", pady=1)
    seperator_frame21 = tk.Frame(window, bg="#A06AE7", height=1).pack(fill="x", pady=1)

    Icosahedron_button = tk.Button(window, text="Click for Icosahedron", command=spawn_Icosahedron)
    Icosahedron_button.pack(pady=10, padx=35)

    entry_o = tk.Entry(window, placeholder="Enter radius (default = 3)", font=("Arial", 12))
    entry_o.pack(pady=5)

    entry_oc = tk.Entry(window, placeholder="Color (default = Purple)", font=("Arial", 12))
    entry_oc.pack(pady=5)

    submit_btn_o = tk.Button(window, text="Submit", command=Icosahedron_values)
    submit_btn_o.pack(pady=10)

    seperator_frame3 = tk.Frame(window, bg="#A06AE7", height=1).pack(fill="x", pady=1)
    seperator_frame31 = tk.Frame(window, bg="#A06AE7", height=1).pack(fill="x", pady=1)

    cube_button = tk.Button(window, text="Click for Cube", command=spawn_cube)
    cube_button.pack(pady=10, padx=35)

    entry_c = tk.Entry(window, placeholder="Enter edge length (default = 4)", font=("Arial", 12))
    entry_c.pack(pady=5)

    entry_cc = tk.Entry(window, placeholder="Color (default = Purple)", font=("Arial", 12))
    entry_cc.pack(pady=5)

    submit_btn_c = tk.Button(window, text="Submit", command=cube_values)
    submit_btn_c.pack(pady=10)

    window.mainloop()

homescreen()
