# チャリ旅のメンバー決定プログラミング

peo_0 = []
peo_1 = ["eng", 2, "man"]
peo_2 = ["", 2, "man"]
peo_3 = ["", 2, "woman"]
peo_4 = ["eng", 3, "man"]
peo_5 = ["eng", 3, "man"]
peo_6 = ["", 1, "woman"]
peo_7 = ["", 1, "woman"]
peo_8 = ["", 4, "man"]
peo_9 = ["", 4, "man"]
Human = [peo_1, peo_2, peo_3, peo_4, peo_5, peo_6, peo_7, peo_8, peo_9]
Eng = []
F = []
M = []
gr_1 = []
gr_2 = []
gr_3 = []

print(Human)

for i in range(9):
    if ("eng"in Human[i]) is True:
        Eng.append(Human[i])
print(Eng)

gr_1.append(Eng[0])
gr_2.append(Eng[1])
gr_3.append(Eng[2])

for i in range(9):
    if ("woman" in Human[i]) is True:
        F.append(Human[i])
    else:
        M.append(Human[i])

gr_1.append(F[0])
gr_2.append(F[1])
gr_3.append(F[2])

print(gr_1, gr_2, gr_3)
