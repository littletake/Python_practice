import random


class Player1:
    # コンストラクタ生成
    def __init__(self):
        self.value = 0
        self.win_num = 0

    def janken_method(self):
        value = int(random.random() * 10)
        self.value = value % 3
