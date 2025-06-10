from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db_util import Base, Session
from random import randint

class User(Base):
    __tablename__ = 't_user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    age  = Column(Integer)

    def __repr__(self):
        return f'<User name={self.name} age={self.age}>'


class News(Base):
    __tablename__ = 't_news'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(32), nullable=False)
    content = Column(String(32), nullable=False)
    read_count = Column(Integer)

    uid = Column(Integer, ForeignKey('t_user.id'), nullable=False)
    user = relationship('User', backref='news')

    def __repr__(self):
        return f'<News: title={self.title}, content={self.content}, read_count={self.read_count}>'


def create_data():
    with Session() as session:
        for i in range(10):
            user = User(name=f'user{i+1}', age=randint(18, 30))
            session.add(user)
        session.commit()  

def query_data():
    with Session() as session:
        # users = session.query(User).order_by(User.age).all()
        users = session.query(User).order_by(User.age.desc()).all()
        for user in users:
            print(user)



if __name__ == '__main__':
    # Base.metadata.drop_all()
    # Base.metadata.create_all()
    # create_data()
    query_data()