import tkinter as tk
from Cell import Cell
import random


class Grid:
    def __init__(self, width, height, cell_size, canvas,p):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.cells = [[Cell(row, col,p) for col in range(width)] for row in range(height)]
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

    def populate(self):
        # calculate the number of people on the grid
        number_of_people = 0
        for row in range(len(self.cells)):
            for column in range (len(self.cells[0])):
                cell = self.cells[row][column]
                if cell.human is not None:
                    number_of_people += 1
        self.number_of_people = number_of_people
        S1_number,S2_number,S3_number,S4_number = number_of_people*self.S1,number_of_people*self.S2,number_of_people*self.S3,number_of_people*self.S4
        self.index_to_S = {1:S1_number,2:S2_number,3:S3_number,4:S4_number}
        
        for row in range(len(self.cells)):
            for column in range (len(self.cells[0])):
                cell = self.cells[row][column]
                if cell.human is None:
                    continue
                selected = self.assign_human_S()
                self.index_to_S[selected] -= 1
                cell.human.S_index = selected
                cell.choose_color()

    def assign_human_S(self) -> int:
        available_choice = []
        for key, value in self.index_to_S.items():
            if value > 0:
                available_choice.append(key)
        return random.choice(available_choice)