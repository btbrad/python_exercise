"""
    找出所有水仙花数
"""

for x in range(100, 1000):
    a = x // 100
    b = (x - a * 100) // 10
    c = (x - a * 100 - b * 10)
    if (a ** 3 + b ** 3 + c ** 3) == x:
        print(x)