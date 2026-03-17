"""
输入两个正整数计算它们的最大公约数和最小公倍数
最小公倍数 = x × y ÷ 最大公约数
"""

x = int(input("x = "))
y = int(input("y = "))
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print(f"{x}和{y}的最大公约数是{factor}")
        print(f"{x}和{y}的最小公倍数是{x * y // factor}")
        break
