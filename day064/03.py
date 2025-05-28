from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

HOST = 'localhost'
PORT = '3306'
DATABASE = 'flask_db'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

# 创建引擎
engine = create_engine(DB_URI)
# 创建一个基类
Base = declarative_base(engine)

class Person(Base):
    __tablename__ = 't_person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    age = Column(Integer)
    country = Column(String(32))

Session = sessionmaker(engine)

def create_data_one():
    with Session() as session:
        p1 = Person(name='alex', age=18, country='China')
        session.add(p1)
        session.commit()

def create_data_many():
    with Session() as session:
        p2 = Person(name='bob', age=19, country='China')
        p3 = Person(name='candy', age=20, country='China')
        session.add_all([p2, p3])
        session.commit()

def query_data_all():
    with Session() as session:
        persons = session.query(Person).all()
        for person in persons:
            print(person.id, person.name, person.age, person.country)  

def query_data_one():
    with Session() as session:
        person = session.query(Person).first()
        print(person.id, person.name, person.age, person.country)

def query_data_by_params():
    with Session() as session:
        # person = session.query(Person).filter_by(name='bob').first()
        person = session.query(Person).filter(Person.name=='bob').first()
        print(person.id, person.name, person.age, person.country)

def update_data():
    with Session() as session:
        person = session.query(Person).filter(Person.name=='bob').first()
        person.age = 28
        session.commit()  

def delete_data():
    with Session() as session:
        person = session.query(Person).filter_by(name='candy').first()
        session.delete(person)
        session.commit()                                            


if __name__ == '__main__':
    # create_data_one()
    # create_data_many()
    # query_data_all()
    # query_data_one()
    # query_data_by_params()
    # update_data()
    delete_data()