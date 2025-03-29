import mysql.connector

# conn = mysql.connector.connect(
#     host="127.0.0.1",
#     user="vsearche",
#     password="vsearchpasswd",
#     database="vsearchlogdb"
# )
# print(111, conn)
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="rootpassword",
    database="vsearchlogdb"
)
cursor = conn.cursor()
try:
    _SQL = """describe log"""
    cursor.execute(_SQL)
    res = cursor.fetchall()
    for row in res:
        print(row)
except BaseException as e:
    print(e)
finally:
    cursor.close()
    conn.close()