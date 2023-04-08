import random
from human import Human


class Cell:
    def __init__(self, row, col, p: float) -> None:
        self.row = row
        self.col = col
        self.human = Human() if random.random() < p else None
        self.color = "#F9F9F9"
        self.is_spreader = False

    """
    Choosing the cell number - if not human, default (grey) color. if human - color according to S_index.
    """
    def choose_color(self):
        if self.human is None:
            self.color = "#ffffff"
        else:
            # colors = ["#0000ff", "#ffff00", "#ff00ff", "#00ffff"]
            colors = ["#014f86", "#2c7da0", "#a9d6e5", "#b2f7ef"]
            self.color = colors[self.human.S_index - 1]