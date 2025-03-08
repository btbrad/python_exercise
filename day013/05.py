class AgeError(Exception):

    def __init__(self, errorInfo):
        super(AgeError, self).__init__()
        self.errorInfo = errorInfo

    def __str__(self):
        return str(self.errorInfo) + ", 年龄错误！"

if __name__ == "__main__":
    age = input("请输入年龄：")

    if float(age) < 30 or float(age) >150:
        raise AgeError(age)
    else:
        print("输入的年龄是：", age)