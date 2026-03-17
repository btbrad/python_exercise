"""
猜数字游戏的规则是：计算机出一个1到100之间的随机数，
玩家输入自己猜的数字，计算机给出对应的提示信息（大一点、小一点或猜对了），
如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。
"""

import random

target = random.randint(1, 100)
answer = None
count = 0

while answer != target:
    answer = int(input("请输入一个1~100之间的整数："))
    count += 1
    if answer > target:
        print("猜大了")
    elif answer < target:
        print("猜小了")
    else:
        print("猜对了")
        print(f"你猜了{count}次")
