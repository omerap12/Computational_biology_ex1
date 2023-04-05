import tkinter as tk
from Grid import Grid

global RUNNING_TIMES
global L
global S1
global S2
global S3
global S4

P = 0.2

# create the tkinter window and canvas
root = tk.Tk()
canvas = tk.Canvas(root, width=100 * 10, height=100 * 10, bg="#ffffff")
# create the grid
grid = Grid(100, 100, 10, canvas,P)
canvas.pack()

# add a text input
label_L = tk.Label(root, text="Enter L:")
label_L.pack(side="left")
entry_L = tk.Entry(root, width=10)
entry_L.pack(side="left")

# add a text input
label_running_time = tk.Label(root, text="Enter number of generation:")
label_running_time.pack(side="left")
entry_running_time = tk.Entry(root, width=10)
entry_running_time.pack(side="left")

# add a text input
label_s1 = tk.Label(root, text="S1:")
label_s1.pack(side="left")
entry_s1 = tk.Entry(root, width=10)
entry_s1.pack(side="left")

# add a text input
label_s2 = tk.Label(root, text="S2:")
label_s2.pack(side="left")
entry_s2 = tk.Entry(root, width=10)
entry_s2.pack(side="left")

# add a text input
label_s3 = tk.Label(root, text="S3:")
label_s3.pack(side="left")
entry_s3 = tk.Entry(root, width=10)
entry_s3.pack(side="left")

# add a text input
label_s4 = tk.Label(root, text="S4:")
label_s4.pack(side="left")
entry_s4 = tk.Entry(root, width=10)
entry_s4.pack(side="left")


def print_variables():
    L = entry_L.get()
    RUNNING_TIMES = entry_running_time.get()
    S1 = entry_s1.get()
    S2 = entry_s2.get()
    S3 = entry_s3.get()
    S4 = entry_s4.get()

button = tk.Button(root, text="Print BB", command=print_variables)
button.pack(side="top")

# # bind mouse click events to the canvas
# canvas.bind("<Button-1>", grid.paint_cell)

# create a color palette
palette = tk.Frame(root)
palette.pack(side="bottom")
# colors = ["#000000", "#ff0000", "#00ff00", "#0000ff", "#ffff00", "#ff00ff", "#00ffff"]

# draw the initial grid
grid.draw()

# start the tkinter event loop
root.mainloop()
