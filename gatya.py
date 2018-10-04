#coding:utf-8
import numpy as np
import random
import time

def GetRandom():
    random = np.random.choice(["Rank5 servant","Rank4 servant","Rank3 servant",
                               "Rank5 reisou","Rank4 reisou","Rank3 reisou"],
                            p=[0.01, 0.03, 0.04, 0.12, 0.4, 0.4])
    return random

sh1 = False
sh2 = False
count = 0

while sh1 == False or sh2 == False:    #２種最低保証チェック
    sh1 = False
    sh2 = False
    haisyutu = []
    count = count + 1

    for i in range(10): #Rankselect
        haisyutu.append(GetRandom())

    for t in haisyutu:  #最低保証チェック 鯖
        if "servant" in t:
            sh1 = True
            break

    for t in haisyutu:  #最低保証チェック 星４以上
        if "Rank4" in t or "Rank5" in t:
            sh2 = True
            break

for s in haisyutu:  #servant & reisou nameselect
    if "Rank5 servant" in s:
        nameselect5s = random.choice(["A","B"])
        print(nameselect5s)

    elif "Rank4 servant" in s:
        nameselect4s = random.choice(["C","D"])
        print(nameselect4s)

    elif "Rank3 servant" in s:
        nameselect3s = random.choice(["E","F"])
        print(nameselect3s)

    elif "Rank5 reisou" in s:
        nameselect5r = random.choice(["G","H"])
        print(nameselect5r)

    elif "Rank4 reisou" in s:
        nameselect4r = random.choice(["I","J"])
        print(nameselect4r)

    elif "Rank3 reisou" in s:
        nameselect3r = random.choice(["K","L"])
        print(nameselect3r)

#表示
print("\n10連ガチャ\n")

for h in haisyutu:
    print("\n",h)

print("\n",count)

