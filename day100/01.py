"""
将一颗色子掷6000次，统计每个点数出现的次数
"""

import random

count_list = [0 for i in range(6)]

for n in range(6000):
    num = random.randint(1, 6)
    count_list[num - 1] += 1
for i in range(len(count_list)):
    print(f"{i + 1}点出现了{count_list[i]}次")
