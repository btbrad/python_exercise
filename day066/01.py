from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref
from db_util import Base, Session

class LoginUser(Base):
    __tablename__ = 't_users_login'
    id = Column(Integer, primary_key=True, autoincrement=True)
    uname = Column(String(32), nullable=False)
    passwd = Column(String(32), nullable=False)
    # user = relationship('User', uselist=False)
   
    def __repr__(self):
        return f'<User id={self.id}, uname={self.uname}, passwd={self.passwd}>'
    

class User(Base):
    __tablename__ = 't_users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False,name='name')
    gender = Column(String(1))
    address = Column(String(64))

    login_id = Column(Integer, ForeignKey('t_users_login.id'))
    login_user = relationship('LoginUser', backref=backref('user', uselist=False))

    def __repr__(self):
        return f'<UserInfo id={self.id}, name={self.name}, gender={self.gender}, address={self.address}>'
    
def create_data():
    # loginUser = LoginUser(uname='admin', passwd='123456')
    # user = User(name='alex', gender='m', address='china')
    loginUser = LoginUser(uname='bt', passwd='123456')
    user = User(name='btbrad', gender='m', address='china')
    user.login_user = loginUser 
    with Session() as session:
        session.add(user)
        session.commit()

def query_data():
    with Session() as session:
        # login = session.query(LoginUser).first()
        # print(login.user)
        user = session.query(User).filter(User.id==3).first()
        print(user.login_user)

if __name__ == '__main__':
    # Base.metadata.create_all()
    # create_data()
    query_data()