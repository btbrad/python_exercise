from sqlalchemy import create_engine

HOST = 'localhost'
PORT = '3306'
DATABASE = 'flask_db'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

engine = create_engine(DB_URI)

# 执行一个sql
with engine.connect() as conn:
    sql = 'select 1'
    rs = conn.execute(sql)
    print(rs.fetchone())
    # sql = 'create table t_user(id int primary key auto_increment, name varchar(32))'
    # conn.execute(sql)