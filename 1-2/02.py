import time

a = time.time()
print(a)

totalYears = a//(60 * 60 * 24 * 365)
print(totalYears)

a = 1000
b = 1000
print(a is b)

a = 'hello'
b = 'hello'
print(a is b)

name = input("请输入名字：")
print("您的名字是***"+name+"***")

s = "abcde"
print(s[1:50])
print(s[::-1])