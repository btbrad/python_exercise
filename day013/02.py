try:
    a = input("请输入被除数：")
    b = input("请输入除数：")
    result = float(a) / float(b)
except ValueError:
    print("输入不合法！")
except ZeroDivisionError:
    print("除数不能为0")
except BaseException as e:
    print("出错了", e)
else:
    print(f"{a} / {b} = {result}")

