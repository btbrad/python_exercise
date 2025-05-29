from sqlalchemy import Column, ForeignKey, Integer, String, Text
from db_util import Base, Session
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 't_user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    uname = Column(String(50), nullable=False, name='name')

    def __repr__(self):
        return f'<User(id={self.id}, uname={self.uname})>'


class News(Base):
    __tablename__ = 't_news'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)
    uid = Column(Integer, ForeignKey('t_user.id'))

    user = relationship('User', backref='news')

    def __repr__(self):
        return f'<News: id={self.id} title={self.title} content={self.content} uid={self.uid}>'

def add_data():
    user1 = User(uname='alex')
    news1 = News(title='测试标题1', content='测试内容1', uid=1)
    news2 = News(title='测试标题2', content='测试内容2', uid=1)

    with Session() as session:
        session.add(user1)
        session.commit()

    with Session() as session:
        session.add(news1)
        session.add(news2)
        session.commit()    

def query_data():
    with Session() as session:
        news1 = session.query(News).first()
        print(news1)
        uid = news1.uid
        rs = session.query(User).filter(User.id == uid).first()
        print(rs)

def query_data2():
    with Session() as session:
        news1 = session.query(News).first()
        print(news1.user)

def query_data3():
    with Session() as session:
        user1 = session.query(User).first()
        print(user1.news)        

if __name__ == '__main__':
    # Base.metadata.create_all()
    # add_data()
    # query_data()
    # query_data2()
    query_data3()