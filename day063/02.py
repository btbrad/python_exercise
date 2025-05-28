from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

HOST = 'localhost'
PORT = '3306'
DATABASE = 'flask_db'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

# 创建引擎
engine = create_engine(DB_URI)
# 创建一个基类
Base = declarative_base(engine)

class Person(Base):
    __tablename__ = 't_person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    age = Column(Integer)
    country = Column(String(32))

# 映射表结构
Base.metadata.create_all()    