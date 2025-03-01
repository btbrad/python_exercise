x = int(input("请输入X坐标："))
y = int(input("请输入Y坐标："))

if x == 0:
    print("在Y轴上")
elif y == 0:
    print("在X轴上")
elif x > 0 and y > 0:
    print("在第一象限")
elif x > 0 > y:
    print("在第二象限")
elif x < 0 and y < 0:
    print("在第三象限")
else:
    print("在第四象限")
