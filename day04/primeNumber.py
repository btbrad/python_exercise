'''
输入一个正整数判断是不是素数。
素数指的是只能被1和自身整除的大于1的整数。
'''

number = int(input('请输入一个整数：'))

other = False
for x in range(2, number):
    if number % x == 0:
        other = True
        break

if not other and number > 1:
    print(f'{number}是素数')
else:
    print(f'{number}不是素数')
