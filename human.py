
class Human:
    def __init__(self):
        self.L = 0
        self.S_index = 0
        self.num_of_gotten_messages = 0
        self.S_index_original = 0

    """
    if a human, heard a rumor (or whisper), so it increases the number of gotten messages,
    and if in the same cycle, a human got 2 messages at least, so the S_index is decreased.
    """
    def heard_whisper(self):
        self.num_of_gotten_messages += 1
        if self.num_of_gotten_messages == 2 and self.S_index > 1:
            self.S_index -= 1

    """
    At the end of the cycle, this method is being called to reset the number of gotten messages,
    and the S_index is resets.
    """
    def reset(self):
        self.num_of_gotten_messages = 0
        self.S_index = self.S_index_original
    


