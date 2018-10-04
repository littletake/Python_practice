# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

def sort_func(list):
    while 1:
        for n in range(3):
            if(list[n] < list[n+1]):
                tmp = list[n]
                list[n] = list[n+1]
                list[n+1] = tmp
        if(list[0] >= list[1]) and (list[1] >= list[2]) and (list[2] >= list[3]):
            break


input_lines = input()
string = input_lines.split(" ")
list = []
for i in range(4):
    list.append(int(string[i]))

sort_func(list) #ここでsortが完了
ans_1 = list[0] * 10 + list[2]
ans_2 = list[1] * 10 + list[3]
ans = ans_1 + ans_2
print(ans)
