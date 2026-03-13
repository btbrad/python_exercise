"""
比较运算符和逻辑运算符的使用
"""

flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)

print(f"flag0 = {flag0}")  # True
print(f"flag1 = {flag1}")  # True
print(f"flag2 = {flag2}")  # False
print(f"flag3 = {flag3}")  # False
print(f"flag4 = {flag4}")  # True
print(f"flag5 = {flag5}")  # False
