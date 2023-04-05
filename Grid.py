import tkinter as tk
from Cell import Cell


class Grid:
    def __init__(self, width, height, cell_size, canvas):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.cells = [[Cell(row, col) for col in range(width)] for row in range(height)]
        self.selected_color = "#000000"  # black by default
        self.canvas = canvas

    def select_color(self, color):
        self.selected_color = color

    def paint_cell(self, event):
        row = event.y // self.cell_size
        col = event.x // self.cell_size
        self.cells[row][col].color = self.selected_color
        self.draw()

    def draw(self):
        for row in range(self.height):
            for col in range(self.width):
                color = self.cells[row][col].color
                x0 = col * self.cell_size
                y0 = row * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="#cccccc")
