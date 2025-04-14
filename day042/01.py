import pymysql

connection = pymysql.connect(host='127.0.0.1',user='root',password='123456',db='test',charset='utf8')

cursor = connection.cursor()

sql = "select * from employees"

cursor.execute(sql)

result = cursor.fetchall()

for row in result:
    print(row)