from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

HOST = 'localhost'
PORT = '3306'
DATABASE = 'flask_db'
USERNAME = 'root'
PASSWORD = '123456'

DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

engine = create_engine(DB_URI)

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    age = Column(Integer)
    country = Column(String(32))

Session = sessionmaker(engine)

def create_data_one():
    with Session() as session:
        p1 = Person(name='alex', age=18, country='china')
        session.add(p1)
        session.commit()

def query_data_all():
    with Session() as session:
        all_data = session.query(Person).all()
        for data in all_data:
            print(data.id, data.name, data.age, data.country)

if __name__ == '__main__':
    # create_data_one()
    query_data_all()