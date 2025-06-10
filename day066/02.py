from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, backref
from db_util import Base, Session


news_tag = Table(
    't_news_tag', 
    Base.metadata,             
    Column('news_id', ForeignKey('t_news.id'), primary_key=True),
    Column('tag_id', ForeignKey('t_tag.id'), primary_key=True)
)

class News(Base):
    __tablename__ = 't_news'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(32), nullable=False)

    tags = relationship('Tag', secondary=news_tag, backref='news')
   
    def __repr__(self):
        return f"<News(id={self.id}, title='{self.title}')>"


class Tag(Base):
    __tablename__ = 't_tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False)

    def __repr__(self):
        return f"<Tag id={self.id}, name={self.name}>"
    

def create_data():
    news1 = News(title='Python更新了！！！')
    news2 = News(title='Java更新了！！！')
    tag1 = Tag(name='IT新闻')
    tag2 = Tag(name='科技新闻')
    news1.tags.append(tag1)
    news1.tags.append(tag2)
    news2.tags.append(tag1)
    news2.tags.append(tag2)

    with Session() as session:
        session.add(news1)
        session.add(news2)
        session.commit()


def query_data():
    with Session() as session:
        news = session.query(News).first()
        print(news.tags)


if __name__ == '__main__':
    # Base.metadata.create_all()
    # create_data()
    query_data()
    