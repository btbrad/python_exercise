'''
在终端中打印如下图形
$
$$
$$$
$$$$
'''
row = int(input('请输入一个整数：'))

for x in range(row):
    print('$'*(x + 1))