from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db_util import Base, Session


class User(Base):
    __tablename__ = 't_user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))


class Article(Base):
    __tablename__ = 't_article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(32))
    uid = Column(Integer, ForeignKey('t_user.id'), nullable=False)

    user = relationship('User', backref='articles')


def create_data():
    Base.metadata.drop_all()
    Base.metadata.create_all()
    user = User(name='alex')
    art1 = Article(title='article1')
    art2 = Article(title='article2')
    user.articles.append(art1)
    user.articles.append(art2)

    with Session() as session:
        session.add(user)
        session.commit()

def delete_data():
    with Session() as session:
        user = session.query(User).first()
        session.delete(user)
        session.commit()


if __name__ == '__main__':
    # create_data()
    delete_data()
    