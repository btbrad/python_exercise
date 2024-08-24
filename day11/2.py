'''
二维列表
list01 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]
1. 将第一行从左到右逐行打印
效果：
1
2
3
4
5
2. 将第二行从右到左逐行打印
 效果：
10
9
8
7
 6
3. 将第三列行从上到下逐个打印
 效果：
3
 8
13
4. 将第四列行从下到上逐个打印
 效果：
14
9
4
5. 将二维列表以表格状打印
 效果：
1 2 3 4 5
 6 7 8 9 10
11 12 13 14 15
'''

list01 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]
# for x in list01[0]:
#     print(x)
# for x in range(len(list01[1]) - 1, -1, -1):
#     print(list01[1][x])
# for x in list01:
#     print(x[2])
# for x in range(len(list01) -1, -1, -1):
#     print(list01[x][3])
for x in list01:
    for y in x:
        print(y, end=' ')
    print('\t')