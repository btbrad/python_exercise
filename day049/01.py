from flask import Flask, request, url_for, redirect, Response

app = Flask(__name__)

@app.route('/')
def index():
    username = request.args.get('username')
    age = request.values.get('age')
    return f'Hello Flask !--{username}--{age}'


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.values.get('password')
    return f'login--{username}--{password}'

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('pic')
    filename = f.filename
    with open(f'{filename}', 'wb') as tf:
        tf.write(f.read())
    # f.save(f'{filename}')
    return '上传成功'   

@app.route('/show_url/')
def show_url():
    url = url_for('index', name='张三', age=18)
    return f'反向查询到的url是：{url}' 

@app.route('/info/')
def info():
    return redirect('/show_url')

@app.route('/response/')
def response():
    response = Response('<h1 style="color: red;">Hello Flask</h1>', status=204)
    response.headers['Content-Type'] = 'text/html'
    return response

if __name__ == '__main__':
    app.run(debug=True)