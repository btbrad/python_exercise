'''
定义函数，将列表中大于某个值的元素设置为None
 参数 结果
 [34, 545, 56, 7, 78, 8] -10-> [None,None,None,7,None,8]
 [34, 545, 56, 7, 78, 8] -100-> [34, None, 56, 7, 78, 8]
'''


def test_fun(l, n):
    for item in range(len(l)):
        if l[item] > n:
            l[item] = None
    return l


list_01 = [34, 545, 56, 7, 78, 8]
res1 = test_fun(list_01, 10)
print(res1)

list_02 = [34, 545, 56, 7, 78, 8]
res2 = test_fun(list_02, 100)
print(res2)
