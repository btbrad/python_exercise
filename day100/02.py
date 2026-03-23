"""
基于match case 语法实现四则运算
"""

num1 = int(input("请输入第一个数字："))
num2 = int(input("请输入第二个数字："))
op = input("请输入运算符：")

try:
    match op:
        case "+":
            print(f"{num1} + {num2} = {num1 + num2}")
        case "-":
            print(f"{num1} - {num2} = {num1 - num2}")
        case "*":
            print(f"{num1} * {num2} = {num1 * num2}")
        case "/":
            print(f"{num1} / {num2} = {num1 / num2}")
        case _:
            print("请输入正确的运算符！")

except ZeroDivisionError as e:
    print("0不能作为除数！")
