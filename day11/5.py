'''
对数字列表进行升序排列（小 --> 大）
'''

list1 = [5, 6, 23, 78, 1]
for x in range(len(list1) - 1):
    for y in range(len(list1) - x - 1):
        if list1[y] > list1[y+1]:
            list1[y], list1[y+1] = list1[y+1], list1[y]

print(list1)            