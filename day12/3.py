'''
创建计算治愈比例的函数
confirmed = int(input("请输入确诊人数:"))
cure = int(input("请输入治愈人数:"))
cure_rate = cure / confirmed * 100
print("治愈比例为" + str(cure_rate) + "%")
'''

def cure_ratio():
    confirmed = int(input("请输入确诊人数:"))
    cure = int(input("请输入治愈人数:"))
    cure_rate = cure / confirmed * 100
    print("治愈比例为" + str(cure_rate) + "%")

cure_ratio()    