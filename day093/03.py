"""
写一个程序：

定义一个函数 find_max(nums)，接收一个整数列表 nums，返回其中的最大值。

从用户输入一串整数（用空格分隔），转换为列表，调用函数并输出最大值。
"""


def find_max(nums):
    return max(nums)


if __name__ == "__main__":
    input_str = input("请输入一组整数，用空格分隔：")
    num_list = list(map(int, input_str.split()))
    print("最大值为：", find_max(num_list))
