from sqlalchemy import Column, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship, backref, aliased
from db_util import Base, Session
from random import randint, choice

class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    pid = Column(Integer)

    def __repr__(self):
        return f'<City id={self.id} name={self.name} pid={self.pid}>'
    

def create_data():
    Base.metadata.drop_all()
    Base.metadata.create_all()
    city1 = City(id=1, name='北京', pid=0)
    city2 = City( id= 10, name='海淀', pid=1 )
    city3 = City( id= 11, name='朝阳', pid=1 )
    city4 = City( id= 2, name='上海', pid=0 )
    city5 = City( id= 20, name='浦东', pid=2 )
    city6 = City( id= 21, name='虹口', pid=2 )
    with Session() as session:
        session.add(city1)
        session.add(city2)
        session.add(city3)
        session.add(city4)
        session.add(city5)
        session.add(city6)
        session.commit()

def query_data():

    c = aliased(City)

    with Session() as session:
        rs = session.query(City.id, City.name, c.id, c.name).join(c, City.id == c.pid).all()
        for i in rs:
            print(i)

if __name__ == '__main__':
    # create_data()
    query_data()
    
    