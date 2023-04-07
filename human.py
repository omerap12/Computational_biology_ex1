global S
S = {1: 1, 2: 2/3, 3: 1/3, 4: 0}

class Human:
    def __init__(self):
        self.L = 0
        self.S_index = 0
        self.num_of_gotten_messages = 0
        self.S_index_original = 0

    def heard_whisper(self):
        self.num_of_gotten_messages += 1
        if self.num_of_gotten_messages == 2 and self.S_index > 1:
            self.S_index -= 1

    def reset(self):
        self.num_of_gotten_messages = 0
        self.S_index = self.S_index_original
    


