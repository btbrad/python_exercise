import random

count = 0
target = random.randint(1, 100)

guess_num = 0

while guess_num != target:
    guess_num = int(input("请输入1-100的整数："))
    count += 1
    if guess_num < target:
        print("太小了")
    elif guess_num > target:
        print("太大了")
    else:
        print("猜中了！")
else:
    print(f"猜了{ count }次")