score = int(input("请输入学生成绩："))

if score < 0 or score > 100:
    print("非法输入")
else:
    if score < 60:
        print("不及格")
    elif score <= 79:
        print("及格")
    elif score <= 89:
        print("良好")
    else:
        print("优秀")
