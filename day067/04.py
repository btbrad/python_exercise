from sqlalchemy import Column, ForeignKey, Integer, String, func
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
        return f'<News id={self.id}, title={self.title}, content={self.content}, read_count={self.read_count}, uid={self.uid}>' 
    
def create_data():
    Base.metadata.drop_all()
    Base.metadata.create_all()
    with Session() as session:
        for i in range(2):
            user = User(name=f'name{i+1}', age=randint(1, 100))
            session.add(user)
        for i in range(10):
            news = News(title=f'title{i+1}', content=f'content{i+1}', read_count=randint(100, 1000), uid=randint(1, 2))
            session.add(news)
        session.commit()    

def query_data():
    with Session() as session:
        rs = session.query(User.name, func.count(News.id)).join(News).group_by(User.id).order_by(func.count(News.id)).all()
        print(rs)

if __name__ == '__main__':  
    # create_data()
    query_data()

