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
        return f'<User id={self.id} name={self.name} age={self.age}>'
    

def create_data():
    Base.metadata.drop_all()
    Base.metadata.create_all()
    with Session() as session:
        for i in range(100):
            user = User(name=f'name{i+1}', age=randint(1, 100))
            session.add(user)
        session.commit()    

def query_data():
    with Session() as session:
        res = session.query(User.age, func.count(User.id)).group_by(User.age).all()
        print(res)

def query_data2():
    with Session() as session:
        res = session.query(User.age, func.count(User.id)).group_by(User.age).having(User.age < 18).all()
        print(res)        

if __name__ == '__main__':
    # create_data()     
    # query_data()   
    query_data2()   