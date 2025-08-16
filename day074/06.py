'''
掷骰子，统计点数
'''
from random import randint

counter = [0] * 6

for i in range(6000):
    num = randint(1, 6)
    counter[num - 1] += 1

for i in range(6):
    print(f'点数{i + 1}出现的次数为：{counter[i]}')    