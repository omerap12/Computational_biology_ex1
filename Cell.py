import random

class Cell:
    def __init__(self, row, col, p: float) -> None:
        self.row = row
        self.col = col
        self.human = 1 if random.random() < p else None
        self.color = "#ff00ff" if self.human else "#ffffff"
