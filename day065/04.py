from sqlalchemy import Column, ForeignKey, Integer, String, Text
from db_util import Base, Session

class User(Base):
    __tablename__ = 't_user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    uname = Column(String(50), nullable=False, name='name')


class News(Base):
    __tablename__ = 't_news'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)
    # uid = Column(Integer, ForeignKey('t_user.id', ondelete='RESTRICT'))
    # uid = Column(Integer, ForeignKey('t_user.id', ondelete='NO ACTION'))
    # uid = Column(Integer, ForeignKey('t_user.id', ondelete='CASCADE'))
    uid = Column(Integer, ForeignKey('t_user.id', ondelete='SET NULL'))

def add_data():
    user1 = User(uname='alex')
    news1 = News(title='测试标题1', content='测试内容1', uid=1)
    news2 = News(title='测试标题2', content='测试内容2', uid=1)

    with Session() as session:
        session.add(user1)
        session.commit()

    with Session() as session:
        session.add(news1)
        session.add(news2)
        session.commit()    


if __name__ == '__main__':
    Base.metadata.create_all()
    add_data()