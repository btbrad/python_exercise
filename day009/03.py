a = 1

def outer():
    b = 2

    def inner():
        nonlocal b
        print(f"inner: {b}")
        b = 20

        global a
        a = 10

    inner()
    print(f"outer: {b}")

outer()
print(f"global: {a}")
