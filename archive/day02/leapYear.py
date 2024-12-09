'''
 1. 公历年份是4的倍数，且不是100的倍数的
 2. 公历年份是整百数的,必须是400的倍数才是闰年
'''
year = int(input('请输入年份：'))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f'{year}是闰年！')
else:
    print(f'{year}不是闰年！')
