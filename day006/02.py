num = input("请输入一个数字：")
if int(num) > 10:
    print(f"{num}是一个大于10的数。")
else:
    print(f"{num}是一个小于10的数。")

print(bool(range(0)))
print(bool([]))
print(bool({}))

age = int(input("请输入年龄："))
print("成年了" if age > 18 else "未成年")