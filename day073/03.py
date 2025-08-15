'''
    判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积
    计算三角形的面积用海伦公式
'''
a = float(input("请输入边长 a: "))
b = float(input("请输入边长 b: "))  
c = float(input("请输入边长 c: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    perimeter = a + b + c
    p = perimeter / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(f"三角形的周长为: {perimeter}")
    print(f"三角形的面积为: {area}")
else:
    print("输入的边长不能构成三角形")
    