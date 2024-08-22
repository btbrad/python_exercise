# 英制单位英寸和公制单位厘米互换 1英寸=2.54厘米

value = float(input('请输入数值：'))
unit = input('请输入单位：')

if unit == '英寸' or unit == 'inch':
    print(f'{value}英寸={value * 2.54}厘米')
elif unit == '厘米' or unit == 'cm':
    print(f'{value}厘米={value / 2.54}英寸')
else:
    print('输入错误！')
