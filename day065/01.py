from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String
from db_util import Base, Session

class News(Base):
    __tablename__ = 't_news2'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(32), nullable=False)
    phone = Column(String(11), unique=True)
    read_count = Column(Integer, default=1)
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)

def add_data():
    news1 = News(title='测试标题', phone='13888887777')
    with Session() as session:
        session.add(news1)
        session.commit()

def add_data2():
    news1 = News(title='测试标题2', phone='13888888888')
    with Session() as session:
        session.add(news1)
        session.commit()  

def add_data3():
    news1 = News(title='测试标题3', phone='13888889999')
    with Session() as session:
        session.add(news1)
        session.commit()   

def update_data():
    with Session() as session:
        news = session.query(News).filter_by(id=1).first()
        news.title = '测试列标题关键字'
        session.commit()                     

if __name__ == '__main__':
    # Base.metadata.create_all()
    # add_data()
    # add_data2()
    # add_data3()
    update_data()