'''
题目 3：最大值函数

写一个函数，接收一个整数列表，返回列表中的最大值（不能直接用 max() 函数）。
'''
def find_maximum(int_list):
  max_value = int_list[0]
  for x in int_list:
    if x > max_value:
        max_value = x
  return max_value

def find_maximum2(int_list):
  sorted_list = sorted(int_list)
  return sorted_list[-1]

if __name__ == "__main__":
  print(find_maximum([3, 5, 2, 8, 1]))        
  print(find_maximum2([3, 5, 2, 8, 1]))        