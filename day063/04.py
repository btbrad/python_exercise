from sqlalchemy import DECIMAL, Boolean, Column, Date, DateTime, Enum, Float, Integer, String, Text, Time, create_engine
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

class TagEnum(enum.Enum):
    Python = 'Python'
    Java = 'Java'
    JavaScript = 'JavaScript'


class News(Base):
    __tablename__ = 't_news'
    id = Column(Integer, primary_key=True, autoincrement=True)
    price1 = Column(Float) # 精度丢失
    price2 = Column(DECIMAL)
    title = Column(String(32))
    is_delete = Column(Boolean)
    tag1 = Column(Enum('Python', 'Java', 'JavaScript'))
    tag2 = Column(Enum(TagEnum))
    create_time = Column(Date)
    update_time = Column(DateTime)
    delete_time = Column(Time)
    content = Column(Text)


def add_data():
    news = News(
        price1=100.00078, 
        price2=100.00078, 
        title='new version of Python is coming', 
        is_delete=True, 
        tag1='Python', 
        tag2='Java',
        create_time=date(2025,5,28),
        update_time=datetime(2025,5,28,12,30,30),
        delete_time=time(12,30,30),
        content='Python is a programming language, please subscribe to my channel.'
    )
    with Session() as session:
        session.add(news)
        session.commit()

if __name__ == '__main__':
    # Base.metadata.create_all()
    add_data()