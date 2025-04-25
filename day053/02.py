from flask import Flask, make_response, request, session

app = Flask(__name__)

app.secret_key = 'i am a key'

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/set-cookie/')
def set_cookie():
    res = make_response('Setting a cookie')
    res.set_cookie('foo', 'bar')
    return res

@app.route('/get-cookie/')
def get_cookie():
    foo = request.cookies.get('foo')
    return f'get cookie: foo={foo}'

@app.route('/set-session/')
def set_session():
    session['foo'] = 'bar'
    return '设置了一个session'

@app.route('/get-session/')
def get_session():
    foo = session['foo']
    return f'读取了一个session: { foo }'

if __name__ == '__main__':
    app.run(debug=True)