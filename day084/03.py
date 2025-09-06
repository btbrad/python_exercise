'''
题目 2：列表求和

给定一个整数列表，写一个程序输出列表中所有元素的和。

示例：

输入: [1, 2, 3, 4, 5]
输出: 15
'''
def sum_list():
  input_str = input('请输入一组整数，用逗号分隔：')
  num_list = map(lambda x: int(x), input_str.split(','))
  print('数字之和为：', sum(num_list))

from functools import reduce

def sum_list2():
  input_str = input('请输入一组整数，用逗号分隔：')
  num_list = map(lambda x: int(x), input_str.split(','))
  print('数字之和为：', reduce(lambda x, y: x + y, num_list, 0))

if __name__ == "__main__":
  # sum_list()  
  sum_list2()  