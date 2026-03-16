"""
英制单位英寸和公制单位厘米互换 1英寸=2.54厘米
"""

value = float(input("请输入数值："))
unit = input("请输入单位：")

if unit == "厘米" or unit == "cm":
    print(f"{value}{unit} = {value / 2.54:.2f}英寸(inch)")
elif unit == "英寸" or unit == "inch":
    print(f"{value}{unit} = {value * 2.54:.2f}厘米(cm)")
else:
    print("请输入有效的单位！")
