try:
    a = 3 / 0
except BaseException as e:
    print(e)

while True:

    try:
        x = int(input("请输入一个数字："))
        print(f"输入的数字是：{x}")
    except BaseException as e:
        print("输入的不是数字", e)