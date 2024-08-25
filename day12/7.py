'''
创建函数,根据年龄计算人生阶段
age = int(input("请输入年龄："))
if age <= 6:
    print("童年")
elif age <= 17: # 程序能执行到本行,说明age一定大于6
    print("少年")
elif age <= 40:
    print("青年")
elif age <= 65:
    print("中年")
else:
    print("老年")
'''
def calc_life():
    age = int(input("请输入年龄："))
    if age <= 6:
        print("童年")
    elif age <= 17:  # 程序能执行到本行,说明age一定大于6
        print("少年")
    elif age <= 40:
        print("青年")
    elif age <= 65:
        print("中年")
    else:
        print("老年")

calc_life()