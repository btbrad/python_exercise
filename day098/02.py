"""
用for循环实现1-100之间的偶数求和
"""

total = 0
for x in range(2, 101, 2):
    total += x
print(total)
