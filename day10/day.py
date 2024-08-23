'''
根据月日,计算是这一年的第几天.
公式：前几个月总天数 + 当月天数
例如：5月10日
计算：31 29 31 30 + 10
'''
tuple = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
month = int(input('请输入月:'))
day = int(input('请输入日：'))

sum = 0
for n in range(month - 1):
    sum += tuple[n]
sum += day
print(f'这一年的第{sum}天')
