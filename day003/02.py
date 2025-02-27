"""
输入圆的半径计算计算周长和面积。
"""
import math

radius = float(input("请输入半径："))
perimeter = 2 * math.pi * radius
area = math.pi * radius**2
print(f"""
周长：{perimeter: .2f},
面积：{area: .2f}
""")