'''
在终端中获取一个整数，作为边长，打印矩形。
效果：
请输入整数:5
$$$$$
$ $
$ $
$ $
$$$$$
'''

num = int(input('请输入整数：'))

for row in range(num):
    if row == 0 or row == num - 1:
        print('$' * num)
    else:
        s = ' ' * (num - 2)
        print('$' + s + '$')
