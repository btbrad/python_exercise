'''
创建对象计数器，统计构造函数执行的次数，使用类变量实现并画出内存图。
'''
class Count:
    count = 0

    def __init__(self):
        Count.count += 1


Count()
Count()
Count()
Count()
Count()

print(Count. count)