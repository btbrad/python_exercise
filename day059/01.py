from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

HOST = 'localhost'
PORT = '3306'
DATABASE = 'flask_db'
USERNAME = 'root'
PASSWORD = '123456'

DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 't_user'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(32))

    def __repr__(self):
        return f'<User id={self.id}, name={self.name}>'
    

class News(db.Model):
    __tablename__ = 't_news'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    content = db.Column(db.String(128))

    uid = db.Column(db.Integer, db.ForeignKey('t_user.id'))
    user = db.relationship('User', backref = 'news')

    def __repr__(self):
        return f'<News id={self.id}, content={self.content}>'

def create_data():
    user = User(name = '张三')
    news = News(content = '张三在博客写了一篇文章')
    user.news.append(news)
    db.session.add(user)
    db.session.commit()

def query_data():
    users = User.query.all()
    for u in users:
        print(u.name)

def query_data_many():
    rs = db.session.query(User, News.content).join(News, User.id == News.uid).all()
    print(rs)        

def update_data():
    user = User.query.filter(User.id == 1).first()
    user.name = '李四'
    db.session.commit()    

def delete_data():
    news = News.query.filter(News.id == 1).first()
    db.session.delete(news)
    db.session.commit()

if __name__ == '__main__':
    # with app.app_context():
        # db.drop_all()
        # db.create_all()
        # create_data()  
        # query_data()    
        # query_data_many()
        # update_data()
        # delete_data()

    app.run(debug=True)
