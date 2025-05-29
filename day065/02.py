from sqlalchemy import Column, Integer, String, func
from db_util import Base, Session

from random  import randint

class Item(Base):
    __tablename__ = 't_item'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(32))
    price = Column(Integer)

def add_data():
    with Session() as session:
        for i in range(1, 11):
            item = Item(title=f'测试标题{i}', price=randint(1, 100))
            session.add(item)
        session.commit() 

def query_data1():
    with Session() as session:
        items = session.query(Item).all()
        for item in items:
            print(item.id, item.title, item.price)   

def query_data2():
    with Session() as session:
        items = session.query(Item.title, Item.price).all()
        for item in items:
            print(item.title, item.price) 

def query_data3():
    with Session() as session:
        # rs = session.query(func.count(Item.id)).first()
        # rs = session.query(func.max(Item.price)).first()
        # rs = session.query(func.sum(Item.price)).first()
        # rs = session.query(func.avg(Item.price)).first()
        rs = session.query(func.min(Item.price)).first()
        print(rs)             

if __name__ == '__main__':
    # Base.metadata.create_all()    
    # add_data()
    # query_data1()
    # query_data2()
    query_data3()