'''
 定义函数,在终端中打印一维列表
 list01 = [5, 546, 6, 56, 76, ]
for item in list01:
    print(item)
list02 = [7,6,879,9,909,]
for item in list02:
    print(item)
'''
list01 = [5, 546, 6, 56, 76, ]
list02 = [7,6,879,9,909,]

def print_list(l):
    for item in l:
        print(item)

print_list(list01)
print_list(list02)