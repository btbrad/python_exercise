'''
题目 1：判断奇偶数

输入一个整数，输出它是奇数还是偶数。

示例：

输入: 7
输出: 奇数
'''
def even_or_odd():
    num = int(input('请输入一个整数：'))
    if num % 2 == 0:
        print('偶数')
    else:
        print('奇数')


if __name__ == "__main__":
    even_or_odd()               