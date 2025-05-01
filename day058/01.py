from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db_util import Base, Session, engine

class LoginUser(Base):
    __tablename__ = 't_user_login'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uname = Column(String(32), nullable=False)
    passwd = Column(String(32), nullable=False)
    
    def __repr__(self):
        return f'<User: id={self.id} uname={self.uname} passwd={self.passwd}>'
    

class User(Base):
    __tablename__ = 't_user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False, name='name')
    gender = Column(String(1))
    address = Column(String(64))
    login_id = Column(Integer, ForeignKey('t_user_login.id'))
    login_user = relationship('LoginUser', backref='user')

    def __repr__(self):
        return f'<User: id={self.id} name={self.name} gender={self.gender} address={self.address}>'
    
def add_data():
    login = LoginUser(uname='alex', passwd='123456')
    user = User(name='alex', gender='m', address='china')
    user.login_user = login
    with Session() as session:
        session.add(user)
        session.commit()

def query_data():
    with Session() as session:
        login = session.query(LoginUser).first()
        print(login)
        print(login.user)


if __name__ == '__main__':
    # Base.metadata.create_all(engine)
    # add_data()
    query_data()