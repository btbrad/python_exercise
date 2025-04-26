from flask import Flask,session, request, render_template

app = Flask(__name__)

app.secret_key = 'secret'

@app.route('/')
def index():
    username = request.args.get('name')
    uname = session.get(username)
    if uname:
        return f'Hello {username}!'
    else:
        return f'{username}未登录'

@app.route('/login/')
def login():
    username = request.args.get('name')
    session[username] = username
    return '登录成功'

@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/goods/')
def goods():
    return render_template('goods.html')

@app.before_request
def before_first():
    print('每次请求时都执行！！！')


@app.context_processor
def my_context_processor():
    return {'slogan':'ha ha ha!'}

if __name__ == '__main__':
    app.run(debug=True)

