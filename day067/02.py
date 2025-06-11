from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref
from db_util import Base, Session
from random import randint

class User(Base):
    __tablename__ = 't_user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    age = Column(Integer)

    def __repr__(self):
        return f'<User id={self.id}, name={self.name}, age={self.age}>'
    

class News(Base):
    __tablename__ = 't_news'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(32), nullable=False)
    content = Column(String(32), nullable=False)
    read_count = Column(Integer)

    uid = Column(Integer, ForeignKey('t_user.id'))
    user = relationship('User', backref=backref('news', lazy='dynamic'))

    def __repr__(self):
        return f'<News id={self.id}, title={self.title}, content={self.content}, read_count={self.read_count}>'
    

def create_data():
    with Session() as session:
        for i in range(10):
            user = User(name=f'user{i+1}', age=randint(1, 100))
            session.add(user)
        for i in range(10):
            news = News(title=f'title{i+1}', content=f'content{i+1}', read_count=randint(100, 1000))
            user.news.append(news)
        session.commit()    

def query_data():
    with Session() as session:
        users = session.query(User).all()
        newsList = users[-1].news.filter(News.read_count > 500).all()
        print(newsList)        


if __name__ == '__main__':
    # Base.metadata.drop_all()
    # Base.metadata.create_all()
    # create_data()
    query_data()
