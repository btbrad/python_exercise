import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="vsearche",
    password="vsearchpasswd",
    database="vsearchlogdb"
)
print(111, conn)
try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="vsearche",
        password="vsearchpasswd",
        database="vsearchlogdb"
    )
    print(111, conn)
    cursor = conn.cursor()
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