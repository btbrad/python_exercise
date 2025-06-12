from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import enum
from datetime import date, datetime, time

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

Session = sessionmaker(engine)