# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

def making_divisor(num):
    divisor = 0
    for n in range(num): #n = 0の時を除くこと
        if(n != 0 and num % n == 0):
            divisor = divisor + n #ここでnum以外の約数の和ができる
    return divisor


def func_classifying(num, divisor):
    abs_num = abs(num - divisor)
    if(num == divisor):
        print("perfect")
    elif(abs_num ==  1):
        print("nearly")
    else:
        print("neither")


num = int(input())
list = []
for i in range(num):
    list.append(int(input()))
    div = making_divisor(list[i]) #ここで約数の生成
    func_classifying(list[i], div)
    
