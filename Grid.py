import tkinter as tk
from Cell import Cell
import random
import time


class Grid:
    def __init__(self, root, width, height, cell_size, canvas, p) -> None:
        self.master = root
        self.width = width
        self.height = height
        self.cell_size = cell_size
        # creating the cells with the decision if cell is human or not.
        self.cells = [[Cell(row, col, p) for col in range(width)] for row in range(height)]
        self.selected_color = "#000000"  # black by default
        self.canvas = canvas
        self.list_of_people = []
        self.running_times = 0

    """
    drawing to the screen all the cells according to their color. 
    Cells that has been spread a rumor get also a red rectangle inside them.
    """
    def draw(self) -> None:
        self.canvas.delete("all")
        for row in range(self.height):
            for col in range(self.width):
                color = self.cells[row][col].color
                x0 = col * self.cell_size
                y0 = row * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size
                cell = self.cells[row][col]
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="#cccccc")
                # For cells that spread a rumor - getting also a red rectangle inside them.
                if cell.is_spreader:
                    color = "#fe6d73"
                    offset = 2.7
                    self.canvas.create_rectangle(x0+offset, y0+offset, x1-offset, y1-offset, fill=color)
        # force to update the gui when finishing the iteration over the cells.
        self.master.update()

    """
    Function that saves all the cells that contains human in a list, and choose how to divide the humans according
    to the user's input (S1,S2,S3,S4 numbers).
    """
    def group_arranger(self) -> None:
        # calculate the number of people on the grid and save them in a list
        number_of_people = 0
        for row in range(len(self.cells)):
            for column in range(len(self.cells[0])):
                cell = self.cells[row][column]
                if cell.human is not None:
                    number_of_people += 1
                    self.list_of_people.append(cell)
        self.number_of_people = number_of_people
        sum_inputs = sum((self.S1, self.S2, self.S3, self.S4))
        # if the sum not sums to 100, add the remainder to S4
        if sum_inputs < 1:
            self.S4 += (100 - sum_inputs)/100
        S1_number, S2_number, S3_number, S4_number = int(number_of_people * self.S1), int(
            number_of_people * self.S2), int(number_of_people * self.S3), int(number_of_people * self.S4)
        # save the numbers in a dictionary
        self.index_to_S = {1: S1_number, 2: S2_number, 3: S3_number, 4: S4_number}

    """
    populate the S_i values to the cells with the humans randomly.
    """
    def populate_slow(self) -> None:
        self.group_arranger()
        copy_list_of_people = self.list_of_people.copy()
        random.shuffle(copy_list_of_people)
        while copy_list_of_people:
            # pop from the shuffled list
            cell = copy_list_of_people.pop()
            # select randomly a valid S index
            selected = self.assign_human_S()
            if selected == -1:
                break
            self.index_to_S[selected] -= 1
            cell.human.S_index = selected
            cell.human.S_index_original = selected
            cell.human.L = self.L
            cell.choose_color()
        self.draw()

    """
    iterate over the dict (key- S index, value- amount of S index) and while there is values
    create a list from all this values, pick randomly an S index.
    """
    def assign_human_S(self) -> int:
        available_choice = []
        for key, value in self.index_to_S.items():
            if value > 0:
                available_choice.append(key)
        try:
            return random.choice(available_choice)
        except IndexError:
            return -1

    """
    populate the cells with the humans in the layers method - first layer is the S1 humans, then S2 humans...
    the first spreader is chosen from the S1 layer inorder to make the rumor spread faster.
    """
    def populate_fast(self) -> None:
        self.group_arranger()
        # create a list of duplicates of all the groups to make the layers in the grid
        array_of_duplicates = [1]*self.index_to_S[1] + [2]*self.index_to_S[2] + [3]*self.index_to_S[3] + [4]*self.index_to_S[4]
        # choose the spreader from S1 - the group with the most high chance to spread.
        self.spreader = self.list_of_people[int(random.randint(0, self.index_to_S[1]))]
        self.spreader.is_spreader = True
        for row in range(len(self.cells)):
            for col in range(len(self.cells[0])):
                cell = self.cells[row][col]
                if cell.human is None:
                    continue
                cell.human.S_index = array_of_duplicates.pop(0)
                cell.human.S_index_original = cell.human.S_index
                cell.human.L = self.L
                cell.choose_color()
        self.draw()

    """
    choosing the spreader randomly for the slow population
    """
    def choose_spreader(self) -> None:
        self.spreader = random.choice(self.list_of_people)
        self.spreader.is_spreader = True

    """
    Creates a list of 4 neighbors. If a human in (i,j), it checks the cells (i+1,j), (i-1,j), (i,j+1), (i,j-1).   
    if these cells are humans so it is appended to the list. 
    """
    def get_4_neighbors(self, cell: Cell) -> list:
        neighbors = []
        if cell.row-1 >= 0 and self.cells[cell.row-1][cell.col].human:
            neighbors.append(self.cells[cell.row-1][cell.col])
        if cell.row+1 < len(self.cells) and self.cells[cell.row+1][cell.col].human:
            neighbors.append(self.cells[cell.row+1][cell.col])
        if cell.col-1 >= 0 and self.cells[cell.row][cell.col-1].human:
            neighbors.append(self.cells[cell.row][cell.col-1])
        if cell.col+1 < len(self.cells[0]) and self.cells[cell.row][cell.col+1].human:
            neighbors.append(self.cells[cell.row][cell.col+1])
        return neighbors

    """
    Creates a list of 8 neighbors. function calls to the 4 neighbors and also checks another 4 neighbors.  
    if a human in cell (i,j), it checks also the cells (i+1,j+1), (i+1,j-1), (i-1,j+1), (i-1, j-1). 
    if these cells are humans so it is appended to the list. 
    """
    def get_8_neighbors(self, cell: Cell) -> list:
        neighbors = []
        neighbors += self.get_4_neighbors(cell)
        if cell.row-1 >= 0 and cell.col-1 >= 0 and self.cells[cell.row-1][cell.col-1].human:
            neighbors.append(self.cells[cell.row-1][cell.col-1])
        if cell.row-1 >= 0 and cell.col+1 < len(self.cells[0]) and self.cells[cell.row-1][cell.col+1].human:
            neighbors.append(self.cells[cell.row-1][cell.col+1])
        if cell.row+1 < len(self.cells) and cell.col+1 < len(self.cells[0]) and self.cells[cell.row+1][cell.col+1].human:
            neighbors.append(self.cells[cell.row+1][cell.col+1])
        if cell.row+1 < len(self.cells) and cell.col-1 >= 0 and self.cells[cell.row+1][cell.col-1].human:
            neighbors.append(self.cells[cell.row+1][cell.col-1])
        return neighbors

    """
    Function starts the simulation by iterate over all the number of generations (user's input). 
    Every loop go over all spreaders and grab their neighbors if the L value is 0. 
    if L value is bigger than 0, it rejects the cell. The first spreader has an S_2 value. 
    """
    def start_simulation(self) -> None:
        # index of S index values
        S = {1: 1, 2: 2/3, 3: 1/3, 4: 0}
        spreaders = set()
        self.spreader.human.S_index = 2
        spreaders.add(self.spreader)
        for cycle in range(self.running_times):
            print(cycle)
            new_spreaders = set()
            for spreader in spreaders:
                # spreader can't spread a rumor anyway.
                if spreader.human.L > 0:
                    spreader.human.L -= 1
                    continue
                # if spreader.human.L = 0
                rand_num = random.random()
                if rand_num < float(S[spreader.human.S_index]):
                    neighbors = self.get_8_neighbors(spreader)
                    # if human has neighbors - initial again the L value.
                    if neighbors:
                        spreader.human.L = self.L
                    for neighbor in neighbors:
                        neighbor.is_spreader = True
                        new_spreaders.add(neighbor)
                        neighbor.human.heard_whisper()
                        neighbor.choose_color()
            # adding the new spreaders from the current iteration to the spreaders list.
            spreaders = spreaders.union(new_spreaders)
            time.sleep(1)
            self.draw()
            for people in self.list_of_people:
                people.human.reset()