from sqlalchemy import Column, Float, Integer, String, Text, and_, or_
from db_util import Base, Session
from random import randint
from uuid import uuid4

class Article(Base):
    __tablename__ = 't_article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(32), nullable=False)
    price = Column(Float, nullable=False)
    content = Column(Text)

    def __repr__(self):
        return f"<Article(id={self.id}, title={self.title}, price={self.price}, content={self.content})>"
    

def create_data():
    with Session() as session:
        for i in range(10):
            if i % 2 == 0:
                art = Article(title=f'title{i+1}', price=randint(1, 100), content=uuid4())
            else:
                art = Article(title=f'TITLE{i+1}', price=randint(1, 100)) 
            session.add(art)
        session.commit()

def query_data():
    with Session() as session:
        # rs = session.query(Article).filter_by(id=1).first()
        rs = session.query(Article).filter(Article.id==1).first()
        print(rs)  

def query_data2():
    with Session() as session:
        rs = session.query(Article).filter(Article.title != 'title2').all()
        for r in rs:
            print(r) 

def query_data3():
    with Session() as session:
        rs = session.query(Article).filter(Article.title.like('title%')).all()
        for r in rs:
            print(r)

def query_data4():
    with Session() as session:
        rs = session.query(Article).filter(Article.title.in_(['title1', 'title3', 'title6'])).all()
        for r in rs:
            print(r)  

def query_data5():
    with Session() as session:
        rs = session.query(Article).filter(~ Article.title.in_(['title1', 'title3', 'title6'])).all()
        for r in rs:
            print(r)  

def query_data6():
    with Session() as session:
        rs = session.query(Article).filter(~ Article.content is not None).all()
        for r in rs:
            print(r)  
            
def query_data7():
    with Session() as session:
        # rs = session.query(Article).filter(Article.title != 'title4' and Article.price > 50).all()
        # rs = session.query(Article).filter(Article.title != 'title4', Article.price > 50).all()
        rs = session.query(Article).filter(and_(Article.title != 'title4', Article.price > 50)).all()
        for r in rs:
            print(r)   

def query_data8():
    with Session() as session:
        rs = session.query(Article).filter(or_(Article.title != 'title4', Article.price > 50)).all()
        for r in rs:
            print(r)                                                                                

if __name__ == '__main__':
    # Base.metadata.create_all()
    # create_data()
    # query_data()              
    # query_data2()
    # query_data3()
    # query_data4()
    # query_data5()
    # query_data6()
    # query_data7()
    query_data8()
