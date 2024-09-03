'''
练习：创建手机类，实例化两个对象并调用其函数，最后画出内存图。
数据：品牌、价格、颜色
行为：通话
'''

class Phone:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def call(self):
        print(self.brand + ' is calling...')

xiaomi14 = Phone("xiaomi", "4500", "black")
onePlusAce3 = Phone("One Plus", "3500", "sliver")

xiaomi14.call()
onePlusAce3.call()