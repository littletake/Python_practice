from player1 import Player1
from player2 import Player2


def judge_method(value1, value2):
    if value1 == 0:
        if value2 == 1:
            return 1
        elif value2 == 2:
            return 2
        else:
            return 0
    elif value1 == 1:
        if value2 == 2:
            return 1
        elif value2 == 0:
            return 2
        else:
            return 0
    elif value1 == 2:
        if value2 == 0:
            return 1
        elif value2 == 1:
            return 2
        else:
            return 0
    else:
        return 0


# インスタンス生成
player1 = Player1()
player2 = Player2()

for n in range(10):
    player1.janken_method()
    player2.janken_method(n)

    win_num = judge_method(player1.value, player2.value)
    if win_num == 1:
        player1.win_num = player1.win_num + 1
    elif win_num == 2:
        player2.win_num = player2.win_num + 1

    print("出した手:%d, %d" % (player1.value, player2.value))
    print("勝ち数:%d, %d" % (player1.win_num, player2.win_num))
    print("")

if player1.win_num == player2.win_num:
    print("winner: None")
elif player1.win_num > player2.win_num:
    print("winner: Player1")
else:
    print("winner: Player2")
