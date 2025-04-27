from flask import Flask, request, g

from signals import login_space

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/login/')
def login():
    username = request.args.get('name')
    if username:
        g.name = username
        login_space.send()
        return '登录成功'
    else:
        return '登录失败'

if __name__ == '__main__':
    app.run(debug=True)