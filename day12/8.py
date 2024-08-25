'''
定义函数，根据年月日计算是这一年的第几天.
 如果2月是闰年,则29天平年28
'''
def is_leap():
    year = int(input("请输入年份:"))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        day = 29
    else:
        day = 28
    return day

def calc_day():
    feb_days = is_leap()
    month = int(input("请输入月:"))
    day = int(input("请输入日:"))
    days_of_month = (31, feb_days, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    total_days = sum(days_of_month[:month - 1])
    total_days += day
    print(f"{month}月{day}日是第{total_days}天.")

calc_day()