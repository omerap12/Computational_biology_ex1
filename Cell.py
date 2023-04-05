import random
from human import Human

class Cell:
    def __init__(self, row, col, p: float) -> None:
        self.row = row
        self.col = col
        self.human = Human() if random.random() < p else None
        self.color = "#F9F9F9"

    def choose_color(self):
        if self.human is None:
            self.color = "#ffffff"
        colors = ["#0000ff", "#ffff00", "#ff00ff", "#00ffff"]
        self.color = colors[self.human.S_index - 1]