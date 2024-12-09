'''
创建函数,计算IQ等级
ma = int(input("请输入你的心里年龄："))
ca = int(input("请输入你的实际年龄："))
iq = ma / ca * 100
if 140 <= iq:
    print("天才")
elif 120 <= iq:
    print("超常")
elif 110 <= iq:
    print("聪慧")
elif 90 <= iq:
    print("正常")
elif 80 <= iq:
    print("迟钝")
else:
    print("低能")
'''

def calc_iq():
    ma = int(input("请输入你的心里年龄："))
    ca = int(input("请输入你的实际年龄："))
    iq = ma / ca * 100
    if 140 <= iq:
        print("天才")
    elif 120 <= iq:
        print("超常")
    elif 110 <= iq:
        print("聪慧")
    elif 90 <= iq:
        print("正常")
    elif 80 <= iq:
        print("迟钝")
    else:
        print("低能")

calc_iq()