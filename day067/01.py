from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db_util import Base, Session
from random import randint

class News(Base):
    __tablename__ = 't_news'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(32), nullable=False)
    content = Column(String(32), nullable=False)
    read_count = Column(Integer)
    
    def __repr__(self):
        return f'<News id={self.id} title={self.title} content={self.content} read_count={self.read_count}>'
    

def create_data():
    Base.metadata.drop_all()
    Base.metadata.create_all()
    with Session() as session:
        for i in range(10):
            news = News(title=f'title{i+1}', content=f'content{i+1}', read_count=randint(100, 1000))
            session.add(news)
        session.commit()  

def query_data():
    with Session() as session:
        newsList = session.query(News).limit(3).all()
        for news in newsList:
            print(news)

def query_data2():
    with Session() as session:
        newsList = session.query(News).offset(3).all()
        for news in newsList:
            print(news)     

def query_data3():
    # 获取第二页数据
    with Session() as session:
        newsList = session.query(News).limit(3).offset(3 * (2-1)).all()
        for news in newsList:
            print(news)     

def query_data4():
    with Session() as session:
        newsList = session.query(News).slice(3, 6).all()
        for news in newsList:
            print(news)  

def query_data5():
    with Session() as session:
        newsList = session.query(News).all()[3:6]
        for news in newsList:
            print(news)                            


if __name__ == '__main__':
    # create_data()
    # query_data()
    # query_data2()
    # query_data3()
    # query_data4()
    query_data5()
