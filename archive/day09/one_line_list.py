'''
练习：
生成10--30之间能被3或者5整除的数字
[10, 12, 15, 18, 20, 21, 24, 25, 27]
生成5 -- 20之间的数字平方
[25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
'''
list_1 = [item for item in range(10, 30) if not item % 3 or not item % 5]
print(list_1)

list_2 = [item**2 for item in range(5, 20)]
print(list_2)
