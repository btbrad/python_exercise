from sqlalchemy import Column, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship, backref
from db_util import Base, Session
from random import randint, choice

class User(Base):
    __tablename__ = 't_user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    age = Column(Integer)
    def __repr__(self):
        return f'<User id={self.id}, name={self.name}, age={self.age}>'
    
def create_data():
    Base.metadata.drop_all()
    Base.metadata.create_all()
    names = ['张三', '李四', '王五']

    with Session() as session:
        for i in range(20):
            user = User(name=choice(names), age=randint(1, 20))
            session.add(user)
        session.commit()

def query_data():
    with Session() as session:
        sub_query = session.query(User.name.label('uname'), User.age.label('uage')).filter(User.name == '张三').limit(1).subquery()
        rs = session.query(User).filter(User.name == sub_query.c.uname, User.age == sub_query.c.uage).all()       
        print(rs)


if __name__ == '__main__':
    # create_data()
    query_data()