import tkinter as tk
from Grid import Grid
import time


class Automation:
    def __init__(self):
        # create the tkinter window and canvas
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=100 * 10, height=100 * 10, bg="#ffffff")
        self.p_value = 0.5
        self.grid = Grid(self.root, 100, 100, 10, self.canvas, self.p_value)

        """
        class that initialize all the gui items that appears on the screen before clicking
        on the "Click to start" button. 
        """
    def initial_gui(self):
        # parameters for the gui - font and row offset
        font_labels = "Times 18 roman bold"
        row_offset = 20

        # initialize the canvas grid size
        self.canvas.grid(row=0, column=3, rowspan=60)
        label_P = tk.Label(self.root, text=f'P value is {self.p_value}', font=font_labels)
        label_P.grid(row=row_offset - 5, column=0, columnspan=3)
        row_offset += 1

        # add a text input
        label_L = tk.Label(self.root, text="L value:", font=font_labels)
        label_L.grid(row=row_offset, column=0)
        self.entry_L = tk.Entry(self.root, width=5)
        self.entry_L.grid(row=row_offset, column=1)
        row_offset += 1

        # add a text input
        label_running_time = tk.Label(self.root, text="Num generations:", font=font_labels, padx=5)
        label_running_time.grid(row=row_offset, column=0)
        self.entry_running_time = tk.Entry(self.root, width=5)
        self.entry_running_time.grid(row=row_offset, column=1)
        row_offset += 1

        # add a text input
        label_s1 = tk.Label(self.root, text="S1 value:", font=font_labels)
        label_s1.grid(row=row_offset, column=0)
        self.entry_s1 = tk.Entry(self.root, width=5)
        self.entry_s1.grid(row=row_offset, column=1)
        label_precentage = tk.Label(self.root, text="%", font=font_labels)
        label_precentage.grid(row=row_offset, column=2)
        row_offset += 1

        # add a text input
        label_s2 = tk.Label(self.root, text="S2 value:", font=font_labels)
        label_s2.grid(row=row_offset, column=0)
        self.entry_s2 = tk.Entry(self.root, width=5)
        self.entry_s2.grid(row=row_offset, column=1)
        label_precentage = tk.Label(self.root, text="%", font=font_labels)
        label_precentage.grid(row=row_offset, column=2)
        row_offset += 1

        # add a text input
        label_s3 = tk.Label(self.root, text="S3 value:", font=font_labels)
        label_s3.grid(row=row_offset, column=0)
        self.entry_s3 = tk.Entry(self.root, width=5)
        self.entry_s3.grid(row=row_offset, column=1)
        label_precentage = tk.Label(self.root, text="%", font=font_labels)
        label_precentage.grid(row=row_offset, column=2)
        row_offset += 1

        # add a text input
        label_s4 = tk.Label(self.root, text="S4 value:", font=font_labels)
        label_s4.grid(row=row_offset, column=0)
        self.entry_s4 = tk.Entry(self.root, width=5)
        self.entry_s4.grid(row=row_offset, column=1)
        label_precentage = tk.Label(self.root, text="%", font=font_labels)
        label_precentage.grid(row=row_offset, column=2)
        row_offset += 1

        # checkbox - slow or fast mode
        self.entry_checkbox = tk.IntVar()
        c1 = tk.Checkbutton(self.root, text='fast mode', variable=self.entry_checkbox, onvalue=1, offvalue=0,
                            font=font_labels)
        c1.grid(row=row_offset, column=0, columnspan=3)
        row_offset += 1
        self.button = tk.Button(self.root, text="Click to start", font=font_labels, command=self.start_process)
        self.button.grid(row=row_offset, column=0, columnspan=3)
        row_offset += 5

        # draing to the screen the colors palette
        label_color_pallet = tk.Label(self.root, text="Colors Pallet", font="Times 18 roman bold underline",
                                      underline=True)
        label_color_pallet.grid(row=row_offset, column=0)
        row_offset += 1

        # iterate over colors and labels inorder to show the colors palette
        colors = ["#014f86", "#2c7da0", "#a9d6e5", "#b2f7ef", "#F9F9F9"]
        labels = ["S1", "S2", "S3", "S4", "Non human"]
        for color, label in zip(colors, labels):
            label_tk = tk.Label(self.root, text=label, font=font_labels)
            label_tk.grid(row=row_offset, column=0)
            rectangle_tk = tk.Canvas(self.root, width=20, height=20, bg=color, borderwidth=1, highlightthickness=1,
                                     highlightbackground="#cccccc")
            rectangle_tk.grid(row=row_offset, column=1)
            row_offset += 1

        # our names' label
        label_names = tk.Label(self.root, text="By Omer Aplatony & Avital Aviv", font="Times 14 roman bold")
        label_names.grid(row=57, column=0, columnspan=3)

        # draw the initial grid
        self.grid.draw()
        # start the tkinter event loop
        self.root.mainloop()

    """
    Called when clicking on the "Click to Start" button". It disables the button, gets all the info
    from all gui entries, populate and start the simulation.
    """
    def start_process(self):
        self.button['state'] = 'disabled'
        self.grid.S1 = int(self.entry_s1.get()) / 100
        self.grid.S2 = int(self.entry_s2.get()) / 100
        self.grid.S3 = int(self.entry_s3.get()) / 100
        self.grid.S4 = int(self.entry_s4.get()) / 100
        self.grid.running_times = int(self.entry_running_time.get())
        self.grid.L = int(self.entry_L.get())
        mode = self.entry_checkbox.get()

        # slow mode - populated randomly
        if mode == 0:
            self.grid.populate_slow()
            self.grid.choose_spreader()
        # fast mode - populated in layers, the first spreader is chosen from the S1 layer.
        else:
            self.grid.populate_fast()
        time.sleep(3)
        self.grid.start_simulation()


if __name__ == "__main__":
    automation = Automation()
    automation.initial_gui()
