global S
S = {1: 1, 2: 2/3, 3: 1/3, 4: 0}

class Human:
    def __init__(self, L, S_index):
        self.L = L
        self.S_index = S_index
        self.num_of_gotten_messages = 0

    def heard_whisper(self):
        self.num_of_gotten_messages += 1
        if self.num_of_gotten_messages == 2 and self.S_index > 1:
            self.S_index -= 1

