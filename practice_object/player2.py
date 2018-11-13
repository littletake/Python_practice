class Player2:
    def __init__(self):
        self.value = 0
        self.win_num = 0

    def janken_method(self, i):
        self.value = i % 3
