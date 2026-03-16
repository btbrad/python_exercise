"""
分段函数求值
"""

x = float(input("请输入x:"))
if x > 1:
    y = 3 * x - 5
elif x >= -1 and x <= 1:
    y = x + 2
else:
    y = 5 * x + 3
print(f"f({x}) = {y}")
