staff_list = []
salary_sum = 0
count = 0

while count < 4:
    salary = input("请输入员工薪资, 输入Q或q结束：")

    if salary == 'q' or salary == 'Q':
        print("退出程序！")
        break

    salary = float(salary)

    if salary < 0:
        print("薪资小于0, 重新输入！")
        continue

    staff_list.append(salary)
    salary_sum += salary
    print("录入成功！")
    count += 1
else:
    print("4位员工薪资录入完成！")

print(f"薪资列表：{ staff_list }, 员工数：{len(staff_list)}，总工资：{salary_sum}")