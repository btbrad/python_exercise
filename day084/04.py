"""
题目 3：九九乘法表

打印标准的 九九乘法表，格式如下：

1*1=1
1*2=2  2*2=4
1*3=3  2*3=6  3*3=9
...
"""


def multiplication_table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{j}*{i}={i*j}", end="\t")
        print("")


if __name__ == "__main__":
    multiplication_table()
