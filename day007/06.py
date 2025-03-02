def add(a, b, c):
    sum_all = a + b + c
    print(f"{a} + {b} + {c} = {sum_all}")
    return sum_all

add(1, 2, 3)

def greater_than(a, b):
    return a > b

print(greater_than(1, 2))

def print_start(n):
    """
    打印n个*
    :param n: 个数
    :return: 无返回值
    """
    print("*"*n)

print_start(5)
help(print_start)
print(print_start.__doc__)