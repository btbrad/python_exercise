'''
：一家公司有如下岗位：
 "经理"："曹操","刘备","孙权"
 "技术" ："曹操","刘备","张飞","关羽"
1. 定义数据结构,存储以上信息.
2. 是经理也是技术的都有谁?
3. 是经理不是技术的都有谁?
4. 不是经理是技术的都有谁?
5. 身兼一职的都有谁?
6. 公司总共有多少人数?
'''

set1 = {'曹操', '刘备', '孙权'}
set2 = {'曹操', '刘备', '张飞', '关羽'}

print(set1 & set2)
print(set1 - set2)
print(set2 - set1)
# print((set1 - set2) | (set2 - set1))
print(set1 ^ set2)
print(len(set1 | set2))