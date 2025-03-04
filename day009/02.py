def my_recursion(n):
    print(f"start:{n}")
    if n == 1:
        print("recursion over")
    else:
        my_recursion(n - 1)
    print(f"end:{n}")


my_recursion(3)


def f1(n, sum_n=0):
    if n == 1:
        return 1
    else:
        return n * f1(n - 1)


print(f1(5))
