from sqlalchemy import create_engine, text

HOST = 'localhost'
PORT = '3306'
DATABASE = 'flask_db'
USERNAME = 'root'
PASSWORD = '123456'

DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

engine = create_engine(DB_URI)

sql = 'select 1;'


with engine.connect() as conn:
    rs = conn.execute(text(sql))
    print(rs.fetchone())