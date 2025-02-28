import random

count_list = [0, 0, 0, 0, 0, 0]

for _ in range(6000):
    res = random.randint(1, 6)
    count_list[res - 1] += 1

for index in range(6):
    print(f"{index + 1}点出现了{count_list[index]}次")
