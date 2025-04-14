import pymysql

cursor = None
connection = None

try:
    connection = pymysql.connect(host='127.0.0.1',user='root',password='123456',db='test',charset='utf8')

    cursor = connection.cursor()

    sql = "insert into employees(EMPLOYEE_ID, last_name, EMAIL, HIRE_DATE, JOB_ID) values(207,'张三', 'zhangsan@gmail.com', '2025-04-14', 'IT_PROG')"

    count = cursor.execute(sql)

    connection.commit()
except Exception as e:
    print(e)
    if connection:
      connection.rollback()
finally:
    if cursor:
      cursor.close()
    if connection:  
      connection.close()         