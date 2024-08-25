'''
创建函数,根据课程阶段计算课程名称
number = input("请输入课程阶段数：")
if number == "1":
    print("Python语言核心编程")
elif number == "2":
    print("Python高级软件技术")
elif number == "3":
    print("Web全栈")
elif number == "4":
    print("项目实战")
elif number == "5":
    print("数据分析、人工智能")
'''
def calc_course():
    number = input("请输入课程阶段数：")
    if number == "1":
        print("Python语言核心编程")
    elif number == "2":
        print("Python高级软件技术")
    elif number == "3":
        print("Web全栈")
    elif number == "4":
        print("项目实战")
    elif number == "5":
        print("数据分析、人工智能")

calc_course()