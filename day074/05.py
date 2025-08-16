'''
斐波那契数列前20位
'''
a, b = 0, 1

for i in range(20):
    a, b = b, a + b
    print(a)