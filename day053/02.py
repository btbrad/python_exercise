from flask import Flask, make_response, request

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)