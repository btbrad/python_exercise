'''
判断素数
'''
num = int(input('请输入一个正整数：'))

isPrime = True

for i in range(2, num):
    if num % i == 0:
         isPrime = False

print(num, '是素数') if isPrime and num > 1 else print(num, '不是素数')
